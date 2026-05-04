"""Library for handling BSL loading functions with Epec canLoader.
"""
import tempfile
import subprocess
import shutil
import re
from typing import Optional, Union
from pathlib import Path
from robot.api import logger


class can_loader_error(Exception):
    """Custom exception for canLoader operation failures.

    Primary error type for all canLoader-related failures, providing consistent interface for
    error handling. Wraps various underlying exceptions with descriptive messages.
    """


class can_loader:
    """ A utility class for canLoader operations. """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    DEFAULT_CAN_LOADER_BITRATE = "1000000"
    DEFAULT_SOURCE_DIR = Path(__file__).parent.resolve()
    DEFAULT_TARGET_DIR = Path.cwd().joinpath("~can_loader")
    EXE_FILE_NAME = "canLoader2.exe"
    DLL_FILE_NAME = "canLoader2.dll"

    CAN_LOADER_KNOWN_ERRORS = {
        "Failed to find channel": "canLoader2.exe did not find the specific can channel!"
    }

    def __init__(self, can_card_serial: str = "", device_serial_number: str = "", can_bitrate: str = DEFAULT_CAN_LOADER_BITRATE):
        """Initialize the can_loader library with CAN connection settings.

        Args:
        - `can_card_serial`: CAN adapter serial number
        - `device_serial_number`: Device Under Test serial number
        - `can_bitrate`: canLoader bitrate (default: 1000000)
        """
        self.can_card_serial = can_card_serial
        self.device_serial_number = device_serial_number
        self.can_bitrate = can_bitrate

        self.target_dir: Path = can_loader.DEFAULT_TARGET_DIR
        self.source_dir: Path = can_loader.DEFAULT_SOURCE_DIR

        self._executed_user_scripts: list[str] = []

    # =========================================================================
    # PUBLIC ROBOT FRAMEWORK KEYWORDS
    # =========================================================================

    def configure_connection(self, can_card_serial: str = "", device_serial_number: str = "", can_bitrate: Optional[str] = None, *,
                             source_dir: Optional[Path] = None, target_dir: Optional[Path] = None) -> None:
        """Configures library with CAN connection settings.
        - It's possible to override the arguments given in init
        - Source and target directories can be set for canLoader files, otherwise default are used.

        Args:
        - `can_card_serial`: CAN adapter serial number
        - `device_serial_number`: Device Under Test serial number
        - `can_bitrate`: canLoader bitrate (default: 1000000)
        - `source_dir`: canLoader2 directory path (leave empty for default path: The directory of this .py file)
        - `target_dir`: Directory to which all files are generated at runtime (leave empty for default path: cwd/~canloader)

        Examples:
        | Configure Connection | 12345678 | 10000 |
        | Configure Connection | 12345678 | 10000 | source_dir=C:\\user_canloader\\ | target_dir=${EXECDIR}\\user_canloader\\
        """
        if can_card_serial:
            self.can_card_serial = can_card_serial
        if device_serial_number:
            self.device_serial_number = device_serial_number

        if can_bitrate is not None:
            self.can_bitrate = can_bitrate

        if source_dir is not None:
            self.source_dir = source_dir
        if target_dir is not None:
            self.target_dir = target_dir

    def generate_files_for_canloader_and_execute_update(self, script_file_paths: Union[Path, list[Path]],
                                                        remove_target_dir: bool = False) -> None:
        """Generates files for canloader and executes update.

        - Creates all necessary files based on user script files
        - Executes all update batch files
        - Removes temporary directory after execution if remove_target_dir is set to True.

        Args:
        - `script_file_paths`: Single user script file path or list of user script file paths
        - `remove_target_dir`: Boolean to determine if target directory is removed after execution.

        Example:
        | ${script_file} | Set Variable | ${EXECDIR}\\canloader_scripts\\read_production_data.txt |
        | Generate Files For Canloader And Execute Update | script_file_paths=${script_file} |
        | Generate Files For Canloader And Execute Update | script_file_paths=${script_file} | remove_target_dir=${TRUE} |

        Or with multiple files:
        | ${script_file} | Set Variable | ${EXECDIR}\\canloader_scripts\\read_production_data.txt |
        | ${script_file2} | Set Variable | ${EXECDIR}\\canloader_scripts\\read_fw_log.txt |
        | @{script_files} | Create List | ${script_file} | ${script_file2} |
        | Generate Files For Canloader And Execute Update | script_file_paths=${script_files} |
        | Generate Files For Canloader And Execute Update | script_file_paths=${script_files} | remove_target_dir=${TRUE} |
        """
        # Accept single Path as well.
        if isinstance(script_file_paths, Path):
            script_file_paths = [script_file_paths]

        for script_file_path in script_file_paths:
            self.generate_files_for_canloader(script_file_path)

        self.execute_update(remove_target_dir)

    def generate_files_for_canloader(self, script_file_path: Path) -> None:
        """Generates files for canloader to be executed.

        - Creates directory for files if not exist
        - Creates new script file from user script
        - Creates batch file to run the new script file

        Args:
        - `script_file_path`: User script file path

        Example:
        | ${script_file} | Set Variable | ${EXECDIR}\\canloader_scripts\\read_production_data.txt |
        | Generate Files For Canloader | script_file_path=${script_file} |
        """
        # Verify source and target directories exist
        self._verify_directories()

        # Read user script file content
        original_script_content = self._read_file_content(
            file_path=script_file_path)
        sanitized_script_content = self._sanitize_script_content(
            original_script_content)

        # Generate filename prefix for new file
        executed_script_file_name_prefix = script_file_path.stem + "_"
        # Creates new file to target directory. Content is copied from user script
        executed_script_file_path = self._create_unique_file(
            content=sanitized_script_content, prefix=executed_script_file_name_prefix, suffix='.txt')

        # Checks whether any references .bin files found and copy to target dir if needed
        self._copy_script_related_binaries(script_file_path)

        # Creates .bat file to be executed
        batch_file = self._create_batch_file(executed_script_file_path)

        # Add to internal list
        self._executed_user_scripts.append(batch_file.name)

    def execute_update(self, remove_target_dir: bool = False) -> None:
        """Executes canloader by running batch file(s) already generated.

        - Run all update batch files
        - Cleans target directory if remove_target_dir is set to True (After execution)

        Args:
        - `remove_target_dir`: Boolean to determine if target directory is removed after execution.

        Example:
        | Execute Update |
        | Execute Update | remove_target_dir=${TRUE} |
        """
        # Ensure canLoader2.dll and .exe exists in target folder
        self._copy_canloader_lib_to_target_dir()

        # Ensure login script file and batch exists in target folder
        login_script_file = self._create_login_file()
        login_batch_file = self._create_batch_file(login_script_file)

        self._verify_execution_folder()

        try:
            self._execute_can_loader(login_batch_file, timeout_s=10)
            for user_script in self._executed_user_scripts:
                self._execute_can_loader(user_script)
        finally:
            # Cleanup batch files to be executed
            self.cleanup_files(remove_target_dir)

    def cleanup_files(self, remove_target_dir: bool = False) -> None:
        """Clears internal list of files to be executed.

        - Also cleans target directory, if remove_target_dir is set to True.

        Args:
        - `remove_target_dir`: Boolean to determine if the target dir is removed.

        Example:
        | Cleanup Files |
        | Cleanup Files | remove_target_dir=${TRUE} |
        """
        if remove_target_dir:
            shutil.rmtree(self.target_dir)
        self._executed_user_scripts = []

    # =========================================================================
    # PRIVATE METHODS
    # =========================================================================

    def _verify_directories(self) -> None:
        """Verifies source and target directories exits. Creates target directory if does not exist.

        Raises:
        - 'can_loader_error' : If source directory path does not exist.
        """
        # Setup source directory
        is_default_source = self.source_dir == can_loader.DEFAULT_SOURCE_DIR
        logger.info(
            f"Source directory {'(default)' if is_default_source else ''} set: {self.source_dir}")

        if not self.source_dir.is_dir():
            raise can_loader_error(
                f"Source directory not valid: {self.source_dir}")

        # Setup target directory
        is_default_target = self.target_dir == can_loader.DEFAULT_TARGET_DIR
        logger.info(
            f"Target directory {'(default)' if is_default_target else ''} set: {self.target_dir}")

        # Create target directory if it doesn't exist
        target_path = self.target_dir
        if not target_path.is_dir():
            target_path.mkdir(parents=True, exist_ok=True)
            logger.info(
                f"Created directory for canLoader files: {self.target_dir}")

    def _copy_canloader_lib_to_target_dir(self) -> None:
        """Copies canLoader2 files from source directory to target directory.
        """

        target_dll_file_path = self.target_dir.joinpath(
            can_loader.DLL_FILE_NAME)

        if not Path.is_file(target_dll_file_path):
            # Generate path and copy dll (use default filename for canLoader2 dll)
            source_dll_file_path = self.source_dir.joinpath(
                can_loader.DLL_FILE_NAME)

            logger.debug(
                f"Copy canLoader dll to target folder: {self.target_dir}")
            shutil.copy2(source_dll_file_path, target_dll_file_path)

        target_exe_file_path = self.target_dir.joinpath(
            can_loader.EXE_FILE_NAME)

        if not Path.is_file(target_exe_file_path):
            # Generate path and copy exe (use default filename for canLoader2 exe)
            source_exe_file_path = self.source_dir.joinpath(
                can_loader.EXE_FILE_NAME)

            logger.debug(
                f"Copy canLoader exe to target folder: {self.target_dir}")
            shutil.copy2(source_exe_file_path, target_exe_file_path)

    def _create_login_file(self) -> Path:
        """Creates login script file which is used to login device with serial number.

        Returns:
        - `login_file_path`: Returns the path of the generated login script file

        Raises:
        - 'can_loader_error' : If serial number is not defined
        """
        if not self.device_serial_number:
            raise can_loader_error("Device serial number not configured.")

        content = [
            'login',
            self.device_serial_number
        ]
        login_script = ' '.join(content)
        login_file_path = self.target_dir.joinpath(
            f"login_{self.device_serial_number}.txt")

        # Writes login command + device serial number to a file
        with open(login_file_path, "w", encoding="utf-8") as f:
            f.write(login_script)

        return login_file_path

    def _create_batch_file(self, script_file_path: Path) -> Path:
        """Creates temporary batch file which runs user defined script file.

        Args:
        - `script_file_path`: The path of the user script file

        Returns:
        - `batch_file_path`: Returns the path of the generated batch file

        Raises:
        - 'can_loader_error' : If input script file is not defined or CAN adapter serial number is not configured
        """
        if not self.can_card_serial:
            raise can_loader_error(
                "CAN adapter serial number not configured.")

        content = [
            'canLoader2',
            '-ifs',
            self.can_card_serial,
            '-cmd',
            script_file_path.name,
            '-bitrate',
            self.can_bitrate
        ]
        update_cmd = ' '.join(content)

        batch_file_name = script_file_path.stem + ".bat"
        batch_file_path = self.target_dir.joinpath(batch_file_name)
        logger.trace(f"Batch file '{batch_file_path}' content:\n{update_cmd}")

        with open(batch_file_path, "w", encoding="utf-8") as f:
            f.write(update_cmd)

        logger.debug(f"Created new batch file: {batch_file_path}")

        return batch_file_path

    def _create_unique_file(self, content: str, prefix: str = '', suffix: str = '.txt') -> Path:
        """Creates new unique named file and write content to it.

        Args:
        - `content`: String content to be written into file.
        - `prefix`: String content to be written into file (default: '')
        - `suffix`: Suffix for file name to be generated (default: '.txt').

        Returns:
        - `temp_path`: Returns the path of the generated file

        Raises:
        - 'can_loader_error' : If the content to be written is None or empty string.

        """
        if not content:
            raise can_loader_error("Script file content is empty.")

        with tempfile.NamedTemporaryFile(mode="w+t", encoding="utf-8", prefix=prefix, suffix=suffix, dir=self.target_dir, delete=False) as temp_file:
            temp_file.write(content)
            temp_path = Path(temp_file.name)

        return temp_path

    def _execute_can_loader(self, batch_file_name: str, timeout_s: int = 60) -> None:
        """Executes batch file which should contain canLoader call with arguments.

        Args:
        - `batch_file_name`: Batch file name to be executed.
        - `timeout_s`: Timeout in seconds to wait canLoader execution (default: 60, range: 0.01..3600s)

        Raises:
        - 'can_loader_error' : If the batch file name is not defined, timeout value is not within range or canLoader execution failed.

        """

        # Select batch file
        if not batch_file_name:
            raise can_loader_error("Batch file name not defined.")

        _timeout_s = int(timeout_s)
        if _timeout_s < 0.01 or _timeout_s > 3600:
            raise can_loader_error(f"Invalid timeout, given: {_timeout_s}")

        run_batch_file_path = self.target_dir.joinpath(batch_file_name)
        logger.info(
            f"Run batch file: {run_batch_file_path}")

        try:
            output_file_path = self.target_dir.joinpath(
                f'{Path(batch_file_name).stem}_std_out.log')
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                # Write std_out to file, because when PIPE arg used the timeout was not working correctly
                subprocess.run(run_batch_file_path, check=True, stdout=output_file,
                               timeout=_timeout_s, cwd=self.target_dir)

        except subprocess.TimeoutExpired as exc:
            raise can_loader_error(
                f"Possible issues:\n - Verify timeout value is sufficient\n - Verify CAN card serial number: {self.can_card_serial}\n{exc}") from exc

        except subprocess.CalledProcessError as e:
            with open(output_file_path, 'r', encoding='utf-8') as f:
                std_out_data = f.read()
            # Search for known errors
            # Raise exception with informative description if error is known,
            # otherwise raise 'Unknown error'.
            for known_error, error_info in can_loader.CAN_LOADER_KNOWN_ERRORS.items():
                if known_error in str(std_out_data):
                    raise can_loader_error(
                        f"'Known error: {known_error}' - {error_info} : {self.can_card_serial}\n{e}") from e
                raise can_loader_error(
                    f"'Unknown error.\n{e}") from e

    def _copy_script_related_binaries(self, script_file_path: Path) -> None:
        """Opens the script file and checks whether there are references binary files. If found, those binaries are copied to target folder.

        Args:
        - `script_file_path`: User script file path.

        Raises:
        - 'can_loader_error' : If the referenced binary file does not exist in the user script directory.
        """
        logger.debug(
            f"Find related binaries for script file: {script_file_path}")

        script_content = self._read_file_content(script_file_path)
        script_dir = script_file_path.parent.resolve()

        safe_bin_files, unsafe_bin_files = self._find_binaries_from_file_content(
            script_content)

        # Sanitize unsafe binary names
        for unsafe_bin_file in unsafe_bin_files:
            unsafe_bin_file_name = Path(unsafe_bin_file).stem.replace(".", "_")
            safe_bin_file = unsafe_bin_file_name + ".bin"
            # Copy unsafe binary files with safe name
            unsafe_bin_file_path = script_dir.joinpath(unsafe_bin_file)
            if not unsafe_bin_file_path.is_file():
                raise can_loader_error(
                    f"Referenced binary file not found: '{unsafe_bin_file}' from script folder '{script_dir}'")
            shutil.copy2(unsafe_bin_file_path,
                         self.target_dir.joinpath(safe_bin_file))

        logger.debug(
            f"{'No binary files found in given script.' if not safe_bin_files else f'List of binary files to be copied: {safe_bin_files}'}")

        for bin_file in safe_bin_files:
            bin_file_path = script_dir.joinpath(bin_file)
            if not bin_file_path.is_file():
                raise can_loader_error(
                    f"Referenced binary file not found: '{bin_file}' from script folder '{script_dir}'")

            shutil.copy2(bin_file_path, self.target_dir)
            logger.debug(f"'{bin_file_path}' copied to '{self.target_dir}'")

    def _find_binaries_from_file_content(self, file_content: str) -> tuple[list, list]:
        """Find safe and unsafe binaries from file content.

        Args:
        - `file_path`: File path to be read.

        Returns:
        - `safe_bin_files, unsafe_bin_files`: Returns a tuple containing two separate binary lists.
        """
        # Find all binary filenames which come after 'load' command. Ignore case.
        safe_binaries = re.compile(r"LOAD\s([\w]+\.BIN)", re.IGNORECASE)
        # Get binaries with dots in the name as well. These need to be renamed for safety.
        unsafe_binaries = re.compile(
            r"LOAD\s(\w+(?:\.\w+)+\.BIN)", re.IGNORECASE)
        safe_bin_files = safe_binaries.findall(file_content)
        unsafe_bin_files = unsafe_binaries.findall(file_content)

        return safe_bin_files, unsafe_bin_files

    def _read_file_content(self, file_path: Path) -> str:
        """Reads content of a file.

        Args:
        - `file_path`: File path to be read.

        Returns:
        - `file_content`: Returns the content of the file.

        Raises:
        - 'can_loader_error' : If the file path does not exist.

        """
        if not file_path.is_file:
            raise can_loader_error("File path not valid.")

        with open(file_path, encoding='utf-8', mode='r') as f:
            file_content = f.read()

        logger.trace(f"File content:\n {file_content}")

        return file_content

    def _sanitize_script_content(self, content: str) -> str:
        """Take file content and sanitize binary names that contain dots.

        Args:
        - `content`: Content of the file to sanitize.

        Returns
        - `content`: Returns the original content or sanitized content of the file.
        """
        _, unsafe_bin_files = self._find_binaries_from_file_content(
            content)
        for unsafe_bin_file in unsafe_bin_files:
            unsafe_bin_file_name = Path(unsafe_bin_file).stem.replace(".", "_")
            safe_bin_file = unsafe_bin_file_name + ".bin"
            content = content.replace(unsafe_bin_file, safe_bin_file)
        return content

    def _verify_execution_folder(self) -> None:
        """This function verifies the contents of the execution target folder before execution.

        Checks txt and batch file contents and verifies everything is found.

        Raises:
        - 'can_loader_error': If something is wrong with the contents.
        """
        logger.info(
            "Verifying canloader execution folder: {self.target_dir}")
        error_list = []
        bin_files = [
            bin_file.name for bin_file in self.target_dir.glob('*.bin')]
        bat_files = [
            bat_file.name for bat_file in self.target_dir.glob('*.bat')]
        txt_files = [
            txt_file.name for txt_file in self.target_dir.glob('*.txt')]
        logger.info(f"Binary files found: {(','.join(bin_files))}")
        logger.info(f"Text files found: {(','.join(txt_files))}")
        logger.info(f"Batch files found: {(','.join(bat_files))}")

        # Check that canloader is found.
        canloader_exe = Path(
            self.target_dir.joinpath(can_loader.EXE_FILE_NAME))
        canloader_dir = Path(
            self.target_dir.joinpath(can_loader.DLL_FILE_NAME))

        if not canloader_exe.is_file():
            error_list.append(
                f"{can_loader.EXE_FILE_NAME} not found in {self.target_dir}")
        if not canloader_dir.is_file():
            error_list.append(
                f"{can_loader.DLL_FILE_NAME} not found in {self.target_dir}")

        # Check that binaries and correct batch files are found.
        for txt_file in txt_files:
            txt_file_content = self._read_file_content(
                self.target_dir.joinpath(txt_file))
            safe_binaries, unsafe_binaries = self._find_binaries_from_file_content(
                txt_file_content)
            if unsafe_binaries:
                error_list.append(
                    f"Unsafe binaries found in {txt_file}:\n{unsafe_binaries}")
            for binary in safe_binaries:
                if binary not in bin_files:
                    error_list.append(
                        f"{binary} from {txt_file} not found in {self.target_dir}"
                    )
            if txt_file.replace(".txt", ".bat") not in bat_files:
                error_list.append(
                    f"The required batch file for {txt_file} not found in directory {self.target_dir}")

        # Check and verify batch file contents
        for bat_file in bat_files:
            bat_file_content = self._read_file_content(
                self.target_dir.joinpath(bat_file)
            )
            logger.debug(f"{bat_file} contents: {bat_file_content}")
            logger.info(
                f"Checking {bat_file} for correct CAN card serial number.")
            if not f"-ifs {self.can_card_serial}" in bat_file_content:
                error_list.append(
                    f"Wanted CAN card serial not found in {bat_file}: {self.can_card_serial}")
            logger.info(
                f"Checking {bat_file} for correct bitrate.")
            if not f"-bitrate {self.can_bitrate}" in bat_file_content:
                error_list.append(
                    f"Wanted bitrate not found in {bat_file}: {self.can_card_serial}")
            logger.info(f"Checking that the .txt file {bat_file} uses exists.")
            txt_pattern = re.compile(r'[\w.-]+\.txt', re.IGNORECASE)
            bat_txt_files = txt_pattern.findall(bat_file_content)
            for bat_txt_file in bat_txt_files:
                if bat_txt_file not in txt_files:
                    raise error_list.append(
                        f"Wanted txt file: {bat_txt_file} not found in directory {self.target_dir}")

        # Raise can_loader_error with numbered errors, if errors are found.
        if error_list:
            raise can_loader_error(
                "Errors found during verification:\n\n" +
                "\n".join([f"Error {i+1}: {error}" for i,
                           error in enumerate(error_list)]))
        logger.info("No errors found during verification.")
