"""
Veristand Library
=================

A Robot Framework library for interacting with National Instruments VeriStand.
"""
import os
import subprocess
import psutil
from robot.api import logger as ROBOT_LOGGER
from .ni_errors import ni_errors
try:
    from niveristand.legacy import NIVeriStand
except OSError:
    pass


class veristand:
    """
    Class acts as an interface for National Instruments Veristand
    """
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self, veristand_server_path: str = "C:\\Program Files\\National Instruments\\VeriStand 2023\\veristand-server.exe",
                 ip_address: str = "localhost", target: str = "Controller") -> None:
        """
        Instantiate veristand API.

        *Arguments:*

        veristand_server_path (string, optional): path to veristand-server.exe, default is NI installation folder.
        ip_address (string, optional): ip address to veristand gateway, default localhost.
        """
        self.veristand_ip_address = ip_address
        self.veristand_server_path = veristand_server_path
        self.target = target
        self.pid = None
        self.veristand_error_api = ni_errors()

    def start(self, timeout_s: int = 30):
        """
        Start the NIVeristand server.

        *Arguments:*

        timeout_s (int, optional): timeout in seconds, default 30s.
        """
        try:
            # Check is veristand server IP address valid
            if self.veristand_ip_address is None or self.veristand_ip_address == "":
                raise AttributeError(
                    f"Invalid IP Address, given: {self.veristand_ip_address}")

            # Check is veristand server path valid
            if not os.path.isfile(self.veristand_server_path):
                raise AttributeError(
                    f"Invalid path to veristand-server.exe, given: {self.veristand_server_path}")

            _timeout_s = int(timeout_s)
            if _timeout_s <= 0:
                raise AttributeError(f"Invalid timeout, given: {_timeout_s}")

            # Execute veristand command with status argument
            # NOTE: Using PIPE will make communicate call hang because it generates enough information to STDOUT
            # NOTE: See: https://docs.python.org/2/library/subprocess.html#subprocess.Popen.wait
            with subprocess.Popen([self.veristand_server_path, "start"]) as p:
                # Wait for process call to be done
                p.wait(timeout=_timeout_s)
                # Store Process ID for kill method
                self.pid = p.pid
                print(f"Process id:{p.pid}")
        except Exception as ex:
            raise RuntimeError(
                f"Starting veristand failed, error: {ex}") from ex

    def stop(self, timeout_s: int = 10):
        """
        Stop the NIVeristand server.

        *Arguments:*

        timeout_s (int, optional): timeout in seconds, default 10s.
        """
        try:
            _timeout_s = int(timeout_s)
            if _timeout_s <= 0:
                raise AttributeError(f"Invalid timeout, given: {_timeout_s}")

            # Execute veristand command with status argument
            # NOTE: Using PIPE will make communicate call hang because it generates enough information to STDOUT
            # NOTE: See: https://docs.python.org/2/library/subprocess.html#subprocess.Popen.wait
            with subprocess.Popen([self.veristand_server_path, "stop"]) as p:
                # Wait for process call to be done
                p.wait(timeout=_timeout_s)
        except Exception as ex:
            raise RuntimeError(
                f"Stopping veristand failed, error: {ex}") from ex

    def kill(self):
        """
        Kill Veristand-server process.
        """
        process_name = "veristand-server.exe"
        # Iterate through all running processes
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                # Check if the process name matches the given name
                if proc.info['name'].lower() == process_name.lower():
                    # Kill the process
                    proc.kill()
                    ROBOT_LOGGER.info(
                        f"Process {process_name} with PID {proc.info['pid']} killed.")
                    return
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                ROBOT_LOGGER.info(
                    "Veristand-server has already terminated or permission is denied.")
                return
        ROBOT_LOGGER.info(
            "Veristand-server has already terminated or permission is denied.")

    def get_status(self, timeout_s: int = 10):
        """
        Displays the status of the NIVeristand server.

        *Arguments:*

        timeout_s (int, optional): timeout in seconds, default 10s.
        """
        try:
            _timeout_s = int(timeout_s)
            if _timeout_s <= 0:
                raise AttributeError(f"Invalid timeout, given: {_timeout_s}")

            # Execute veristand command with status argument
            # NOTE: Using PIPE will make communicate call hang because it generates enough information to STDOUT
            # NOTE: See: https://docs.python.org/2/library/subprocess.html#subprocess.Popen.wait
            with subprocess.Popen([self.veristand_server_path, "status"]) as p:
                # Wait for process call to be done
                p.wait(timeout=_timeout_s)
        except Exception as ex:
            raise RuntimeError(
                f"Getting Veristand status failed, error: {ex}") from ex

    def connect_to_system_and_deploy_definition(self, sdf_path=str, deploy: bool = True, timeout_s: int = 60):
        """
        Connects to the system and deploys the specified system definition file.

        This method connects to the VeriStand system using the Workspace2 object and deploys the provided
        system definition file.

        *Arguments:*

        sdf_path (str): Path to the system definition file.
        deploy (bool, optional): Whether to deploy the system definition after connecting. Defaults to True.
        timeout_s (int, optional): Timeout value for the deployment operation in seconds. Defaults to 60s.
        """
        try:
            _timeout_s = int(timeout_s)
            if _timeout_s <= 0:
                raise AttributeError(f"Invalid timeout, given: {_timeout_s}")

            # Check is system definition file exist
            if not os.path.exists(sdf_path):
                raise AttributeError(
                    f"Invalid system definition file path, given: {sdf_path}")

            w_space = self._get_workspace()
            w_space.ConnectToSystem(sdf_path, deploy, (_timeout_s*1000))
        except Exception as ex:
            raise RuntimeError(f"Connecting and deploy failed.\nError message: \
                               {self.veristand_error_api.get_error_message(error_message=str(ex))}.\nException: {ex}") from ex

    def disconnect_system_and_undeploy_definition(self, password: str = "", undeploy: bool = True):
        """
        Disconnects from the VeriStand system and optionally undeploy the system definition.

        *Arguments:*

        :param password: (optional) The password to use for disconnection.
        :param undeploy: (optional) If `True`, undeploy the system definition; otherwise, leave it deployed.
        """
        try:
            _undeploy = bool(undeploy)
            w_space = self._get_workspace()
            w_space.DisconnectFromSystem(
                password=password, undeploy_system_definition=_undeploy)
        except Exception as ex:
            raise RuntimeError(f"Disconnecting and undeploy failed.\nError message: \
                               {self.veristand_error_api.get_error_message(error_message=str(ex))}.\nException: {ex}") from ex

    def get_deployment_status(self):
        """
        Gets the deployment status of the VeriStand system.

        *Arguments:*

        str (dict['state':str, 'systemdefinition_file':str, 'targets':[str]]): The system state.
        """
        try:
            w_space = self._get_workspace()
            return w_space.GetSystemState()
        except Exception as ex:
            raise RuntimeError(
                f"Getting veristand server status failed.\nError message: \
                    {self.veristand_error_api.get_error_message(error_message=str(ex))}.\nException: {ex}") from ex

    def read_channel_value(self, channel_name: str = None):
        """
        Reads the value of a single channel in the VeriStand system.

        *Arguments:*

        channel_name (str): The name of the channel to get the value of.

        *Returns:*

        Any: The value of the specified channel.
        """
        try:
            if channel_name is None:
                raise AttributeError(
                    f"Please provide channel name, given: {channel_name}")

            w_space = self._get_workspace()
            return w_space.GetSingleChannelValue(name=channel_name)
        except Exception as ex:
            raise RuntimeError(
                f"Reading channel failed.\nError message: \
                    {self.veristand_error_api.get_error_message(error_message=str(ex))}.\nException: {ex}") from ex

    def read_channels_values(self, *channel_names):
        """
        Reads the value of a multiple channels in the VeriStand system.

        *Arguments:*

        channel_names (str : list): The names of the channels to get the value of.

        *Returns:*

        List: The values of the specified channels.
        """
        try:
            if not channel_names:
                raise AttributeError(
                    f"Please provide channel names, given:{channel_names}")

            channels = list(channel_names)
            w_space = self._get_workspace()
            return w_space.GetMultipleChannelValues(names=channels)
        except Exception as ex:
            raise RuntimeError(
                f"Reading channels failed.\nError message: \
                    {self.veristand_error_api.get_error_message(error_message=str(ex))}.\nException: {ex}") from ex

    def write_channel_value(self, channel_name: str = None, value: float = None):
        """
        Writes the value of a single channel in the VeriStand system.

        *Arguments:*

        channel_name (str): The name of the channel to set the value for.
        value (float): The value to set for the specified channel.
        """
        try:
            if channel_name is None:
                raise AttributeError(
                    f"Please provide channel name, given: {channel_name}")

            if value is None:
                raise AttributeError(
                    f"Please provide value for channel: {channel_name}, value given: {value}")

            w_space = self._get_workspace()
            w_space.SetSingleChannelValue(name=channel_name, value=value)
        except Exception as ex:
            raise RuntimeError(
                f"Writing channel value failed.\nError message: \
                    {self.veristand_error_api.get_error_message(error_message=str(ex))}.\nException: {ex}") from ex

    def write_channels_values(self, *channel_names_with_values):
        """
        Writes the value of a single channel in the VeriStand system.

        *Arguments:*

        channel_names_with_values (list): Names of the channels with values as a list.
        """
        try:
            if not channel_names_with_values:
                raise AttributeError(
                    "Please provide channel names with channel values, [name, value, name, value]")

            if len(channel_names_with_values) % 2 != 0:
                raise AttributeError(
                    "List should be even, [name, value, name, value]")

            list_tmp = list(channel_names_with_values)
            # Odd items are channels, even items are values
            # some_list[start:stop:step]
            channels = list_tmp[0::2]
            # Convert from str to float
            values = list(map(float, list_tmp[1::2]))

            w_space = self._get_workspace()
            w_space.SetMultipleChannelValues(
                names=channels, values=values)
        except Exception as ex:
            raise RuntimeError(
                f"Writing multiple channels with values failed.\nError message: \
                    {self.veristand_error_api.get_error_message(error_message=str(ex))}.\nException: {ex}") from ex

    def write_channel_fault(self, channel_name: str = None, value: float = None):
        """
        Writes a fault value for a channel in the VeriStand system.

        *Arguments:*

        channel_name (str): The name of the channel to set the fault for.
        value (float): The fault value to set for the specified channel.
        """
        try:
            if channel_name is None:
                raise AttributeError(
                    f"Please provide channel name, given: {channel_name}")

            if value is None:
                raise AttributeError(
                    f"Please provide value for channel: {channel_name}, value given: {value}")

            w_fault_manager = NIVeriStand.ChannelFaultManager(
                gatewayIPAddress=self.veristand_ip_address)
            w_fault_manager.SetFaultValue(channel_name, value)
        except Exception as ex:
            raise RuntimeError(
                f"Setting channel fault failed.\nError message: \
                    {self.veristand_error_api.get_error_message(error_message=str(error_message=str(ex)))}.\nException: {ex}") from ex

    def clear_channel_fault(self, channel_name: str = None):
        """
        Clears a fault for a channel in the VeriStand system.

        *Arguments:*

        channel_name (str): The name of the channel to clear the fault for.
        """
        try:
            if channel_name is None:
                raise AttributeError(
                    f"Please provide channel name, given: {channel_name}")

            w_fault_manager = NIVeriStand.ChannelFaultManager(
                gatewayIPAddress=self.veristand_ip_address)
            w_fault_manager.ClearFault(channel_name)
        except Exception as ex:
            raise RuntimeError(
                f"Clearing channel fault failed.\nError message: \
                    {self.veristand_error_api.get_error_message(error_message=str(ex))}.\nException: {ex}") from ex

    def check_alarms(self):
        """
        Reads alarms and indicates logs warnings or errors if alarms triggered.

        *Returns:*

        Raises an exception if fatal alarm triggered.
        """
        fault_alarms = False
        # Get all alarms defined in system
        alarms_list = NIVeriStand.AlarmManager2(
            gateway_ip_address=self.veristand_ip_address).GetAlarmList(target=self.target)

        # Get detailed information of alarms
        alarms_data_list = NIVeriStand.AlarmManager2(
            gateway_ip_address=self.veristand_ip_address).GetMultipleAlarmsData(target=self.target, alarms=alarms_list, timeout=60*1000)

        for list_item in alarms_data_list:
            name = list_item['Name']
            state = list_item['State']

            if state == 4:
                ROBOT_LOGGER.warn(f"Alarm indication: '{name}'.")

            if state in (2, 3):
                fault_alarms = True
                ROBOT_LOGGER.error(f"Alarm fault: '{name}'.")

        if fault_alarms is True:
            raise SystemError("Fault alarms are active, see errors!")

    def _get_workspace(self):
        """
        Returns a Workspace2 object.

        This method creates and returns a Workspace2 object from the NIVeriStand module using the provided
        gateway IP address.

        *Returns:*

        NIVeriStand.Workspace2: A Workspace2 object, Exception on failure.
        """
        return NIVeriStand.Workspace2(gatewayIPAddress=self.veristand_ip_address)
