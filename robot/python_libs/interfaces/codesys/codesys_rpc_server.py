"""
Server interface to interact with Codesys via RPC protocol
"""
from __future__ import print_function
import sys

# Codesys using IronPython 2.7 so plus lot of other linting errors
# pylint:disable=consider-using-f-string, invalid-name, deprecated-method, undefined-variable, unused-argument, too-many-instance-attributes
# pylint:disable=consider-using-enumerate, import-error

from robotremoteserver import RobotRemoteServer


class CodesysInterface:
    """Interface class to control Codesys

    *Please note:*

    The monitoring works through events which depend on the main message queue.
    While running a script the main message queue is mostly blocked.

    Some methods of the CODESYS script engine contain some code to process the main message queue.
    Sometimes that is not enough and you have to add one or more of system.delay(n) in your script.

    It processes the main message queue while waiting for the specified time to elapse.
    The time should be bigger then 200ms but it depends on the PLC, the amount and type of expressions which are monitored at that moment.
    """

    # Used for sleep value when writing/reading channel values (ms).
    SYSTEM_DELAY = 200

    def __init__(self):
        """
        Initialize class variables.

        *Codesys remote API documentation:*

        https://product-help.schneider-electric.com/Machine%20Expert/V1.1/en/ScriptEngine/index.htm?#t=topics%2Fidx-scriptingengine.htm

        """
        # ScriptCommunicationSettings. Provides access to the communication settings of the device.
        self.communication_parameters = None
        # String, name of the device. For example 'SC10_22262016'.
        self.target_device_name = None
        # ScriptDeviceObject for manipulating device objects. All device objects implementing DeviceObject will be extended with this methods.
        self.device = None
        # List of ScriptScanTargetDescription objects.
        self.devices_found = None
        # String. Path to the project
        self.project_path = None
        # String. Device ip-address. Leave empty if not using Ethernet connection.
        self.device_ip = None
        # ScriptProject. Provides project specific functionality to scripts.
        self.proj = None
        # ScriptObject but name is 'Application'. Modelling of a script object.
        self.__app = None
        # ScriptOnline.ScriptOnlineApplication. Online functionality for the ScriptEngine.
        # Some of the commands may temporarily change the active application.
        self.online_app = None
        # ScriptOnline. ScriptGateway. Script engine representation of a configured gateway for runtime connections.
        self.gateway = None
        # String. Name of the gateway. For example 'Gateway-1'
        self.gateway_name = None
        self.codesys_addr = None
        # List of strings. Names of the devices found on networkscan in a list.
        self.device_name_list = []
        # List of strings. Names of the gateways found in online.gateways in a list.
        self.gateway_name_list = []

    def set_communication_parameters(self, device_ip="localhost", device_name="Device-1", gateway_name='Gateway-1'):
        """
        Sets communication parameters for communication between CODESYS and the device where application should run.

        *Arguments:*

        :param device_ip(str): IP-address of the device. No need to pass if communication settings are saved into the codesys project
        :param device_name(str): Name of the device. No need to pass if communication settings are already saved into the codesys project.
        :param gateway_name(str): Name of the gateway used in communication. Gateway-1 as default.
        """
        self.device_name_list = []
        self.target_device_name = device_name
        self.device_ip = device_ip
        self.gateway_name = gateway_name

        # Check if device is found.
        found = self.proj.find('Device', False)
        if (not found and len(found) < 1):
            print(found)
            print("No device found or more than one device found")
        self.device = found[0]

        # download to hardware, no simulation mode tests
        if self.device.get_simulation_mode():
            self.device.set_simulation_mode(False)

        # Find gateways
        self.gateway_name_list = []
        for gw in online.gateways:
            print("Gateways online:{}".format(gw.name))
            self.gateway_name_list.append(gw.name)
            if gw.name == self.gateway_name:
                self.gateway = gw

        # No gateway found
        if self.gateway_name not in self.gateway_name_list:
            raise AssertionError("Gateway '{}' not found. Add new gateway using keyword 'Add New Gateway' or provide"
                                 " name of existing gateways: {}".format(self.gateway_name, self.gateway_name_list))

        # Perform network scan on gateway.
        self.perform_network_scan()

        # Save found devices names to device name list.
        self.device_name_list = []
        for i in range(len(self.devices_found)):
            print(self.devices_found[i])
            self.device_name_list.append(self.devices_found[i].device_name)
        print(self.device_name_list)

        print("Set device name for communication")
        if len(self.target_device_name) > 0:
            if self.target_device_name not in self.device_name_list:
                raise AssertionError("No device with name '{}' available. Provide Name of the target device from "
                                     "list {}".format(self.target_device_name, self.device_name_list))

            self.device.set_gateway_and_device_name(
                self.gateway, self.target_device_name)

        elif len(self.device_ip) > 0:
            # If port is omitted, the port can be passed in ip_address separated by a colon (e.G. "127.0.0.1:11739")
            self.device.set_gateway_and_ip_address(
                self.gateway, self.device_ip)

        # self.proj.save()
        print("Gateway: '{}' and Device: (name: '{}', IP-address: '{}') set for communication.".
              format(self.gateway.name, self.target_device_name,
                     self.device_ip))

        # Save settings to project
        self.proj.save()

    def get_project(self):
        """
        Returns the currently open project.

        Class: ScriptProject

        *Returns:*

        :return (ScriptProject or None): The currently open project object,
            or None if no project is open.
        """
        # To ensure that RPC picks up an project, if it is executed beforehand.
        if projects.primary:
            self.proj = projects.primary
        if self.proj is not None:
            print("Current project: {}".format(self.proj.path))
            return self.proj.path
        print("No project currently open.")
        return None

    def perform_network_scan(self):
        """
        Performs a network scan on this gateway.
        This method will block at least for the duration of the network scan timeout period.

        Class: ScriptOnline.ScriptGateway
        Doc: https://content.helpme-codesys.com/en/ScriptingEngine/ScriptOnline.html#ScriptOnline.ScriptGateway.perform_network_scan
        """
        print("network scan for gateway:{}".format(self.gateway.name))
        self.devices_found = []
        self.devices_found = self.gateway.perform_network_scan()
        if len(self.devices_found) == 0:
            raise AssertionError("No devices found in network scan.")

    def login(self):
        """
        Performs application login and downloads the source archive to the device. Deletes foreign applications.

        Class: ScriptOnline.ScriptOnlineApplication
        Doc: https://content.helpme-codesys.com/en/ScriptingEngine/ScriptOnline.html#ScriptOnline.ScriptOnlineApplication.login
        login(change_option, delete_foreign_apps)
        """
        print(self.__app)
        if not self.online_app.is_logged_in:
            print("Not yet logged in")
            self.online_app.login(OnlineChangeOption.Never, True)
            system.delay(500)

        print("Application logged in and downloaded.")

    def login_without_download(self):
        """
        Try to login. Do not online update. Do not download. Keep as it is. Do not delete foreign application.

        Class: ScriptOnline.ScriptOnlineApplication
        Doc: https://content.helpme-codesys.com/en/ScriptingEngine/ScriptOnline.html#ScriptOnline.ScriptOnlineApplication.login
        login(change_option, delete_foreign_apps)
        """
        print(self.__app)
        if not self.online_app.is_logged_in:
            print("Not yet logged in")
            self.online_app.login(OnlineChangeOption.Keep, False)
            system.delay(500)

        print("Application logged in.")

    def logout(self):
        """
        Performs application logout

        Class: ScriptOnline
        logout()
        """
        if self.online_app.is_logged_in:
            self.online_app.logout()
            system.delay(500)
        print("Application logged out")

    def start_app(self):
        """
        Starts the application.

        Class: ScriptOnline
        start()
        """
        if not self.online_app.application_state == ApplicationState.run:
            self.online_app.start()
            system.delay(500)
        print("Application running")

    def stop_app(self):
        """
        Stops the application running on PLC.

        Class: ScriptOnline
        stop()
        """
        if self.online_app.application_state == ApplicationState.run:
            self.online_app.stop()
            system.delay(500)
        print("Application stopped")

    def read_variables(self, *variables):
        """
        Reads the values variables given as an argument.
        Class: ScriptOnline
        read_values(*expressions)

        *Arguments:*

        :param variables:  indeterminable number of variable names as separate arguments.
        :return:  Dictionary of variables and their values.
        """
        variables = list(variables)
        print("Reading values of the given variables...")
        print(variables)
        self.online_app.read_values(variables)
        values = self.online_app.read_values(variables)
        system.delay(CodesysInterface.SYSTEM_DELAY)
        print("Read values successfully")

        for i in range(len(values)):
            # Value don't contains #, skip index
            if "#" not in values[i]:
                continue
            # remove Codesys prefix
            values[i] = values[i].split("#")[1]

        return {variables[i]: values[i] for i in range(len(variables))}

    def read_variable(self, *variable):
        """
        Reads the variable value for the given argument.
        Class: ScriptOnline
        read_value(expression)

        *Arguments:*

        :param variable:  one variable name as str.
        :return (Any):  the variable value.
        """

        print("Reading values of the given variable...")
        print(variable[0])
        self.online_app.read_value(variable[0])
        value = self.online_app.read_value(variable[0])
        system.delay(CodesysInterface.SYSTEM_DELAY)

        print(value)
        print("Read values successfully")

        # Value don't contains #
        if "#" not in value:
            return value

        # remove Codesys prefix
        return value.split("#")[1]

    def write_variables(self, **variables_and_values):
        """
        Sets the values of given variables to desired values.
        Class: ScriptOnline
        set_prepared_value(expression, value)

        *Arguments:*

        :param variables_and_values: indeterminable number of variables and their desired values as key-value pairs.
        """
        print("Writing given variables to desired values...")
        for var, value in variables_and_values.items():
            print(var, value)
            var = str(var)
            value = str(value)
            self.online_app.set_prepared_value(var, value)
        self.online_app.write_prepared_values()
        system.delay(CodesysInterface.SYSTEM_DELAY)
        print("All values written.")

    def write_variable(self, variable, value):
        """
        Set the value of given variable to desired value.
        Class: ScriptOnline
        set_prepared_value(expression, value)

        *Arguments:*

        :param variable: variable to be written.
        :param value: value to be written.
        """
        print("Writing given variables to desired values...")
        print(variable, value)
        self.online_app.set_prepared_value(variable, value)
        self.online_app.write_prepared_values()
        system.delay(CodesysInterface.SYSTEM_DELAY)

        print("All values written.")

    def enter_debug_mode(self):
        """
        Enters debug mode.
        Class: System
        system.commands returns a list of System.ScriptCommands

        *Solution found from Codesys forum:*

        https://forge.codesys.com/forge/talk/Engineering/thread/cb4c263657/
        """
        system.prompt_handling |= PromptHandling.ProcessScriptPrompts  # this forwards prompts to script
        # this silences other prompts
        system.prompt_handling &= ~PromptHandling.ForwardSimplePrompts
        # you have to put it before the execute
        system.prompt_answers["EnterDebugMode_Prompt"] = PromptResult.OK
        print(system.prompt_answers)
        system.commands["sil2_commands", "enter_debug_mode"].execute(
            str(self.device.guid))
        system.delay(500)
        print("Entered debug mode.")

    def force_values(self, **variables_and_values):
        """
        Forces the values of given variables to desired values.

        *Arguments:*

        variables_and_values: indeterminable number of variables and their desired values as key-value pairs.
        """
        print("Forcing given variables to desired values...")
        for var, value in variables_and_values.items():
            self.online_app.set_prepared_value(var, value)
        self.online_app.force_prepared_values()
        system.delay(500)
        print("All values forced.")

    def unforce_values(self):
        """
        Unforces all forced variables
        """
        print("Unforcing given variables...")
        system.commands['online', 'unforceactiveapplication'].execute()
        system.delay(500)
        print("All values unforced.")

    def open_project(self, project_path):
        """
        Opens the project, sets default credentials, (cleans application build) and creates online application.

        Class : ScriptProjects
        open(path, password=None, primary=True, encryption_password=None, session_user=None, session_password=None,
             update_flags='VersionUpdateFlags.NoUpdates', allow_readonly=False)

        Class: ScriptOnline
        create_online_application(application=None)
        -- application (ScriptObject) -- The application object to use. If this parameter is omitted, the active application is used.

        *Arguments:*

        :param project_path(str): Path to the Codesys project.
        """
        self.project_path = project_path

        # Check if primary projects exists
        if projects.primary is not None:
            projects.primary.close()
            system.delay(500)

        # Open project and hide versionupdate pop-up.
        print(projects)
        print("Opening project: {}".format(self.project_path))
        self.proj = projects.open(self.project_path, update_flags=(
            VersionUpdateFlags.SilentMode | VersionUpdateFlags.NoUpdates))
        system.delay(500)

        # ScriptObject but name is 'Application'
        self.__app = self.proj.active_application
        print(str(self.__app.get_name()))

        self.online_app = online.create_online_application(self.__app)
        print(self.online_app)

        print("Project opened and and online application built.")

    def close_project(self):
        """
        Closes the active project

        Class: ScriptProject
        close()
        """
        self.proj.close()
        system.delay(500)
        print("Project closed")

    def reset_warm(self):
        """
        Executes reset warm
        """
        self.online_app.reset(reset_option=ResetOption.Warm)
        system.delay(500)
        print("Reset warm completed")

    def reset_cold(self):
        """
        Executes reset cold
        """
        self.online_app.reset(reset_option=ResetOption.Cold)
        system.delay(500)
        print("Reset cold completed")

    def reset_original(self):
        """
        Executes reset original
        """
        self.online_app.reset(reset_option=ResetOption.Original)
        system.delay(500)
        print("Reset original completed")

    def scan_network(self, gateway="Gateway-1", device="Device"):
        """
        Scans Devices from Gateway by Device name

        *Arguments:*

        gateway (str): Name of the gateway
        device (str): Name of the device
        """
        gw = online.gateways[gateway]
        devices = self.proj.find(device, False)
        dev = devices[0]
        dev.set_gateway_and_device_name(
            gateway=gw, device_name=self.device_name_list[0])
        system.commands["devicecommunication", "setactivepath"].execute()
        system.commands["file", "save"].execute()
        system.delay(500)

    def set_default_credentials(self, username, password):
        """
        Set the default credentials for current CODESYS instance.

        *Arguments:*

        username (str): Username for the user manager of current device.
        password (str): Password for the user manager of current device.

        *Returns:*

        (str): Success if successful.
        """
        online.set_default_credentials(username, password)
        system.delay(500)
        print("Credentials set.")

    def add_new_gateway(self, name, port, ip_addr='localhost'):
        """
        Adds new gateway to communication settings of Codesys

        *Arguments:*

        :param name: name of the new gateway
        :param port: port number of the new gateway
        :param ip_addr: Ip-address of the gateway. localhost as default
        """
        params = {0: ip_addr, 1: port}
        tcp_driver = online.gateway_drivers["TCP/IP"]
        online.gateways.add_new_gateway(name, params, tcp_driver)

    def find_gateway(self, name):
        """
        Finds a gateway by given name

        *Arguments:*

        :param name: name of the gateway
        """
        return online.gateways.find_with_name(name)


if __name__ == "__main__":
    print("CODESYS READY")
    RobotRemoteServer(CodesysInterface(), *sys.argv[1:])
    system.exit(0)
