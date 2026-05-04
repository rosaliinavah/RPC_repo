"""
Python library to implement API class for Codesys
"""
import socket
import time
import configparser
import json
import re
from datetime import datetime
from robot.api import logger

# A constant list variable for different CODESYS errors that can occur and need to be caught.
CODESYS_ERRORS = [
    "Object reference not set to an instance of an object.",
    "No device description was found because the following parameters are wrong:",
    "Login failed:",
    "Value cannot be null.",
    "Unable to rename entry",
    "No devdesc installed for 'Device'",
    "Root element is missing.",
    "No connection to the device. Please rescan your network.",
    "Network error:",
    "No primary project loaded.",
    "The selected project is currently in use",
    "Invalid expression",
    "is not a literal."]

RET_TYPES = {
    "bin": bin,
    "hex": hex,
    "int": int,
    "float": float,
    "bool": bool
}


class codesys_client:
    """
    Socket client class used with communication with codesys_client_server.
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self, config_file: str = "") -> None:
        """
        Main constructor for codesys_client. Reads host and port parameters from given configuration file.

        *Arguments:*

        config_file (str): Path or name of file.
        """
        try:
            self.config = configparser.ConfigParser()
            self.config.read(config_file)
            self.host = self.config.get('socket_api_client', 'host')
            self.port = int(self.config.get('socket_api_client', 'port'))
            self.device_host = None
            self.device_gateway = None
        except BaseException:
            codesys_client.__timed_logger("No config file given.")

    @staticmethod
    def __timed_logger(data: str, loglevel: str = "Info") -> None:
        """
        Just a print function that adds current time to print.

        *Arguments:*

        data: Text to be logged
        loglevel: Level to use for logging (info, debug, warn, error)
        """
        _time = datetime.now().strftime("%H:%M:%S")
        if loglevel.lower() == "info":
            logger.info(f"[ {_time} ] - {data}", also_console=True)
        if loglevel.lower() == "debug":
            logger.debug(f"[ {_time} ] - {data}")
        if loglevel.lower() == "warn":
            logger.warn(f"[ {_time} ] - {data}")
        if loglevel.lower() == "error":
            logger.error(f"[ {_time} ] - {data}")

    @staticmethod
    def __json_convert(data: str) -> dict:
        """
        Try to convert given data string to JSON format.

        *Arguments:*

        data (str): The data in string format.

        *Returns:*

        (str): The data in JSON formatted string.
        """
        try:
            codesys_client.__timed_logger(
                "Converting command data to JSON format.")
            data_split = data.split("|")
            json_dict = {}
            json_dict['command'] = data_split[0]
            try:
                json_dict['args'] = data_split[1:]
            except BaseException:
                json_dict['args'] = None
            return json.dumps(json_dict, indent=4)
        except BaseException:
            return data

    @staticmethod
    def __convert_from_json(json_data: str) -> str:
        """
        Try to convert given data from JSON into dictionary.

        *Arguments:*

        json_data (str): The data in JSON format.

        *Returns:*

        (str): The converted data or the original data.
        """
        try:
            conversion = json.loads(json_data)
            return conversion
        except BaseException:
            codesys_client.__timed_logger(
                "Data already in dictionary format, returning data as is.")
            return json_data

    def __command_error_handler(self, ret_data: str) -> bool:
        """
        Checks for errors in API return data. Returns True if the command should be retried.

        *Arguments:*

        ret_data (str): Returned data string from command.
        """
        if not ret_data:
            codesys_client.__timed_logger("No return data.")
            return False
        if "not logged in" in ret_data.lower():
            codesys_client.__timed_logger(
                "Device not logged in, even though it should be.\
                    Retrying command after relog.", loglevel="warn")
            self.login_to_onlineapp(True)
            return True
        if "Command failed" in ret_data:
            codesys_client.__timed_logger(
                "Failure found in return data.",
                loglevel="error")
            raise ValueError(f"{ret_data}")
        # Get errors and warnings (warnings not used.)
        if "Compile complete" in ret_data or "Build complete" in ret_data:
            errors, _ = map(int, re.findall("\\d+", ret_data))
            if errors > 0:
                raise ValueError(
                    f"Compile/Build was completed, but error count was: {errors}")
        for error in CODESYS_ERRORS:
            if error in ret_data:
                if error == "Login failed:":
                    if "Compile errors" in ret_data:
                        raise ValueError(
                            "Compiling the application has failed.")
                    if "No primary project loaded." in ret_data:
                        raise ValueError("There is no project open.")

                    self.scan_network()

                    if self.device_host:
                        self.set_address_from_ip(self.device_host)
                    if self.device_gateway:
                        self.set_gateway(self.device_gateway)
                    if self.device_host and self.device_gateway:
                        self.conf_device_gateway_and_address()

                    self.login_to_onlineapp(False)
                    return True

                if error in ('Network error:', 'No connection to the device. Please rescan your network.'):
                    time.sleep(1)
                    return True

                raise ValueError(ret_data)
        return False

    def change_api_connection_settings(self, host: str | None = None, port: int | None = None) -> None:
        """
        Changes the current host address/port settings.

        *Arguments:*

        host (str): The new host address for the API. Defaults to None (No change)
        port (int): The new host port for the API. Defaults to None (No change)
        """
        if host:
            codesys_client.__timed_logger(
                f"Changing host from {self.host} to {host}.")
            self.host = host
        if port:
            codesys_client.__timed_logger(
                f"Changing port from {self.port} to {port}.")
            self.port = int(port)

    def command(self, data: str, timeout: int | str = 60, retries: int = 5, error_handler=True) -> str:
        """
        Opens and connects to a socket. Sends the given data through the
        socket. Raises a ValueError, if return data has Failure.

        *Arguments:*

        data (str): Data to be sent through the socket.
        timeout (int|str): Timeout for command transfer.
        retries (int): Command retry count.
        error_handler (bool): Handle errors, default True

        *Returns:*

        (str): Returns the received data stripped.
        """
        if isinstance(timeout, str):
            timeout = int(timeout)
        initial_data = data
        data = self.__json_convert(data)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as api_connection:
            codesys_client.__timed_logger(
                f"Command timeout set to: {timeout}")
            api_connection.settimeout(timeout)
            try:
                codesys_client.__timed_logger(
                    f"Connecting to {self.host}:{self.port}.")
                api_connection.connect((self.host, int(self.port)))
                codesys_client.__timed_logger(
                    f"Sending\n{data}\nto socket.")
                api_connection.send(data.encode())
                codesys_client.__timed_logger("Waiting for response:")
                response = api_connection.recv(65536).decode()
                ret_json = self.__convert_from_json(response)
                try:
                    ret_data = ret_json['return']
                except BaseException:
                    ret_data = ret_json
                codesys_client.__timed_logger("--- RETURN FROM API ---")
                codesys_client.__timed_logger(f"\n{response}")
                if error_handler:
                    error = self.__command_error_handler(ret_data)
                else:
                    error = None
                if error:
                    if retries:
                        retries = retries - 1
                        return self.command(initial_data, timeout, retries)

                    raise ValueError(
                        "Max amount of retries achieved without succession.")
            except ConnectionRefusedError:
                codesys_client.__timed_logger(
                    "Server is not online.", "error")
                return ""
            except ConnectionResetError:
                if "shutdown_codesys" not in data:
                    codesys_client.__timed_logger(
                        "Server has gone offline for unknown reason.",
                        "error")
                codesys_client.__timed_logger("Server was closed.")
                return "Server was closed."
        return ret_data.strip()

    def restart_server(self) -> None:
        """
        Send restart server command for Codesys.
        """
        self.command("restart_server")

    def reset_api(self) -> None:
        """
        Reset data inside API.
        """
        self.command("reset_api")

    def get_api_commands(self) -> str:
        """
        Gets all the current api commands.

        *Returns:*

        (str): Return string containing all api commands.
        """
        ret = self.command("get_api_commands")
        ret = ret.split("|")
        commands = "\n".join(ret)
        codesys_client.__timed_logger(f"Commands:\n{commands}")
        return ret

    def get_api_command_help(self, command: str) -> str:
        """
        Get docstring for given API command.

        *Returns:*

        (str): Docstring for given API command.
        """
        ret = self.command(f"get_help_for_command|{command}")
        codesys_client.__timed_logger(f"Command help: \n\n{ret}\n\n")
        return ret

    def get_current_api_info(self) -> str:
        """
        Gets the information of the current API.

        *Returns:*

        (str): Information of API status.
        """
        ret = self.command("get_current_api_info")
        codesys_client.__timed_logger(
            f"\nCurrent API Info:\n\n{ret}")
        return ret

    def build_app(self) -> None:
        """
        Builds the current open application/project.
        """
        self.command("build")

    def clean_app(self, full: bool = False) -> None:
        """
        Cleans the current open application/project.

        *Arguments:*

        full (boolean): To indicate to clean full or not
        """
        self.command(f"clean|{full}")

    def generate_code(self) -> None:
        """
        Generates code for the current open application/project.
        """
        self.command("generate_code")

    def rebuild_app(self) -> None:
        """
        Rebuilds the current open application/project.
        """
        self.command("rebuild")

    def create_boot_application(self, filename: str, update_compile_info: bool = False, write_visu_files: bool = False) -> None:
        """
        Creates a boot application for the current open application/project.

        *Arguments:*

        filename (str): The filename to write the boot application to.
        update_compile_info (bool): Writes the compile information (compiler reference context) to the project directory.
        write_visu_files (bool): Write the visualization files into the output directory.
        """
        self.command(
            f"create_boot_application|{filename}|{update_compile_info}|{write_visu_files}")

    def get_system_messages(self) -> list:
        """
        Gets script message buffer from Codesys.

        *Returns:*

        (list): List of messages from Codesys.
        """
        messages = self.command("get_system_messages")
        messages = messages.split("|")
        return messages

    def get_message_categories(self, active: bool = True) -> list:
        """
        Gets all the message categories from Codesys.

        *Arguments:*

        active (bool): If active, only returns active categories. Otherwise returns all categories.

        *Returns:*

        (list): List of message categories from Codesys.
        """
        categories = self.command(f"get_message_categories|{active}")
        categories = categories.split("|")
        return categories

    def get_message_objects(self, category: str | None = None) -> list:
        """
        Gets all the messages from a given category and with given
        severities.

        *Arguments:*

        category (str): Category to return messages from, if None returns all categories.
        severities (int): The severities. By default, all severities are returned.
        """
        messages = self.command(f"get_message_objects|{category}")
        messages = messages.split("|")
        return messages

    def save_project(self) -> None:
        """
        Save the current open project.
        """
        self.command("save_project")

    def close_project(self) -> None:
        """
        Close the current open project.
        """
        self.command("close_project")

    def get_device(self, device: str) -> None:
        """
        Gets and sets the current device from the open project.

        *Arguments:*

        (str): The device name in the current project.
        """
        self.command(f"get_device|{device}")

    def update_device(self, device: str, version: str) -> None:
        """
        Update given device with given device description version.

        *Arguments:*

        device (str): The device name in the current project.
        version (str): The device description version. Has to exist.
        """
        self.command(f"update_device|{device}|{version}")

    def install_device_description(self, description: str) -> None:
        """
        Send the add device description command to the socket.

        *Arguments:*

        description (str): Path to the description file.
        """
        self.command(f"add_device_description|{description}")

    def uninstall_device_description(self, device_name: str, source: str | None = None) -> None:
        """
        Send the remove device description command to the socket.

        *Arguments:*

        device_name (str): Name of the device description to be removed.
        source (str): Repository to remove the description from.
        """
        self.command(f"remove_device_description|{device_name}|{source}")

    def full_config(self,
                    project: str | None = None,
                    dev_name: str | None = None,
                    version: str | None = None,
                    gateway: str | None = None,
                    ip: str | None = None,
                    timeout: int = 60) -> None:
        """
        Reads dev_name, ip, version and gateway from the config file.
        Also takes the project as a variable. Sends the full_config command to the API socket server.

        *Arguments:*

        project (str): Full path to the project to be opened in Codesys.
        """
        if not dev_name:
            dev_name = self.config.get('device_config', 'proj_device_name')
        if not version:
            version = self.config.get('device_config', 'device_version')
        if not gateway:
            gateway = self.config.get('device_config', 'gateway')
        if not ip:
            ip = self.config.get('device_config', 'ip')
        self.device_host = ip
        self.device_gateway = gateway
        self.command(
            f"full_config|{project}|{dev_name}|{version}|{gateway}|{ip}", timeout)

    def create_project(self, path: str, primary: bool = True) -> None:
        """
        Sends the create project command to the API server, which creates a new empty project.

        *Arguments:*

        path: Path to the project
        primary: Set project to primary
        """
        self.command(f"create_project|{path}|{primary}")

    def open_project(self, project: str) -> None:
        """
        Sends the open command to the API server.

        *Arguments:*

        project (str): Full path to the project to be opened in Codesys.
        """
        self.command(f"open_project|{project}", 60, error_handler=True)

    def import_native(self, filenames: str | None = None, _filter: str |
                      None = None, handler: str | None = None) -> None:
        """
        Sends the import native command to the API server, which imports native CODESYS file to current project.

        *Arguments:*

        filenames (str): Path to the files that should be imported.
        _filter (str): Filter for the importation.
        handler (obj): Not supported, should be left as None.
        """
        self.command(f"import_native|{filenames}|{_filter}|{handler}")

    def export_native(
            self,
            objects: str | None = None,
            destination: str | None = None,
            recursive: bool = False,
            one_file_per_subtree: bool = False,
            profile_name: bool = False,
            reporter: str | None = None) -> None:
        """
        Sends the export native command that exports native CODESYS file from the current project.

        *Arguments:*

        objects (str): Not yet supported. Function exports everything inside the current project.
        destination (str): Path to save the export to.
        recursive (bool): If everything is exported recursively. Should be set to True, if everything needs to be exported.
        one_file_per_subtree (bool): If set to true all objects will be saved to separate files.
        profile_name (str): This is not supported and does not work for some reason (Codesys side problem)
        reporter (obj): This is not yet supported to be used. None is enough for exporting.
        """
        self.command(f"export_native|{objects}|{destination}|{recursive}|"
                     f"{one_file_per_subtree}|{profile_name}|{reporter}")

    def import_xml(self, path: str, reporter: str | None = None,
                   import_folder_structure: bool = False) -> None:
        """
        Sends the import xml command to the API server, which imports an XML file from the current project.

        *Arguments:*

        path (str): Path to the XML file.
        reporter (obj): This is not yet supported to be used. None is enough for exporting.
        import_folder_structure (bool): If set to True will import the whole folder structure.
        """
        self.command(f"import_xml|{path}|{reporter}|{import_folder_structure}")

    def export_xml(
            self,
            objects: str | None = None,
            reporter: str | None = None,
            path: str | None = None,
            recursive: bool = False,
            export_folder_structure: bool = False,
            declarations_as_plaintext: bool = False) -> None:
        """
        Sends the export xml command to the API server, which exports the current project as an xml file.

        *Arguments:*

        objects (tuple): Not yet supported.
        reporter (ExportReporter): Not yet supported.
        path (str): Path where the exported file will be saved.
        recursive (bool): If all children of the given object should be exported. \
        This should be set to True (Because everything will be exported.)
        export_folder_structure (bool): If set to True, the folder structure of the objects is also exported. \
        This is a proprietary extension to the default schema.
        declarations_as_plaintext (bool): If set to true, the declaration parts will be additionally exported as plain text \
        (which is lossless in contrast to the default schema).
        This is a proprietary extension to the default schema. \
        (Import will automatically recognize and prefer the plain text format if present)
        """
        self.command(f"export_xml|{objects}|{reporter}|{path}|{recursive}|"
                     f"{export_folder_structure}|{declarations_as_plaintext}")

    def __parse_datatypes(self, value: str, ret_type: str | None):
        """Removes datatype from return value, for example BYTE#, INT#, etc.
        Additionally can convert return value into int/float/bin/hex/bool

        *Arguments:*

        data (str): Initial data string.
        ret_type (str): Changes the return type based on given.

        *Returns:*

        (str): Parsed data.
        """
        pattern = r'^\w+#'
        value = re.sub(pattern, '', value)
        if not ret_type:
            return value
        elif ret_type in ["bin", "hex", "int", "float"]:
            value = int(value)
            value = RET_TYPES[ret_type](value)
        elif ret_type == "bool":
            if value.isnumeric():
                value = int(value)
            else:
                value = value.replace("TRUE", "True")
                value = value.replace("FALSE", "False")
            value = RET_TYPES[ret_type](value)
        return value

    def read_value(self, value: str, check_running_app: bool = True, ret_type: str | None = None) -> str:
        """Sends the read command to the socket API server and waits for the return value.

        *Arguments:*

        value (str): The parameter to be read.
        check_running_app (bool): Check that application is running before writing.
        ret_type (str): bin/hex/int/float/bool

        *Returns:*

        (str): Returns the read value from Codesys.
        """
        ret = self.command(f"read|{value}|{check_running_app}")
        return self.__parse_datatypes(ret, ret_type)

    def write_value(
            self,
            param: str,
            value: str,
            force: bool = False,
            check: bool = True,
            check_running_app: bool = True) -> None:
        """Sends the write command to the socket API server.

        *Arguments:*

        param (str): The parameter to be written in.
        value (str): The value to be written to the parameter.
        force (str): Force values.
        """
        self.command(
            f"write|{param}|{value}|{force}|{check}|{check_running_app}")

    def shutdown_codesys(self) -> None:
        """
        Sends the shutdown command to the socket.
        """
        self.command("shutdown_codesys")

    def shutdown_server(self) -> None:
        """
        Sends the shutdown command to the socket.
        """
        self.command("shutdown_server")

    def health_check(self, tries: int = 10, timeout: int = 1) -> None:
        """
        Sends health check command to socket and awaits answer.
        Raises ValueError if no answer is received.

        *Arguments:*

        tries (int): Number of retries
        timeout (int): Timeout to wait answer
        """
        res = None
        for i in range(tries):
            try:
                res = self.command("health", timeout, 1)
            except TimeoutError:
                codesys_client.__timed_logger(
                    "Health check timed out, trying again.", "Warn")
                continue

            if res:
                break

            codesys_client.__timed_logger(
                f"Health check failed, trying again for\
                    a maximum of {i+1}/{tries} tries.", "error")
            time.sleep(1)
        if not res:
            raise ValueError("Health check not successful after 10 tries.")

    def scan_network(self, tries: int = 10) -> str:
        """Sends the network scan command to the socket.

        *Arguments:*

        tries: Number of tries

        """
        for i in range(tries):
            try:
                return self.command("scan")
            except BaseException:
                codesys_client.__timed_logger(
                    f"Scan failed, trying again for a maximum of {i + 1}/{tries} tries.")
                time.sleep(1)
        raise ValueError("Scan failed maximum amount of times.")

    def create_gateway(
            self,
            gateway: str,
            address: str,
            port: str,
            driver: str | None = None,
            guid: str | None = None) -> None:
        """
        Creates the given gateway with the given address.

        *Arguments:*

        gateway (str): Gateway name.
        address (str): Address for gateway.
        port (str): Port for gateway.
        driver (str): Driver for gateway, default is TCP/IP if None given.
        guid (str): Id for gateway, new will be generated if None given.
        """
        command_str = f"create_gateway|{gateway}|{address}|{port}|{driver}|{guid}"
        self.command(command_str)

    def remove_gateway(self, gateway: str) -> None:
        """
        Removes the given gateway if it exists.

        *Arguments:*

        gateway (str): The name of the gateway to be removed.
        """
        self.command(f"remove_gateway|{gateway}")

    def set_gateway(self, gateway: str) -> None:
        """
        Sends the set gateway command to the socket with the given gateway argument.

        *Arguments:*

        gateway (str): The name of the gateway to be set.
        """
        self.device_gateway = gateway
        self.command(f"set_gateway|{gateway}")

    def get_gateways(self) -> list:
        """
        Sends the get gateways command.

        *Returns:*

        (list): Returns a list of all created gateways.
        """
        ret = self.command("get_gateways")
        return ret.split("|")

    def download_file(self, local_file: str, remote_file: str,
                      overwrite: bool) -> None:
        """
        Send the file download command to socket.

        *Arguments:*

        local_file (str): Path of the local file.
        remote_file (str): Path of the remote file.
        overwrite (bool): Force the overwrite if remote file already exists.
        """
        self.command(f"download_file|{local_file}|{remote_file}|{overwrite}")

    def upload_file(self, remote_file: str, local_file: str,
                    overwrite: bool) -> None:
        """
        Send the file upload command to socket.

        *Arguments:*

        remote_file (str): Path of the remote file.
        local_file (str): Path of the local file.
        overwrite (bool): Force the overwrite if the local file already exists.
        """
        self.command(f"upload_file|{remote_file}|{local_file}|{overwrite}")

    def rename_file(self, old_name: str, new_name: str) -> None:
        """
        Send the file rename command to the socket.

        *Arguments:*

        old_name (str): Path of the remote file with the old name.
        new_name (str): Path of the remote file with the old name.
        """
        self.command(f"rename_file|{old_name}|{new_name}")

    def delete_file(self, remote_file: str) -> None:
        """
        Send the file delete command to the socket.

        *Arguments:*

        remote_file (str): Remote path to the file.
        """
        self.command(f"delete_file|{remote_file}")

    def rename_directory(self, old_name: str, new_name: str) -> None:
        """
        Send the directory rename command to the socket.

        *Arguments:*

        old_name (str): Path of the remote directory with the old name.
        new_name (str): Path of the remote directory with the new name.
        """
        self.command(f"rename_directory|{old_name}|{new_name}")

    def delete_directory(self, remote_directory: str, recursive: bool) -> None:
        """
        Send the directory delete command to the socket.

        *Arguments:*

        remote_directory (str): Path of the remote directory.
        recursive (bool): If True, delete directory recursively.
        """
        self.command(f"delete_directory|{remote_directory}|{recursive}")

    def create_directory(self, remote_directory: str) -> None:
        """
        Send the directory create command to the socket.

        *Arguments:*

        remote_directory (str): Path to the new directory.
        """
        self.command(f"create_directory|{remote_directory}")

    def get_file_list(self, remote_directory: str) -> None:
        """
        Send the get file list of directory command to socket.

        *Arguments:*

        remote_directory (str): Path of the directory.
        """
        self.command(f"get_file_list|{remote_directory}")

    def set_address_from_ip(self, ip: str, tries: int = 10) -> None:
        """
        Sends the set ip command to the socket with the given IP.

        *Arguments:*

        ip (str): The IP address to set the device with.
        tries (int): Number of tries
        """
        self.device_host = ip
        for i in range(tries):
            try:
                self.command(f"set_ip|{ip}")
                return
            except BaseException:
                codesys_client.__timed_logger(
                    f"Setting IP/Scan, trying again for a maximum of {i + 1}/{tries} tries.")
                time.sleep(1)
        raise ValueError("Setting IP/Scan failed maximum amount of times.")

    def set_address_from_scan(self, _id: str) -> None:
        """
        Sends the set address command to the socket with the given id argument.

        *Arguments:*

        _id (str): The index of the address in the scan result.
        """
        self.command(f"set_address|{_id}")

    def conf_device_gateway_and_address(self) -> None:
        """
        Sends the configuration command for gateway and address in device to the socket.
        """
        self.command("conf_device_gateway_and_address")

    def get_installed_libraries(self, _filter: str | None = None) -> tuple:
        """
        Gets all the installed libraries from CODESYS library manager.

        *Arguments:*

        _filter (str): The filter for libraries

        *Returns:*

        (tuple): Returns two list items, the used library names and versions.
        """
        libs = self.command(f"get_installed_libraries|{_filter}")
        used_libs = []
        lib_versions = []
        for lib in libs.split("|"):
            # Uses regex to find library name, version and vendor.
            m = re.findall('([^,]+), ([^(]+) \\(([^)]+)\\)', lib)
            if len(m) > 0:
                libname, libversion, _ = m[0]
                used_libs.append(libname)
                lib_versions.append(libversion)
        return used_libs, lib_versions

    def install_library(
            self,
            library_path: str,
            timeout: int | str = 30) -> None:
        """
        Sends the install library command to the socket with the given library path argument.

        *Arguments:*

        library_path (str): Full path to the library to be installed.
        timeout (int): timeout to wait installation
        """
        self.command(
            f"install_library|{library_path}",
            timeout=timeout)

    def install_libraries(
            self,
            library_paths: list | str,
            ignore: str | None = None,
            timeout: int | str = 30) -> None:
        """
        Sends the install library command to the socket with the given library paths.

        *Arguments:*

        library_paths (list): List to paths of libraries.
        ignore (str): Libraries to ignore, separated by '|'
        timeout (int): Timeout to wait installation
        """
        if ignore:
            ignore = ignore.split("|")
        ignored = False
        cmd_str = "install_library"
        if not library_paths:
            return "Success"

        if not isinstance(library_paths, list):
            library_paths = [library_paths]

        for library in library_paths:
            if ignore:
                for ignored_library in ignore:
                    if ignored_library in library:
                        ignored = True
                        break

                    ignored = False
            if len(cmd_str) >= 8000:
                self.command(cmd_str)
                cmd_str = "install_library"

            if not ignored:
                codesys_client.__timed_logger(
                    f"Library to be installed: {library.strip()}")
                cmd_str += f"|{library.strip()}"

        self.command(cmd_str, timeout=timeout)

    def uninstall_library(
            self,
            library_name: str,
            timeout: int | str = 30) -> None:
        """
        Sends the uninstall library command to the socket with the given library name.

        *Arguments:*

        library_name (str): Full library name.
        timeout (int): timeout to wait uninstallation
        """
        self.command(
            f"uninstall_library|{library_name}",
            timeout=timeout)

    def uninstall_libraries(
            self,
            library_list: list,
            timeout: int | str = 30) -> None:
        """
        Sends the uninstall library command to the socket with the given library name list.

        *Arguments:*

        library_list (list): List of full library names.
        timeout (int): timeout to wait uninstallation
        """
        cmd_str = "uninstall_library"
        for library in library_list:
            cmd_str += f"|{library.strip()}"
        self.command(cmd_str, timeout=timeout)

    def get_library_version(self, lib_name: str) -> str:
        """
        Sends the get library command to the socket with the given library name.

        *Arguments:*

        lib_name (str): Name of the libraries to be searched.
        """
        return self.command(f"get_library|{lib_name}")

    def logout_from_onlineapp(self) -> None:
        """
        Sends the logout command to the socket.
        """
        self.command("logout")

    def login_to_onlineapp(self, error_handler: bool = True) -> None:
        """
        Sends the login command to the socket.

        *Arguments:*

        error_handler (boolean): To handle errors
        """
        total_tries = 0
        for i in range(10):
            try:
                self.command("login", 30, 1, error_handler)
                break
            except ValueError:
                total_tries = -1
                break
            except Exception:
                time.sleep(1)
                total_tries = i
        if total_tries >= 9:
            raise ValueError("Login failed after maximum tries.")
        if total_tries == -1:
            raise ValueError("Login failed.")

    def warm_reset(self) -> None:
        """
        Sends the warm reset command to the socket.
        """
        self.command("warm_reset")

    def cold_reset(self) -> None:
        """
        Sends the warm reset command to the socket.
        """
        self.command("cold_reset")

    def original_reset(self) -> None:
        """
        Sends the warm reset command to the socket.
        """
        self.command("origin_reset")

    def start_app(self) -> None:
        """
        Sends the start app command to the socket.
        """
        self.command("start_app")

    def stop_app(self) -> None:
        """
        Sends the stop app command to the socket.
        """
        self.command("stop_app")

    def find_used_libraries(
            self,
            _filter: str | None = None,
            split_versions: bool = False) -> str | tuple:
        """
        Finds used libraries from the current open project.

        *Arguments:*

        _filter (str/None): Filter for libraries.
        split_versions (bool): Boolean to split to names/versions.

        *Returns:*

        (tuple/str): Returns used libraries either splitted into
        names and versions or one full string containing all info.
        """
        ret = self.command(f"used_libraries|{_filter}")
        if ret:
            if split_versions:
                used_libs = []
                lib_versions = []
                for lib in ret.split("|"):
                    # Uses regex to find library name, version and vendor.
                    m = re.findall('([^,]+), ([^(]+) \\(([^)]+)\\)', lib)
                    if len(m) > 0:
                        libname, libversion, _ = m[0]
                    used_libs.append(libname)
                    lib_versions.append(libversion)
                return used_libs, lib_versions

            return ret.split("|")
        if split_versions:
            return "", ""
        return ""

    def find_missing_libraries(self, _filter: str = "epec") -> tuple:
        """
        Finds missing libraries from the current open project.

        *Arguments:*
        _filter (str): Filters the libraries with given name.

        *Returns:*

        (tuple): Tuple containing all missing library names and versions.
        """
        libs = self.command("missing_libraries")
        if not libs:
            return [], []
        missing_libs = []
        lib_versions = []
        for lib in libs.split("|"):
            # Uses regex to find library name, version and vendor.
            m = re.findall('([^,]+), ([^(]+) \\(([^)]+)\\)', lib)
            if len(m) > 0:
                libname, libversion, libvendor = m[0]
                if _filter not in libvendor.lower():
                    continue
                missing_libs.append(libname)
                lib_versions.append(libversion)
        return missing_libs, lib_versions

    def set_default_credentials(self, username: str, password: str) -> str:
        """
        Sends the set default credentials command.

        *Arguments:*

        username (str): Username
        password (str): Password
        """
        return self.command(f"set_default_credentials|{username}|{password}")

    def download_missing_libs(self) -> str:
        """
        Tries to download all missing CODESYS libraries and install them.
        """
        return self.command("download_missing_libs", 300)

    def change_task_cyclic_interval(self, task_name: str, interval: str) -> str:
        """
        Change given task cyclic interval.

        NOT POSSIBLE WHEN DEVICE IS ONLINE

        *Arguments:*

        task_name (str): Name of the task under task configuration, for example MainTask.
        interval (str): Interval for task, for example 10 (ms)
        """
        return self.command(f"change_task_cyclic_interval|{task_name}|{interval}")
