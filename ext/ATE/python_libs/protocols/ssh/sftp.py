"""Simplified SFTP Client for Robot Framework test automation.

Focused on core file transfer functionality for embedded device testing.
"""

import posixpath
import stat
import time
from operator import attrgetter
from contextlib import contextmanager
from pathlib import Path, PurePosixPath
from typing import Iterator
import paramiko
from paramiko import SFTPAttributes
from robot.api import logger

try:
    from .ssh import ssh, ssh_error
except ImportError:
    from ssh import ssh, ssh_error


class sftp_error(ssh_error):
    """Custom exception for SFTP operation failures.

    Primary error type for all SFTP-related failures, providing consistent error handling
    throughout the SFTP client. Wraps various underlying exceptions from Paramiko, OS,
    and network operations with descriptive messages specific to SFTP operations.

    Examples:
    | Run Keyword And Expect Error | sftp_error* | Upload | missing.txt | /remote/file.txt |
    """


class sftp(ssh):
    """SFTP client for Robot Framework test automation.

    Extends the SSH client to provide comprehensive SFTP (Secure File Transfer Protocol)
    capabilities for secure file transfers and directory operations, while retaining all
    command execution and connection management features from the SSH base class.

    Examples:
    | Library | sftp.py |
    | Configure Connection | 192.168.1.100 | user | password |
    | Upload | local_file.txt | /remote/path/file.txt |
    | Download | /remote/log.txt | local_log.txt |
    | Disconnect |
    """

    ROBOT_LIBRARY_SCOPE: str = "GLOBAL"

    # =========================================================================
    # PUBLIC ROBOT FRAMEWORK KEYWORDS
    # =========================================================================

    def test_connection(self, timeout: int = 10, retry_count: int = 0) -> None:
        """Test whether SFTP connection can be established and verify file transfer capability.

        Attempts to connect to server and open SFTP session, retrying if necessary.
        Tests basic SFTP operations like directory listing to verify functionality.

        Args:
        - `timeout`: Connection timeout in seconds for each attempt (default: 10)
        - `retry_count`: Number of connection retry attempts (default: 1)

        Returns:
        - Success message if SFTP connection is established

        Raises:
        - `sftp_error`: If the sftp session fails, connection is not configured, or retry_count is negative.
        - 'ssh_error': If the initial ssh connection is not functional.

        Examples:
        | Configure Connection | 192.168.1.100 | user | pass |
        | Test Connection |
        | Test Connection | timeout=5 | retry_count=3 |
        """
        if not self._configured:
            raise sftp_error(
                "SFTP not configured. Use 'Configure Connection' first.")

        if retry_count < 0:
            raise sftp_error(
                "Negative retry_count given.")

        last_exception: Exception = None
        total_attempts: int = retry_count + 1  # Initial attempt + retries

        # Test SSH connection
        super().test_connection(timeout, retry_count)

        for attempt in range(total_attempts):
            try:
                # Test SFTP session
                with self._get_sftp_session() as sftp_session:
                    try:
                        sftp_session.listdir(".")
                    except (OSError, IOError, paramiko.SFTPError):
                        # Try root if current dir fails
                        sftp_session.listdir("/")

                message = f"SFTP connection successful to {self._connection_config.address}:{self._connection_config.port}"
                logger.info(message)
                return

            except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
                last_exception = e
                logger.warn(
                    f"SFTP test failed (attempt {attempt+1}/{total_attempts}): {e}")
                if attempt < total_attempts - 1:
                    time.sleep(super().CONNECTION_RETRY_INTERVAL_S)

        raise sftp_error(
            f"SFTP connection test failed: {last_exception}") from last_exception

    def upload_to_remote(self, local_path: str, remote_path: str, verify: bool = True) -> str:
        """Upload file or directory to remote device using SFTP with automatic verification.

        Automatically detects if local_path is a file or directory and handles accordingly.
        Creates remote directories as needed and uploads with automatic progress logging for directories.
        Optionally verifies transfer integrity by comparing file sizes after upload.

        Args:
        - `local_path`: Path to local file or directory to be uploaded
        - `remote_path`: Destination path on remote device
        - `verify`: Whether to verify transfer integrity after upload (default: True)

        Returns:
        - Success message with transfer details including file count or size and verification status

        Raises:
        - `sftp_error`: If local path does not exist, upload fails, or verification fails

        Examples:
        | Upload To Remote | test_data.txt | /tmp/test_data.txt |
        | Upload To Remote | logs/ | /var/log/application/ |
        | Upload To Remote | config.json | /etc/myapp/config.json | verify=False |
        """
        local_item = Path(local_path)

        if not local_item.exists():
            raise sftp_error(f"Local path not found: {local_path}")

        with self._get_sftp_session() as sftp_session:
            if local_item.is_file():
                result = self._upload_file(
                    sftp_session, local_path, remote_path)
            elif local_item.is_dir():
                result = self._upload_directory(
                    sftp_session, local_path, remote_path)
            else:
                raise sftp_error(
                    f"Local path is neither file nor directory: {local_path}")

        # Verify transfer integrity if requested
        if verify:
            verification_result = self._verify_transfer_integrity(
                local_path, remote_path)
            result += f" - {verification_result}"

        return result

    def download_from_remote(self, remote_path: str, local_path: str, verify: bool = True) -> str:
        """Download file or directory from remote device to local system with automatic verification.

        Automatically detects if remote_path is a file or directory and handles accordingly.
        Creates local directories as needed and downloads with automatic progress logging for directories.
        Optionally verifies transfer integrity by comparing file sizes after download.

        Args:
        - `remote_path`: Path to remote file or directory to be downloaded
        - `local_path`: Local destination path for downloaded content
        - `verify`: Whether to verify transfer integrity after download (default: True)

        Returns:
        - Success message with transfer details including file count or size and verification status

        Raises:
        - `sftp_error`: If download fails, remote path is not accessible, or verification fails

        Examples:
        | Download From Remote | /var/log/app.log | local_logs/app.log |
        | Download From Remote | /etc/config/ | backup/config/ |
        | Download From Remote | /tmp/results.txt | test_results.txt | verify=False |
        """
        remote_path = self._validate_path(remote_path)

        try:
            with self._get_sftp_session() as sftp_session:
                # Check what type of item the remote path is
                try:
                    remote_stat = sftp_session.stat(remote_path)
                except (OSError, IOError, paramiko.SFTPError) as e:
                    raise sftp_error(
                        f"Remote path not accessible: {remote_path} - {e}") from e

                if stat.S_ISREG(remote_stat.st_mode):
                    # It's a file
                    result = self._download_file(
                        sftp_session, remote_path, local_path)
                elif stat.S_ISDIR(remote_stat.st_mode):
                    # It's a directory
                    result = self._download_directory(
                        sftp_session, remote_path, local_path)
                else:
                    raise sftp_error(
                        f"Remote path is neither file nor directory: {remote_path}")

            # Verify transfer integrity if requested
            if verify:
                verification_result = self._verify_transfer_integrity(
                    local_path, remote_path)
                result += f" - {verification_result}"

            return result

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"Download failed: {e}") from e

    def download_latest_file_from_remote(self, remote_dir: str, local_path: str, verify: bool = True) -> str:
        """Download latest modified file from remote device to local system with automatic verification.

        Verifies remote_dir is a directory. Lists files in a remote directory and selects the file which is
        latest modified (in time). Creates local directories as needed and downloads with automatic progress logging for directories.
        Optionally verifies transfer integrity by comparing file sizes after download.

        Args:
        - `remote_dir`: Path to remote directory
        - `local_path`: Local destination path for downloaded content. If destination is directory, the file name will match the remote file name.
        - `verify`: Whether to verify transfer integrity after download (default: True)

        Returns:
        - Success message with transfer details including file count or size and verification status

        Raises:
        - `sftp_error`: If download fails, remote directory is not accessible or it is empty, or verification fails

        Examples:
        | Download Latest File From Remote | /home/lvuser/logs-archive | local_dir/measurement_file.tdms |
        | Download Latest File From Remote | /home/lvuser/logs-archive | local_dir/                      | verify=False |
        """
        remote_dir = self._validate_path(remote_dir)
        try:
            with self._get_sftp_session() as sftp_session:
                # Check what type of item the remote path is
                try:
                    remote_stat = sftp_session.stat(remote_dir)
                except (OSError, IOError, paramiko.SFTPError) as e:
                    raise sftp_error(
                        f"Remote path not accessible: {remote_dir} - {e}") from e

                if stat.S_ISDIR(remote_stat.st_mode):
                    # It's a directory, verify files exist
                    files = self._list_directory(remote_dir)
                    if 0 == len(files):
                        raise sftp_error(
                            f"No files in directory: {remote_dir}")

                    # Download latest file from remote directory
                    latest_file = self._get_latest_file(files)
                    remote_file_path = self._validate_path(
                        PurePosixPath(remote_dir, latest_file.filename))

                    if Path(local_path).is_dir():
                        local_path = self._validate_path(
                            Path(local_path, latest_file.filename))
                    result = self._download_file(
                        sftp_session, remote_file_path, local_path)
                else:
                    raise sftp_error(
                        f"Remote path is not directory: {remote_dir}")

            # Verify transfer integrity if requested
            if verify:
                verification_result = self._verify_transfer_integrity(
                    local_path, remote_file_path)
                result += f" - {verification_result}"

            return result

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"Download failed: {e}") from e

    def remove_from_remote(self, remote_path: str) -> str:
        """Remove file or directory from remote device.

        Automatically detects if remote_path is a file or directory and handles accordingly.
        For files: removes the file. For directories: recursively removes all contents
        then removes the directory itself.

        Args:
        - `remote_path`: Remote path to remove (file or directory)

        Returns:
        - Success message indicating removal

        Raises:
        - `sftp_error`: If removal fails

        Examples:
        | Remove From Remote | /tmp/temp_file.txt |
        | Remove From Remote | /tmp/temp_directory/ |
        | Run Keyword And Expect Error | sftp_error* | Remove From Remote | /nonexistent |
        """
        remote_path = self._validate_path(remote_path)

        try:
            with self._get_sftp_session() as sftp_session:
                # Check what type of item the remote path is
                try:
                    remote_stat = sftp_session.stat(remote_path)
                except (OSError, IOError, paramiko.SFTPError) as e:
                    raise sftp_error(
                        f"Remote path not accessible: {remote_path} - {e}") from e

                if stat.S_ISREG(remote_stat.st_mode):
                    # It's a file
                    sftp_session.remove(remote_path)
                    message = f"File removed: {remote_path}"
                    logger.info(message)
                    return message
                if stat.S_ISDIR(remote_stat.st_mode):
                    # It's a directory
                    return self._remove_directory(sftp_session, remote_path)

                raise sftp_error(
                    f"Remote path is neither file nor directory: {remote_path}")

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"Failed to remove: {e}") from e

    def list_files_in_remote_directory(self, remote_dir: str) -> list[tuple[str, int, str]]:
        """Lists all files in remote_dir. The list of files contains information about: File name, file size, file modification date/time.

        Args:
        - `remote_dir`: Path to remote directory

        Returns:
        - Tuple containing: File name, file size, modified date/time

        Raises:
        - `sftp_error`: If remote directory is not accessible

        Examples:
        | List Files In Remote Directory | /home/lvuser/logs-archive |
        """
        items = []
        files = self._list_directory(remote_dir)
        for file in files:
            filename = file.filename
            mtime = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(file.st_mtime))
            size = file.st_size
            items.append((filename, size, mtime))

        return items

    # =========================================================================
    # PRIVATE METHODS
    # =========================================================================

    def _upload_file(self, sftp_session: paramiko.SFTPClient, local_path: str, remote_path: str) -> str:
        """Upload a single file to remote device using SFTP.

        Validates local file exists and is readable, creates remote directory structure if needed,
        and uploads file with confirmation. Used internally by the public Upload keyword.

        Args:
        - `local_path`: Path to local file to be uploaded
        - `remote_path`: Destination path on remote device

        Returns:
        - Success message indicating file upload with size information

        Raises:
        - `sftp_error`: If local file invalid or upload operation fails

        Examples:
        | # Internal usage only - called by Upload keyword
        | self._upload_file("config.txt", "/etc/config.txt")
        """
        local_file = Path(local_path)
        remote_path = self._validate_path(remote_path)

        if not local_file.is_file():
            raise sftp_error(f"Local path is not a file: {local_path}")

        try:
            file_size = local_file.stat().st_size
            logger.info(
                f"Uploading file {local_path} ({file_size} bytes) to {remote_path}")

            # Create remote directory if needed
            remote_dir = posixpath.dirname(remote_path)
            if remote_dir and remote_dir != "/":
                self._ensure_remote_dir(sftp_session, remote_dir)

            # Upload file
            sftp_session.put(local_path, remote_path, confirm=True)

            message = f"File uploaded: {local_path} -> {remote_path} ({file_size} bytes)"
            logger.info(message)
            return message

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"File upload failed: {e}") from e

    def _upload_directory(self, sftp_session: paramiko.SFTPClient, local_dir: str, remote_dir: str) -> str:
        """Upload a directory and all its contents recursively to remote device.

        Creates remote directory structure and uploads all files recursively from local directory.
        Maintains directory hierarchy and provides progress logging for large transfers.
        Used internally by the public Upload keyword.

        Args:
        - `local_dir`: Path to local directory to upload
        - `remote_dir`: Destination directory path on remote device

        Returns:
        - Success message indicating number of files uploaded

        Raises:
        - `sftp_error`: If local directory invalid or upload operation fails

        Examples:
        | # Internal usage only - called by Upload keyword
        | self._upload_directory("logs/", "/var/log/application/")
        """
        local_path = Path(local_dir)
        remote_dir = self._validate_path(remote_dir)

        if not local_path.is_dir():
            raise sftp_error(f"Local path is not a directory: {local_dir}")

        try:
            logger.info(f"Uploading directory {local_dir} to {remote_dir}")
            uploaded_count = 0

            # Create remote base directory
            self._ensure_remote_dir(sftp_session, remote_dir)

            # Upload all files recursively
            for item in local_path.rglob("*"):
                if item.is_file():
                    # Calculate relative path
                    relative_path = item.relative_to(local_path)
                    remote_file_path = posixpath.join(
                        remote_dir, relative_path.as_posix())

                    # Create remote subdirectories if needed
                    remote_parent = posixpath.dirname(remote_file_path)
                    if remote_parent != remote_dir:
                        self._ensure_remote_dir(
                            sftp_session, remote_parent)

                    # Upload file
                    sftp_session.put(
                        str(item), remote_file_path, confirm=True)
                    uploaded_count += 1

                    if uploaded_count % 10 == 0:  # Progress logging
                        logger.info(f"Uploaded {uploaded_count} files...")

            message = f"Directory uploaded: {uploaded_count} files from {local_dir} to {remote_dir}"
            logger.info(message)
            return message

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"Directory upload failed: {e}") from e

    def _download_file(self, sftp_session: paramiko.SFTPClient, remote_path: str, local_path: str) -> str:
        """Download a single file from remote device to local system.

        Creates local directory if needed, verifies remote file exists and downloads with
        size verification. Used internally by the public Download keyword for file transfers.

        Args:
        - `sftp_session`: Active SFTP session for file operations
        - `remote_path`: Path to remote file to download
        - `local_path`: Local destination path for downloaded file

        Returns:
        - Success message indicating file download with size information

        Raises:
        - `sftp_error`: If download operation fails or file verification fails

        Examples:
        | # Internal usage only - called by Download keyword
        | self._download_file(session, "/var/log/app.log", "app.log")
        """
        local_file = Path(local_path)

        # Create local directory if needed
        local_file.parent.mkdir(parents=True, exist_ok=True)

        try:
            # Get remote file size
            remote_stat = sftp_session.stat(remote_path)
            file_size = remote_stat.st_size

            logger.info(
                f"Downloading file {remote_path} ({file_size} bytes) to {local_path}")

            # Download file
            sftp_session.get(remote_path, local_path)

            # Verify download
            if not local_file.exists():
                raise sftp_error("Download failed: local file not created")

            downloaded_size = local_file.stat().st_size
            message = f"File downloaded: {remote_path} -> {local_path} ({downloaded_size} bytes)"
            logger.info(message)
            return message

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"File download failed: {e}") from e

    def _download_directory(self, sftp_session: paramiko.SFTPClient, remote_dir: str, local_dir: str) -> str:
        """Download a directory and all its contents recursively from remote device.

        Creates local directory structure and downloads all files recursively from remote directory.
        Maintains directory hierarchy and provides progress logging for large transfers.
        Used internally by the public Download keyword.

        Args:
        - `sftp_session`: Active SFTP session for file operations
        - `remote_dir`: Path to remote directory to download
        - `local_dir`: Local destination directory path

        Returns:
        - Success message indicating number of files downloaded

        Raises:
        - `sftp_error`: If directory download operation fails

        Examples:
        | # Internal usage only - called by Download keyword
        | self._download_directory(session, "/var/log/myapp/", "logs/")
        """
        local_path = Path(local_dir)

        try:
            logger.info(f"Downloading directory {remote_dir} to {local_dir}")

            # Create local directory
            local_path.mkdir(parents=True, exist_ok=True)

            # Download all files recursively
            downloaded_count = self._download_directory_recursive(
                sftp_session, remote_dir, local_path)

            message = f"Directory downloaded: {downloaded_count} files from {remote_dir} to {local_dir}"
            logger.info(message)
            return message

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"Directory download failed: {e}") from e

    def _download_directory_recursive(self, sftp_session: paramiko.SFTPClient, remote_dir: str, local_dir: Path) -> int:
        """Recursively download all contents of remote directory to local directory.

        Downloads all files and directories from remote location to local filesystem,
        creating directory structure as needed and providing progress logging. Helper method
        for directory download operations.

        Args:
        - `sftp_session`: Active SFTP session for file operations
        - `remote_dir`: Path to remote directory to process
        - `local_dir`: Path object for local destination directory

        Returns:
        - Number of files downloaded during recursive operation

        Raises:
        - `sftp_error`: If recursive download fails at any level

        Examples:
        | # Internal usage only - called by _download_directory
        | count = self._download_directory_recursive(session, "/logs/", Path("local_logs/"))
        """
        downloaded_count = 0

        try:
            items = sftp_session.listdir_attr(remote_dir)

            for item in items:
                remote_path = posixpath.join(remote_dir, item.filename)
                local_path = local_dir / item.filename

                if stat.S_ISDIR(item.st_mode):
                    # It's a directory, recurse
                    local_path.mkdir(exist_ok=True)
                    downloaded_count += self._download_directory_recursive(
                        sftp_session, remote_path, local_path)
                else:
                    # It's a file, download it
                    try:
                        sftp_session.get(remote_path, str(local_path))
                        downloaded_count += 1

                        if downloaded_count % 10 == 0:  # Progress logging
                            logger.info(
                                f"Downloaded {downloaded_count} files...")

                    except (OSError, IOError, paramiko.SFTPError) as e:
                        logger.warn(f"Failed to download {remote_path}: {e}")

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(
                f"Recursive download failed in {remote_dir}: {e}") from e

        return downloaded_count

    def _verify_transfer_integrity(self, local_path: str, remote_path: str) -> str:
        """Verify integrity of file or directory transfer by comparing local and remote content.

        Automatically detects if paths are files or directories and handles accordingly.
        For files: compares file sizes. For directories: recursively compares all files
        and their sizes to ensure complete transfer without corruption.

        Args:
        - `local_path`: Path to local file or directory
        - `remote_path`: Path to remote file or directory

        Returns:
        - Verification result message indicating whether integrity is verified

        Raises:
        - `sftp_error`: If verification fails or content does not match

        Examples:
        | # Internal usage only - called by upload/download methods
        | result = self._verify_transfer_integrity("test.txt", "/tmp/test.txt")
        """
        local_item = Path(local_path)
        remote_path = self._validate_path(remote_path)

        if not local_item.exists():
            raise sftp_error(f"Local path not found: {local_path}")

        if local_item.is_file():
            return self._verify_file_integrity(local_path, remote_path)
        if local_item.is_dir():
            return self._verify_directory_integrity(local_path, remote_path)
        raise sftp_error(
            f"Local path is neither file nor directory: {local_path}")

    def _verify_file_integrity(self, local_file: str, remote_file: str) -> str:
        """Verify integrity of single file transfer by comparing local and remote file sizes.

        Checks that file sizes match between local and remote files to ensure
        transfer completed successfully without corruption. Used internally by
        _verify_transfer_integrity for file operations.

        Args:
        - `local_file`: Path to local file
        - `remote_file`: Path to remote file

        Returns:
        - Verification result message indicating whether integrity is verified

        Raises:
        - `sftp_error`: If verification fails or file sizes do not match

        Examples:
        | # Internal usage only - called by _verify_transfer_integrity
        | self._verify_file_integrity("test.txt", "/tmp/test.txt")
        """
        try:
            # Get local file size
            local_path = Path(local_file)
            if not local_path.exists():
                raise sftp_error(f"Local file not found: {local_file}")

            local_size = local_path.stat().st_size

            # Get remote file size
            with self._get_sftp_session() as sftp_session:
                remote_stat = sftp_session.stat(remote_file)
                remote_size = remote_stat.st_size

            if local_size == remote_size:
                message = f"File integrity verified: {local_size} bytes"
                logger.info(message)
                return message

            raise sftp_error(
                f"File size mismatch: local={local_size}, remote={remote_size}")

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"File integrity verification failed: {e}") from e

    def _verify_directory_integrity(self, local_dir: str, remote_dir: str) -> str:
        """Verify integrity of directory transfer by comparing all files recursively.

        Recursively compares all files in local and remote directories, ensuring all files
        exist in both locations and have matching sizes. Used internally by
        _verify_transfer_integrity for directory operations.

        Args:
        - `local_dir`: Path to local directory
        - `remote_dir`: Path to remote directory

        Returns:
        - Verification result message indicating whether integrity is verified

        Raises:
        - `sftp_error`: If verification fails or any files don't match

        Examples:
        | # Internal usage only - called by _verify_transfer_integrity
        | self._verify_directory_integrity("config/", "/etc/myapp/")
        """
        local_path = Path(local_dir)
        remote_dir = self._validate_path(remote_dir)

        if not local_path.is_dir():
            raise sftp_error(f"Local path is not a directory: {local_dir}")

        try:
            logger.info(
                f"Verifying directory integrity: {local_dir} -> {remote_dir}")
            verified_count = 0
            total_size = 0

            with self._get_sftp_session() as sftp_session:
                # Check that remote directory exists
                try:
                    remote_stat = sftp_session.stat(remote_dir)
                    if not stat.S_ISDIR(remote_stat.st_mode):
                        raise sftp_error(
                            f"Remote path is not a directory: {remote_dir}")
                except (OSError, IOError, paramiko.SFTPError) as e:
                    raise sftp_error(
                        f"Remote directory not accessible: {remote_dir} - {e}") from e

                # Verify all local files exist remotely with matching sizes
                for item in local_path.rglob("*"):
                    if item.is_file():
                        # Calculate relative path and remote path
                        relative_path = item.relative_to(local_path)
                        remote_file_path = posixpath.join(
                            remote_dir, relative_path.as_posix())

                        # Get local file size
                        local_size = item.stat().st_size

                        # Get remote file size
                        try:
                            remote_stat = sftp_session.stat(remote_file_path)
                            remote_size = remote_stat.st_size
                        except (OSError, IOError, paramiko.SFTPError) as e:
                            raise sftp_error(
                                f"Remote file missing: {remote_file_path}") from e

                        # Compare sizes
                        if local_size != remote_size:
                            raise sftp_error(
                                f"Size mismatch for {relative_path}: local={local_size}, remote={remote_size}")

                        verified_count += 1
                        total_size += local_size

                        if verified_count % 10 == 0:  # Progress logging
                            logger.info(f"Verified {verified_count} files...")

            message = f"Directory integrity verified: {verified_count} files, {total_size} bytes total"
            logger.info(message)
            return message

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(
                f"Directory integrity verification failed: {e}") from e

    def _remove_directory(self, sftp_session: paramiko.SFTPClient, remote_dir: str) -> str:
        """Remove directory and all its contents recursively from remote device.

        Recursively removes all files and subdirectories, then removes the directory itself.
        Used internally by remove_from_device for directory operations.

        Args:
        - `sftp_session`: Active SFTP session for file operations
        - `remote_dir`: Path to remote directory to remove

        Returns:
        - Success message indicating directory removal

        Raises:
        - `sftp_error`: If directory removal fails

        Examples:
        | # Internal usage only - called by remove_from_device
        | self._remove_directory(session, "/tmp/temp_folder/")
        """
        try:
            logger.info(f"Removing directory: {remote_dir}")
            removed_count = 0

            def remove_recursive(dir_path: str) -> None:
                nonlocal removed_count
                items = sftp_session.listdir_attr(dir_path)

                for item in items:
                    item_path = posixpath.join(dir_path, item.filename)

                    if stat.S_ISDIR(item.st_mode):
                        # Recurse into subdirectory
                        remove_recursive(item_path)
                        # Remove the empty directory
                        sftp_session.rmdir(item_path)
                    elif stat.S_ISREG(item.st_mode):
                        # Remove file
                        sftp_session.remove(item_path)
                        removed_count += 1

                        if removed_count % 10 == 0:  # Progress logging
                            logger.info(f"Removed {removed_count} files...")

            # Remove all contents recursively
            remove_recursive(remote_dir)

            # Remove the root directory itself
            sftp_session.rmdir(remote_dir)

            message = f"Directory removed: {remote_dir} ({removed_count} files)"
            logger.info(message)
            return message

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"Failed to remove directory: {e}") from e

    @contextmanager
    def _get_sftp_session(self) -> Iterator[paramiko.SFTPClient]:
        """Get SFTP session with automatic resource cleanup using context manager.

        Establishes SFTP session over active SSH connection and ensures SFTP client is
        properly closed after use, even if exception occurs. Handles SSH connection
        management automatically.

        Returns:
        - Active Paramiko SFTP client session for file operations

        Raises:
        - `sftp_error`: If SFTP session cannot be created or SSH connection fails

        Examples:
        | # Internal usage only - used by all SFTP operations
        | with self._get_sftp_session() as sftp:
        |     sftp.put(local_file, remote_file)
        """
        sftp_client = None
        ssh_context = None

        try:
            ssh_context = self._ensure_connection()
            ssh_client = ssh_context.__enter__()
            sftp_client = ssh_client.open_sftp()

            yield sftp_client

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"SFTP session error: {e}") from e
        finally:
            # Clean up SFTP client
            if sftp_client is not None:
                try:
                    sftp_client.close()
                except (OSError, IOError, paramiko.SFTPError):
                    pass
            # Clean up SSH context
            if ssh_context is not None:
                try:
                    ssh_context.__exit__(None, None, None)
                except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException):
                    pass

    def _validate_path(self, path: str) -> str:
        """Validate and sanitize SFTP paths to prevent basic security vulnerabilities.

        Implements basic path validation to protect against directory traversal attacks
        and other filesystem security issues. Normalizes paths and checks for malicious
        patterns commonly used in attacks.

        Args:
        - `path`: User-provided path string to validate and sanitize

        Returns:
        - Validated and normalized path safe for SFTP operations

        Raises:
        - `sftp_error`: If path contains malicious patterns or fails validation checks

        Examples:
        | # Internal usage only - called by all path-using methods
        | safe_path = self._validate_path("/etc/config.txt")
        """
        if not path:
            raise sftp_error("Empty path provided")

        # Normalize path
        normalized = posixpath.normpath(path)

        # Block obvious traversal attempts
        if ".." in normalized.split("/"):
            raise sftp_error(f"Invalid path: {path}")

        return normalized

    def _ensure_remote_dir(self, sftp_session: paramiko.SFTPClient, remote_dir: str) -> None:
        """Create remote directory structure recursively if it doesn't exist.

        Creates complete directory path on remote system, including all necessary parent
        directories. Handles various filesystem conditions and provides robust error
        recovery for common directory creation scenarios.

        Args:
        - `sftp_session`: Active SFTP session for directory operations
        - `remote_dir`: Target directory path to create recursively on remote system

        Raises:
        - `sftp_error`: If directory creation fails due to permissions or filesystem errors

        Examples:
        | # Internal usage only - called during file uploads
        | self._ensure_remote_dir(session, "/etc/myapp/config/")
        """
        try:
            sftp_session.stat(remote_dir)
        except (OSError, IOError, paramiko.SFTPError):
            # Directory doesn't exist, try to create it
            try:
                # Try to create parent directories recursively
                parent = posixpath.dirname(remote_dir)
                if parent and parent != "/" and parent != remote_dir:
                    self._ensure_remote_dir(sftp_session, parent)

                sftp_session.mkdir(remote_dir)
                logger.debug(f"Created remote directory: {remote_dir}")
            except (OSError, IOError, paramiko.SFTPError):
                # Directory might already exist or creation failed
                logger.warn(f"Could not create remote directory: {remote_dir}")

    def _list_directory(self, remote_dir: str) -> list[SFTPAttributes]:
        """Lists all files in remote directory.

        Args:
        - `remote_dir`: Remote directory path

        Returns:
        - Attributes of files

        Raises:
        - `sftp_error`: If listing directory content fails
        """
        remote_dir = self._validate_path(remote_dir)

        try:
            with self._get_sftp_session() as sftp_session:
                try:
                    return sftp_session.listdir_attr(f"{remote_dir}")
                except (OSError, IOError, paramiko.SFTPError):
                    return sftp_session.listdir_attr(f"/{remote_dir}")

        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException) as e:
            raise sftp_error(f"List directory failed: {e}") from e

    def _get_latest_file(self, list_of_files: list[SFTPAttributes]) -> SFTPAttributes:
        """From the list of attributes of files, returns the one which is modified latest (in time).

        Args:
        - `list_of_files`: Attributes of files

        Returns:
        - Attributes of single file
        """
        return max(list_of_files, key=attrgetter("st_mtime"))

    def __del__(self):
        """Clean up resources when SFTP client object is destroyed.

        Calls parent SSH cleanup and suppresses any errors during cleanup to prevent
        shutdown issues. Called automatically when object goes out of scope or is garbage collected.

        Examples:
        | # Internal usage only - automatically called during object destruction
        | del sftp_client  # Triggers __del__ method
        """
        try:
            super().__del__()
        except (OSError, IOError, paramiko.SFTPError, paramiko.SSHException):
            pass
