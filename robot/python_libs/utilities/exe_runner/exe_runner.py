"""
File which implements exe executor class.
"""
import os
import time
import subprocess
import threading
import psutil
from robot.api import logger


class exe_runner:
    """
    Class that acts as an API for executing EXEs.
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self, *exe_path_and_args, search_text: str = None) -> None:
        """
        Constructor that instantiates EXE runner.

        *Arguments:*

        exe_path_and_args (list): Path and arguments to the EXE.
        search_text (string): String which indicates process running when echoed by process.
        """
        self.exe_path_and_args = exe_path_and_args
        self.search_text = search_text
        self.exe_thread = None
        self.pid = None
        self.ready = False

    def execute(self, timeout: int = 30) -> None:
        """Creates a thread for execution and starts it.

        *Arguments:*

        timeout (int): Timeout to wait exe to start
        """
        if len(self.exe_path_and_args) == 0:
            raise ValueError(
                "No EXE path or arguments given in library import.")

        if not os.path.isfile(self.exe_path_and_args[0]):
            raise ValueError(
                f"The given EXE path does not exist: {self.exe_path_and_args[0]}")

        logger.info(
            f'Given EXE path and arguments: {self.exe_path_and_args}', also_console=True)

        # Start EXE in thread
        self.exe_thread = threading.Thread(target=self._run_exe)
        logger.info("Executing EXE.", also_console=True)
        self.exe_thread.start()
        time_taken = 0
        while not self.ready:
            time.sleep(1)
            time_taken += 1
            if time_taken >= timeout:
                logger.info(
                    f"Timeout:{timeout}, time taken:{time_taken}", also_console=True)
                self.kill()
                logger.info("Problem executing EXE.", also_console=True)
                raise TimeoutError("Problem executing EXE.")
        logger.info(
            "EXE executed successfully.", also_console=True)

    def get_pid(self) -> int:
        """
        Get currently running EXE thread PID (Process Identifier).

        *Returns:*

        pid (int): The Process Identifier of the currently running EXE.
        """
        if not self.exe_thread:
            if self.pid:
                return self.pid
            return 0
        if not self.exe_thread.is_alive():
            return 0
        if self.pid:
            return self.pid
        return 0

    def kill(self) -> None:
        """
        Kill the currently running EXE process.
        """
        if not self.exe_thread:
            if self.pid:
                logger.info(
                    f"Killing running EXE process with PID: {self.pid}", also_console=True)
                try:
                    running_exe = psutil.Process(self.pid)
                    running_exe.kill()
                    self.exe_thread.join()
                    logger.info(
                        "EXE process killed successfully.", also_console=True)
                except BaseException:
                    logger.info(
                        "The given process has already been killed.", also_console=True)
                self.exe_thread = None
                self.pid = None
                self.ready = False
            else:
                logger.info(
                    "No EXE process is running.", also_console=True)
        elif self.exe_thread.is_alive():
            if self.pid:
                logger.info(
                    f"Killing running EXE process with PID: {self.pid}", also_console=True)
                try:
                    running_exe = psutil.Process(self.pid)
                    running_exe.kill()
                    self.exe_thread.join()
                    logger.info(
                        "EXE process killed successfully.", also_console=True)
                except BaseException:
                    logger.info(
                        "The EXE process has already been killed.", also_console=True)
                self.exe_thread = None
                self.pid = None
                self.ready = False
        else:
            logger.info(
                "No EXE thread is currently running.", also_console=True)

    def _run_exe(self) -> None:
        """
        The main executor for EXE.
        """
        try:
            cmd = " ".join(self.exe_path_and_args)
            logger.info(cmd, also_console=True)
            with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
                self.pid = process.pid
                while not self.ready and not process.poll():
                    output = process.stdout.readline()
                    # Wait given ready message to console
                    if output and (self.search_text in output.decode()):
                        self.ready = True
                process.communicate()
        except Exception as e:
            logger.info(e, also_console=True)
