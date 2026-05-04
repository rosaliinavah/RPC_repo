"""
File which implements codesys exe executor class.
"""
import os
import time
import sys
import subprocess
import threading
import configparser
from datetime import datetime
import psutil
from robot.api import logger


class codesys_executer:
    """
    Class that helps executing Codesys with CodesysSocketAPI_server script.
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self, config_file: str) -> None:
        """
        Constructor that reads values from given configuration file.

        *Arguments:*

        config_file (string): Path to the given configuration file.
        """
        self.config_file = config_file
        self.codesys_location = None
        self.profile = None
        self.socket_host = None
        self.socket_port = None
        self.codesys_thread = None
        self.pid = None
        self.ready = False

    @staticmethod
    def timed_logger(data: str, loglevel: str = "Info") -> None:
        """
        Just a print function that adds current time to print.

        *Arguments:*

        data (str): data to log
        loglevel (str): loglevel to use in logging (info, debug, warn, error)
        """
        time_ = datetime.now().strftime("%H:%M:%S")
        if loglevel.lower() == "info":
            logger.info(f"[ {time_} ] - {data}", also_console=True)
        if loglevel.lower() == "debug":
            logger.debug(f"[ {time_} ] - {data}")
        if loglevel.lower() == "warn":
            logger.warn(f"[ {time_} ] - {data}")
        if loglevel.lower() == "error":
            codesys_executer.timed_logger(f"[ {time_} ] - {data}")

    def _parse_configuration_file(self):
        """
        Parses configuration file given in library import
        """
        try:
            if self.codesys_location is not None:
                codesys_executer.timed_logger(
                    "Codesys configuration already parsed.")
                return

            config = configparser.ConfigParser()
            config.read(self.config_file)
            self.codesys_location = config.get(
                'codesys_exe_config', 'location')
            self.profile = config.get('codesys_exe_config', 'profile')
            self.socket_host = config.get('socket_api_server', 'host')
            self.socket_port = config.get('socket_api_server', 'port')
            self.codesys_thread = None
            self.pid = None

            codesys_executer.timed_logger(
                "Initializing Codesys with the following data:")
            codesys_executer.timed_logger(
                f"Location: {self.codesys_location}")
            codesys_executer.timed_logger(f"Profile: {self.profile}")
            codesys_executer.timed_logger(
                f"Socket Host: {self.socket_host}")
            codesys_executer.timed_logger(
                f"Socket Port: {self.socket_port}")
        except AttributeError as e:
            codesys_executer.timed_logger(e, loglevel="Error")
            codesys_executer.timed_logger(
                "No config file given.", loglevel="Error")

    def exec_codesys(self, script: str, timeout: int = 30) -> None:
        """
        Creates a thread for Codesys execution and starts it.

        *Arguments:*

        script (string): The name of the script to be used (CodesysSocketAPI_server.py)
        """
        # Server file exist?
        if os.path.isfile(script):
            script = os.path.abspath(script)
        else:
            raise ValueError("The given script path does not exist.")

        # Parse cfg file
        self._parse_configuration_file()

        ####
        codesys_executer.timed_logger(f'{self.codesys_location} --profile="{self.profile}" '
                                      f'--noUI --runscript="{script}" '
                                      f'--scriptargs="{self.socket_host} {self.socket_port}"')
        ####
        # Start codesys EXE in thread
        self.codesys_thread = threading.Thread(
            target=self.run_codesys, args=(script, ))
        codesys_executer.timed_logger(
            f"Executing Codesys with the following script: {script}")
        self.codesys_thread.start()
        time_taken = 0
        while not self.ready:
            time.sleep(1)
            time_taken += 1
            if time_taken >= timeout:
                self.kill_codesys_process()
                codesys_executer.timed_logger("Problem executing Codesys..")
                sys.exit(1)
        codesys_executer.timed_logger("Codesys executed successfully..")

    def get_process_pid(self) -> int:
        """
        Get currently running CODESYS thread PID.

        *Returns:*

        pid (int): The process ID of the currently running CODESYS.
        """
        if not self.codesys_thread:
            if self.pid:
                return self.pid
            return 0
        if not self.codesys_thread.is_alive():
            return 0
        if self.pid:
            return self.pid
        return 0

    def kill_codesys_process(self) -> None:
        """
        Kill the currently running CODESYS process.
        """
        if not self.codesys_thread:
            if self.pid:
                codesys_executer.timed_logger(
                    f"Killing running CODESYS process with PID: {self.pid}")
                try:
                    running_codesys = psutil.Process(self.pid)
                    running_codesys.kill()
                    self.codesys_thread.join()
                    codesys_executer.timed_logger(
                        "CODESYS process killed successfully.")
                except BaseException:
                    codesys_executer.timed_logger(
                        "The given process has already been killed.")
                self.codesys_thread = None
                self.pid = None
                self.ready = False
            else:
                codesys_executer.timed_logger("No CODESYS process is running.")
        elif self.codesys_thread.is_alive():
            if self.pid:
                codesys_executer.timed_logger(
                    f"Killing running CODESYS process with PID: {self.pid}")
                try:
                    running_codesys = psutil.Process(self.pid)
                    running_codesys.kill()
                    self.codesys_thread.join()
                    codesys_executer.timed_logger(
                        "CODESYS process killed successfully.")
                except BaseException:
                    codesys_executer.timed_logger(
                        "The given process has already been killed.")
                self.codesys_thread = None
                self.pid = None
                self.ready = False
        else:
            codesys_executer.timed_logger("No thread is currently alive.")

    def run_codesys(self, script: str) -> None:
        """
        The main executor for Codesys with the given parameters and arguments.

        *Arguments:*

        script (string): Full path to the script to be loaded in Codesys.
        """
        try:
            with subprocess.Popen(
                f'{self.codesys_location} --profile="{self.profile}" '
                f'--noUI --runscript="{script}" '
                f'--scriptargs="{self.socket_host} {self.socket_port}"',
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
                self.pid = process.pid
                while not self.ready and not process.poll():
                    output = process.stdout.readline()
                    if output and "CODESYS READY" in output.decode():
                        self.ready = True
                process.communicate()
        except Exception as e:
            codesys_executer.timed_logger(e, loglevel="Error")
