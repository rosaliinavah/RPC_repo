"""
File for Codesys server API.

This file is provided as an argument for codesys.exe so it can be use through RPC protocol.

Dependencies:
-------------
SocketServer, Codesys installation
System.Net. Codesys installation
"""
from __future__ import print_function
import os
import sys
import json
import inspect
import re
from datetime import datetime
from ast import literal_eval
# imported from Codesys IronPython library
# pylint:disable=import-error
import SocketServer
from System.Net import WebClient

# Codesys using IronPython 2.7 so e.g. f string not supported etc
# pylint:disable=consider-using-f-string, invalid-name, deprecated-method, undefined-variable, unused-argument


class CodesysCommandParser():
    """
    Class that handles parsing and executing commands sent to socket server.
    """

    def __init__(self):
        """
        Initializes all Codesys related objects used in this parser to None.

        If there is currently a project open, it will be set as current
        project.
        """
        self.proj = None
        self.app = None
        self.device = None
        self.gateway = None
        self.address = None
        self.scan_res = None
        self.appstate = None
        self.communication_settings = None
        self.init_api_data()
        self.commands = self.__generate_command_dictionary()

    @staticmethod
    def __value_converter(value):
        """
        This is a small helper functions that converts values so that they work as intended with CODESYS.

        *Arguments:*

        value (str): Value to convert.

        *Returns:*

        (str): Returns the converted/fixed value.
        """
        if "2#" in value:
            return value.replace("2#", "")
        if "16#" in value:
            return value.replace("16#", "")
        if "\"" in value:
            return value.replace("\"", "")
        return value

    def __remove_datatypes(self, data):
        """
        Removes datatype from return value.
        For example BYTE#, INT#, etc.

        *Arguments:*

        data (str): Initial data string.

        *Returns:*

        (str): Parsed data.
        """
        pattern = r'^\w+#'
        return re.sub(pattern, '', data)

    @staticmethod
    def __timed_printer(data):
        """
        Just a print function that adds current time to print.

        *Arguments:*

        data (str): The data to print out with a timestamp.
        """
        time = datetime.now().strftime("%H:%M:%S")
        print("[ {} ] - {}".format(time, data))

    def __convert_from_json(self, json_data):
        """Convert command and arguments from received json.

        *Arguments:*

        json_data: The JSON data to parse.

        *Returns:*

        (tuple): Tuple containing the parsed command, arguments and a dictionary presentation of the arguments.
        """
        conversion = json.loads(json_data)
        command = conversion['command']
        args = conversion['args']
        args_dict = {}
        try:
            command_args = inspect.getargspec(self.commands[command])[0][1:]
        except BaseException:
            command_args = None
        CodesysCommandParser.__timed_printer("Command: {}".format(command))
        if args:
            CodesysCommandParser.__timed_printer("--- Arguments ---")
            CodesysCommandParser.__timed_printer(args)
            args_dict['args'] = {}
            if command in ('install_library', 'uninstall_library'):
                args_dict['args'][command_args[0]] = args
                CodesysCommandParser.__timed_printer(
                    "{} = {}".format(command_args[0], args))
            elif len(args) > len(command_args):
                raise ValueError(
                    "ERROR: Too many arguments given for the function.")
            else:
                for index, value in enumerate(args):
                    args_dict['args'][command_args[index]] = value
                    CodesysCommandParser.__timed_printer(
                        "{} = {}".format(command_args[index], value))
        return command, args, args_dict

    @staticmethod
    def __convert_to_json(data):
        """
        Convert given dictionary to JSON string.

        *Arguments:*

        data (dict): Dictionary to be converted into JSON.

        *Returns:*

        (str): The JSON conversion.
        """
        conversion = json.dumps(data, indent=4)
        return conversion

    def __get_compile_errors(self):
        """
        Get the compile message to ensure that compiling was successful.

        *Returns:*

        (str): Returns the error/completion message.
        """
        errors = self.get_message_objects(
            "97f48d64-a2a3-4856-b640-75c046e37ea9")
        for error in errors.split("|"):
            if "Compile complete" in error or "Build complete" in error:
                return error
            if "C0188: Device not installed" in error:
                return error

    def __generate_command_dictionary(self):
        """
        Generates a dictionary of all the current api commands and related function calls.

        *Returns:*

        (dict): Dictionary including all commands and function calls.
        """
        # Dictionary of all current api functions and their function calls.
        commands = {
            "restart_server": self.restart_server,
            "get_api_commands": self.get_all_api_commands,
            "reset_api": self.init_api_data,
            "get_help_for_command": self.get_help_for_command,
            "get_current_api_info": self.get_current_api_info,
            "shutdown_codesys": self.shutdown_codesys,
            "shutdown_server": self.shutdown_server,
            "build": self.build_app,
            "clean": self.clean_app,
            "generate_code": self.generate_code,
            "rebuild": self.rebuild_app,
            "create_boot_application": self.create_boot_application,
            "get_system_messages": self.get_system_messages,
            "get_message_categories": self.get_message_categories,
            "get_message_objects": self.get_message_objects,
            "health": self.health_check,
            "get_device": self.get_device,
            "update_device": self.find_and_update_device,
            "used_libraries": self.find_used_libraries,
            "add_device_description": self.add_device_description,
            "remove_device_description": self.remove_device_description,
            "scan": self.perform_scan,
            "start_app": self.start_app,
            "stop_app": self.stop_app,
            "create_gateway": self.create_gateway,
            "remove_gateway": self.remove_gateway,
            "set_gateway": self.set_gateway,
            "get_gateways": self.get_gateways,
            "set_address": self.set_address,
            "get_installed_libraries": self.get_installed_libraries,
            "install_library": self.install_library,
            "uninstall_library": self.uninstall_library,
            "full_config": self.full_config,
            "open_project": self.open_project,
            "write": self.write_value,
            "read": self.read_value,
            "logout": self.logout,
            "login": self.login,
            "warm_reset": self.warm_reset,
            "cold_reset": self.cold_reset,
            "origin_reset": self.origin_reset,
            "set_ip": self.set_address_by_ip,
            "missing_libraries": self.find_missing_libraries,
            "download_missing_libs": self.download_missing_libs,
            "download_file": self.download_file,
            "upload_file": self.upload_file,
            "rename_file": self.rename_file,
            "delete_file": self.delete_file,
            "rename_directory": self.rename_directory,
            "delete_directory": self.delete_directory,
            "create_directory": self.create_directory,
            "get_file_list": self.get_file_list,
            "conf_device_gateway_and_address": self.set_gateway_and_address_to_device,
            "get_library": self.get_library_version,
            "create_project": self.create_project,
            "save_project": self.save_project,
            "close_project": self.close_project,
            "import_native": self.import_native,
            "export_native": self.export_native,
            "import_xml": self.import_xml,
            "export_xml": self.export_xml,
            "unforce": self.unforce_values,
            "set_default_credentials": self.set_default_credentials,
            "change_task_cyclic_interval": self.change_task_cyclic_interval}
        return commands

    def handle_request(self, data):
        """
        Handles incoming API request and initiates commands based on it.

        *Arguments:*

        data (str): The incoming data string from socket.

        *Returns:*

        get_api_function(): Returns the return value of the given command with the given arguments.
        """
        command, parameters, param_dict = self.__convert_from_json(data)
        CodesysCommandParser.__timed_printer(
            "Server received command: {}".format(command))
        return self.get_api_function(command, parameters, param_dict)

    def restart_server(self):
        """
        Restart whole server instance.
        """
        self.init_api_data()
        CodesysCommandParser.__timed_printer(
            "Restarting whole server instance.")
        return "Success"

    def get_current_api_info(self):
        """
        Returns the states of current API variables.

        *Returns:*

        (str): String containing all the states of API variables.
        """
        ret_string = ""
        if self.proj:
            ret_string += "Current Primary Project: {}\n".format(
                self.proj.path)
        else:
            ret_string += "Current Primary Project: {}\n".format(self.proj)
        if self.app:
            ret_string += "Application is selected: {}\n".format(True)
            with online.create_online_application(self.app) as onlineapp:
                if onlineapp.is_logged_in:
                    ret_string += "Online Application is logged in: {}\n".format(
                        True)
                else:
                    ret_string += "Online Application is logged in: {}\n".format(
                        False)
                if self.appstate:
                    ret_string += "Online Application state: {}\n".format(
                        self.appstate)
                else:
                    ret_string += "Online Application state: {}\n".format(
                        "Stopped")
        else:
            ret_string += "Application is selected: {}\n".format(False)
        if self.gateway:
            try:
                ret_string += "Current Set Gateway: {}\n".format(
                    self.gateway.name)
            except BaseException:
                ret_string += "Current Set Gateway: {}\n".format(self.gateway)
        else:
            ret_string += "Current Set Gateway: {}\n".format(self.gateway)
        ret_string += "Current Set Address: {}\n".format(self.address)
        if self.device:
            ret_string += "Current Set Device: {}\n".format(
                self.device.get_name())
        else:
            ret_string += "Current Set Device: {}\n".format(self.device)
        return ret_string

    def init_api_data(self):
        """
        Initialize all API objects to None.
        Check current project information and initialize data accordingly.

        *Returns:*

        (str): Success if the command is executed.
        """
        self.proj = None
        self.app = None
        self.device = None
        self.gateway = None
        self.address = None
        self.scan_res = None
        self.appstate = None
        self.communication_settings = None
        # imported from Codesys IronPython library
        # pylint:disable=undefined-variable, self-assigning-variable
        if projects.primary:
            self.proj = projects.primary
            self.device = projects.primary.find("Device", True)[0]
            self.app = self.proj.active_application
            self.communication_settings = self.device.get_device_communication_settings()
            try:
                self.gateway = online.gateways[self.communication_settings.gateway_guid]
                self.address = self.communication_settings.device_address
            except BaseException:
                self.gateway = None
                self.address = None
            with online.create_online_application(self.app) as onlineapp:
                if onlineapp.is_logged_in:
                    self.appstate = onlineapp.application_state
        system.delay(200)

        return "Success"

    def get_api_function(self, command, parameters, param_dict):
        """
        Get and execute the api function.

        *Arguments:*

        command (str): Command string.
        parameters (str): Arguments to be given to the command.
        param_dict (dict): The parameters that the command awaits.

        *Returns:*

        (str): JSON that is constructed based on command, parameters and return value.
        """
        ret_dict = {}
        ret_dict['command'] = command
        ret_dict['args'] = {}
        try:
            if param_dict:
                ret_dict['args'] = param_dict['args']
            # Get the command from the list.
            if command not in self.commands:
                CodesysCommandParser.__timed_printer(
                    "Command {} does not exist in the API.".format(command))
                ret_dict['return'] = "Command failed: This command does not exist."
                ret_json = CodesysCommandParser.__convert_to_json(ret_dict)
                return ret_json
            CodesysCommandParser.__timed_printer("Command received to server.")
            CodesysCommandParser.__timed_printer("Command: {}".format(command))
            ret = ""
            if not parameters:
                ret = self.commands[command]()
            else:
                CodesysCommandParser.__timed_printer(
                    "Args: {}".format(parameters))
                # Check if arguments are given, if not just execute function.
                # Replace all True or False strings with boolean.
                # Also replace all None strings with None.
                for index, parameter in enumerate(parameters):
                    if parameter in ('True', 'False', 'None'):
                        parameters[index] = literal_eval(parameter)
                # If install or uninstall library is called, the parameters are
                # a list of variables and do not need to be separated.
                if command in ('install_library', 'uninstall_library'):
                    ret = self.commands[command](parameters)
                    return ret
                # Convert parameters list to arguments based on given amount of
                # arguments.
                ret = self.commands[command](*parameters)
            ret_dict['return'] = ret
            ret_json = CodesysCommandParser.__convert_to_json(ret_dict)
            return ret_json
        except Exception as e:
            ret_dict['return'] = str(e)
            ret_json = CodesysCommandParser.__convert_to_json(ret_dict)
            return ret_json

    def get_all_api_commands(self):
        """
        Gets all the currently possible API commands.

        *Returns:*

        (str): String containing all the commands separated with |.
        """
        return "|".join(self.commands)

    def get_help_for_command(self, command_name):
        """
        Returns docstring for given API command.

        *Arguments:*

        command_name (str): The name of the command to get info for.

        *Returns:*

        (str): Returns the docstring for the given command.
        """
        doc_string = self.commands[command_name].__doc__.split("\n")
        for index, value in enumerate(doc_string):
            doc_string[index] = value.strip()
        return "\n".join(doc_string)

    def build_app(self):
        """
        Builds the current open application/project.

        *Returns:*

        (str): Returns the state of the build app command.
        """
        if self.app:
            self.app.build()
            error = self.__get_compile_errors()
            return error
        return "Command failed: No application exists."

    def clean_app(self, full=False):
        """
        Cleans the current open application/project.

        *Returns:*

        (str): Returns the state of the clean app command.
        """
        if self.app:
            if full:
                self.proj.clean_all()
            else:
                self.app.clean()
            return "Success"
        return "Command failed: No application exists."

    def generate_code(self):
        """
        Generates code for the current open application/project.

        *Returns:*

        (str): Returns the state of the generate code command.
        """
        if self.app:
            self.app.generate_code()
            error = self.__get_compile_errors()
            return error
        return "Command failed: No application exists."

    def rebuild_app(self):
        """
        Rebuilds the current open application/project.

        *Returns:*

        (str): Returns the state of the rebuild command.
        """
        if self.app:
            self.app.rebuild()
            error = self.__get_compile_errors()
            return error
        return "Command failed: No application exists."

    def get_system_messages(self):
        """Gets the current script messages from the script message buffer in Codesys.

        *Returns:*

        (str): String with all messages divided by |.
        """
        ret_str = "|".join(system.get_messages())
        return ret_str

    def get_message_categories(self, bActive=True):
        """
        Gets all the message categories.

        *Arguments:*

        bActive (bool): If this is True, only the active categories are returned.

        *Returns:*

        (str): String with all categories divided by |.
        """
        ret_list = []
        for category in system.get_message_categories(bActive):
            ret_list.append(str(category))
        ret_string = "|".join(ret_list)
        return ret_string

    def get_message_objects(self, category=None):
        """
        Returns all messages from given category.

        *Returns:*

        ret_str (str): String with all categories divided by |.
        """
        ret_list = []
        for message in system.get_message_objects(category=category):
            ret_list.append(str(message))
        ret_str = "|".join(ret_list)
        return ret_str

    def create_boot_application(
            self,
            filename,
            update_compile_info,
            write_visu_files):
        """
        Creates a boot application for the current open application/project.

        *Arguments:*

        filename (str): The filename to write the boot application to.
        update_compile_info (bool): if set to true, also writes the compile information (compiler reference context) to the project directory.
        write_visu_files (bool): if set to true, also writes the visualization files into the output directory.

        *Returns:*

        (str): Returns the state of the create boot application command.
        """
        if self.app:
            self.app.create_boot_application(
                filename, update_compile_info, write_visu_files)
            error = self.__get_compile_errors()
            return error
        return "Command failed: No application exists."

    def health_check(self):
        """
        Health check for server.

        *Returns:*

        (str): Success if successful.
        """
        return "Success"

    def create_project(self, path, primary=True):
        """
        Creates a new project.

        *Arguments:*

        path (str): Path for the new project to be created.
        primary (bool): If set to True, the new project will be set as the primary project.

        *Returns:*

        (str): Success if successful.
        """
        if projects.primary:
            projects.primary.close()
        self.init_api_data()
        CodesysCommandParser.__timed_printer("Creating new project..")
        self.proj = projects.create(path, primary)
        return "Success"

    def open_project(self, project):
        """
        Opens up the given project in Codesys.

        *Arguments:*

        project (str): The full path to the project to be opened.

        *Returns:*

        (str): Success if successful.
        """
        if not project:
            return "Command failed: No project given."
        CodesysCommandParser.__timed_printer("Opening project..")
        if projects.primary:
            projects.primary.close()
        self.init_api_data()

        # opens project
        try:
            self.proj = projects.open(
                project,
                update_flags=VersionUpdateFlags.SilentMode | VersionUpdateFlags.UpdateAll)
        except BaseException:
            self.proj = projects.primary
        if self.proj:
            self.app = self.proj.active_application
            return "Success"

        return "Command failed: Something went wrong with project opening."

    def save_project(self):
        """
        Save the current open project.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        if self.proj:
            self.proj.save()
            return "Success"

        return "Command failed: No project open."

    def close_project(self):
        """
        Close the current open project.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        if self.proj:
            self.proj.close()
            self.init_api_data()
            return "Success"

        return "Command failed: No project open."

    def import_native(self, filenames=None, _filter=None, handler=None):
        """
        Import native codesys files to current open project.

        *Arguments:*

        filenames (str): Path to the files that should be imported.
        _filter (str): Filter for the importation.
        handler (obj): Not supported, should be left as None.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        if not self.proj:
            return "Command failed: No project open to import to."
        if filenames:
            filenames = filenames.split(",")
            if len(filenames) == 1:
                filenames = filenames[0]
                self.proj.import_native(
                    filename=filenames, filter=_filter, handler=handler)
            else:
                self.proj.import_native(
                    filenames=filenames, filter=_filter, handler=handler)
        else:
            return "Command failed: No filename paths given to import."

        return "Success"

    def export_native(
            self,
            objects=None,
            destination=None,
            recursive=False,
            one_file_per_subtree=False,
            profile_name=None,
            reporter=None):
        """
        Export native codesys files to given destination.

        *Arguments:*

        objects (str): Not yet supported. Function exports everything inside the current project.
        destination (str): Path to save the export to.
        recursive (bool): If everything is exported recursively. Should be set to True, if everything needs to be exported.
        one_file_per_subtree (bool): If set to true all objects will be saved to separate files.
        profile_name (str): This is not supported and does not work for some reason (Codesys side problem)
        reporter (obj): This is not yet supported to be used. None is enough for exporting.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        if not self.proj:
            return "Command failed: No project open to export."
        if not destination:
            return "Command failed: No destination path given."
        if not objects:
            export = []
            for item in self.proj.get_children():
                export.append(item)
                export.extend(item.get_children())
            self.proj.export_native(
                export,
                destination,
                recursive=recursive,
                one_file_per_subtree=one_file_per_subtree,
                reporter=reporter)
            return "Success"

    def import_xml(self, path, reporter, import_folder_structure):
        """
        Import given XML file to current open project.

        *Arguments:*

        path (str): Path to the XML file.
        reporter (obj): This is not yet supported to be used. None is enough for exporting.
        import_folder_structure (bool): If set to True will import the whole folder structure.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        if self.proj:
            self.proj.import_xml(
                dataOrPath=path,
                reporter=reporter,
                import_folder_structure=import_folder_structure)
            return "Success"

        return "Command failed: No project open. Please create a new project or open an existing one before importing."

    def export_xml(
            self,
            objects=None,
            reporter=None,
            path=None,
            recursive=False,
            export_folder_structure=False,
            declarations_as_plaintext=False):
        """
        Import given objects into XML file either as a string or into given path.

        *Arguments:*

        objects (tuple): Not yet supported.
        reporter (ExportReporter): Not yet supported.
        path (str): Path where the exported file will be saved.
        recursive (bool): If all children of the given object should be exported. This should be set to True (Because everything will be exported.)
        export_folder_structure (bool): If set to True, the folder
        structure of the objects is also exported. This is a proprietary extension to the default schema.
        declarations_as_plaintext (bool): If set to true, the declaration parts will be additionally exported as plain text
        (which is lossless in contrast to the default schema). This is a proprietary extension to the default schema.
        (Import will automatically recognize and prefer the plain text format if present)

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        if self.proj:
            pass
        else:
            return "Command failed: No project open."
        if not objects:
            export = []
            for item in self.proj.get_children():
                export.append(item)
                export.extend(item.get_children())
            self.proj.export_xml(
                objects=export,
                reporter=reporter,
                path=path,
                recursive=recursive,
                export_folder_structure=export_folder_structure,
                declarations_as_plaintext=declarations_as_plaintext)
            return "Success"

    def add_device_description(self, description_path):
        """
        Adds the given device description file to the System Repository.
        Returns Success if successful.

        *Arguments:*

        description_path (str): Full path to the device description file.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        sys_repo = device_repository.sources['System Repository']
        if not os.path.exists(description_path):
            if not os.path.exists(
                os.path.abspath(
                    os.getcwd() +
                    os.sep +
                    description_path)):
                return "Command failed: Given path does not exist."
        device_repository.import_device(description_path, sys_repo)
        device_repository.rebuild_device_cache()
        return "Success"

    def remove_device_description(self, device_name, source=None):
        """
        Removes the given device description file from the default
        repository. Returns Success if successful.

        *Arguments:*

        device_name (str): Name of the device description to be removed.
        source (str): Repository to remove the device from

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        if source:
            source = device_repository.sources[source]
        else:
            source = device_repository.sources['System Repository']
        devices = device_repository.get_all_devices(device_name)
        if devices:
            for device in devices:
                CodesysCommandParser.__timed_printer(
                    "Found device: {}".format(device.device_info.name))
                removed_device = device.device_id
                device_repository.remove_device(removed_device, source)
                device_repository.rebuild_device_cache()
        else:
            CodesysCommandParser.__timed_printer(
                "No device with given name found.")
            return "Success"
        return "Success"

    def get_device(self, dev):
        """
        Finds the given device inside the project and makes it a class
        object. Returns Success if successful.

        *Arguments:*

        dev (str): The name of the device in the opened project.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer("Finding device: {}".format(dev))
        if projects.primary:
            devices = projects.primary.find(dev, True)
            if devices:
                self.device = devices[0]
            else:
                return "Command failed: Given device not found."
            return "Success"
        return "Command failed: No project open."

    def find_and_update_device(self, dev, version):
        """
        Finds the given device object in the project. Creates a device object inside handler class.
        Updates the given device object to the given version.

        *Arguments:*

        project (str): The full path to the project to be opened.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer("Finding device: {}".format(dev))
        if projects.primary:
            devices = projects.primary.find(dev, True)
            if devices:
                self.device = devices[0]
            else:
                return "Command failed: Given device not found."
        else:
            return "Command failed: No project open."
        if not self.device is None:
            CodesysCommandParser.__timed_printer("Device found.")
            device_identification = self.device.get_device_identification()
            if device_identification.version != version:
                CodesysCommandParser.__timed_printer(
                    "Updating device with device description version: {}".format(version))
                self.device.update(device_identification.type,
                                   device_identification.id, version)
                CodesysCommandParser.__timed_printer("Update done.")
            else:
                CodesysCommandParser.__timed_printer(
                    "Device already updated to given version.")
        return "Success"

    def download_file(self, local_file, remote_file, force_overwrite):
        """
        Download given file to device.

        *Arguments:*

        local_file (str): Path of the local file.
        remote_file (str): Path of the remote file.
        overwrite (bool): Force the overwrite if remote file already exists.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        with online.create_online_device(self.device) as onlinedevice:
            if not onlinedevice.connected:
                onlinedevice.connect()
            if not isinstance(force_overwrite, bool):
                force_overwrite = literal_eval(force_overwrite)
            CodesysCommandParser.__timed_printer(
                "Downloading file {} to device as {}.".format(
                    remote_file, local_file))
            onlinedevice.download_file(
                local_file, remote_file, force_overwrite)
            CodesysCommandParser.__timed_printer("Download done.")
        return "Success"

    def upload_file(self, remote_file, local_file, force_overwrite):
        """
        Upload given file from device to local.

        *Arguments:*

        remote_file (str): Path of the remote file.
        local_file (str): Path of the local file.
        overwrite (bool): Force the overwrite if the local file already exists.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        with online.create_online_device(self.device) as onlinedevice:
            if not onlinedevice.connected:
                onlinedevice.connect()
            if not isinstance(force_overwrite, bool):
                force_overwrite = literal_eval(force_overwrite)
            CodesysCommandParser.__timed_printer(
                "Uploading file {} from device as {}.".format(
                    remote_file, local_file))
            onlinedevice.upload_file(remote_file, local_file, force_overwrite)
            CodesysCommandParser.__timed_printer("Upload done.")
        return "Success"

    def rename_file(self, old_name, new_name):
        """
        Rename given file in device.

        *Arguments:*

        old_name (str): Path of the remote file with the old name.
        new_name (str): Path to the remote file with the new name.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        with online.create_online_device(self.device) as onlinedevice:
            if not onlinedevice.connected:
                onlinedevice.connect()
            CodesysCommandParser.__timed_printer(
                "Renaming file {} to {}.".format(
                    old_name, new_name))
            onlinedevice.rename_file(old_name, new_name)
            CodesysCommandParser.__timed_printer("Rename done.")
        return "Success"

    def delete_file(self, remote_file):
        """
        Delete given file from device.

        *Arguments:*

        remote_file (str): Remote path to the file.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        with online.create_online_device(self.device) as onlinedevice:
            if not onlinedevice.connected:
                onlinedevice.connect()
            CodesysCommandParser.__timed_printer(
                "Deleting file {} from device.")
            onlinedevice.delete_file(remote_file)
            CodesysCommandParser.__timed_printer("File deleted.")
        return "Success"

    def create_directory(self, remote_directory):
        """
        Create dictionary in device.

        *Arguments:*

        remote_directory (str): Path to the new directory.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        with online.create_online_device(self.device) as onlinedevice:
            if not onlinedevice.connected:
                onlinedevice.connect()
            CodesysCommandParser.__timed_printer(
                "Creating directory {} to device.".format(remote_directory))
            onlinedevice.create_directory(remote_directory)
            CodesysCommandParser.__timed_printer("Directory created.")
        return "Success"

    def rename_directory(self, old_name, new_name):
        """
        Rename directory in device.

        *Arguments:*

        old_name (str): Path of the remote directory with the old name.
        new_name (str): Path of the remote directory with the new name.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        with online.create_online_device(self.device) as onlinedevice:
            if not onlinedevice.connected:
                onlinedevice.connect()
            CodesysCommandParser.__timed_printer(
                "Trying to rename the folder {} to {}.".format(
                    old_name, new_name))
            onlinedevice.rename_directory(old_name, new_name)
            CodesysCommandParser.__timed_printer("Rename successful.")
        return "Success"

    def delete_directory(self, remote_directory, recursive):
        """
        Delete directory from device.

        *Arguments:*

        remote_directory (str): Path of the remote directory.
        recursive (bool): If True, delete directory recursively.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        with online.create_online_device(self.device) as onlinedevice:
            if not onlinedevice.connected:
                onlinedevice.connect()
            if not isinstance(recursive, bool):
                recursive = literal_eval(recursive)
            CodesysCommandParser.__timed_printer(
                "Trying to delete folder: {}".format(remote_directory))
            onlinedevice.delete_directory(remote_directory, recursive)
            CodesysCommandParser.__timed_printer("Folder deleted.")
        return "Success"

    def get_file_list(self, remote_directory):
        """
        Get the file list of the given remote directory.

        *Arguments:*

        remote_directory (str): Path of the directory.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        with online.create_online_device(self.device) as onlinedevice:
            if not onlinedevice.connected:
                onlinedevice.connect()
            files = []
            CodesysCommandParser.__timed_printer(
                "Getting file list for directory {}.".format(remote_directory))
            file_list = onlinedevice.get_file_list_of_directory(
                remote_directory)
            for _file in file_list:
                files.append(_file.name)
        return "|".join(files)

    def get_installed_libraries(self, _filter=None):
        """
        Get installed libraries from CODESYS library manager.

        *Arguments:*

        _filter (str): Filter for libraries.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        ret_libs = []
        repo = librarymanager.repositories[0]
        libs = librarymanager.get_all_libraries(repo)
        for lib in libs:
            if _filter:
                if _filter in str(lib):
                    ret_libs.append(str(lib))
            else:
                ret_libs.append(str(lib))
        return "|".join(ret_libs)

    def install_library(self, library_path):
        """
        Installs the given library to repository 0 inside Codesys. Returns
        Success if successful.

        *Arguments:*

        library_path (str): Full directory path to the given library.

        *Returns:/

        (str): Success if successful, Command failed if not.
        """
        print(library_path)
        CodesysCommandParser.__timed_printer(
            "Setting {} library to repository 0.".format(library_path))
        repo = librarymanager.repositories[0]
        fails = 0
        if isinstance(library_path, list):
            for library in library_path:
                CodesysCommandParser.__timed_printer(
                    "Installing Library: {}".format(library))
                try:
                    librarymanager.install_library(library, repo, True)
                except Exception as e:
                    CodesysCommandParser.__timed_printer(
                        "Library install failed: {}".format(e))
                    fails += 1
        elif not library_path:
            CodesysCommandParser.__timed_printer(
                "No libraries given to install, continuing..")
        else:
            library = library_path
            CodesysCommandParser.__timed_printer(
                "Installing Library: {}".format(library))
            try:
                librarymanager.install_library(library, repo, True)
            except Exception as e:
                CodesysCommandParser.__timed_printer(
                    "Library install failed: {}".format(e))
                raise ValueError("Library install failed: {}".format(e))
        CodesysCommandParser.__timed_printer("Library installation complete.")
        if fails:
            raise ValueError(
                "Command failed: {} libraries not installed.".format(fails))
        return "Success"

    def uninstall_library(self, library_list):
        """
        Uninstalls the given library from repository 0 inside Codesys.
        Sends Success or Failure to the socket connection.

        *Arguments:*

        library_list (str): Full name of library to be uninstalled.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer(
            "Uninstalling {} from repository 0.".format(library_list))
        repo = librarymanager.repositories[0]
        if isinstance(library_list, list):
            for library in library_list:
                librarylib = librarymanager.get_library(library, repo)
                if librarylib:
                    CodesysCommandParser.__timed_printer(
                        "Uninstalling Library: {}".format(library))
                    librarymanager.uninstall_library(repo, librarylib)
                else:
                    CodesysCommandParser.__timed_printer(
                        "No library exists with given data.")
        elif not library_list:
            CodesysCommandParser.__timed_printer(
                "No libraries given to uninstall, continuing..")
        else:
            library = library_list
            librarylib = librarymanager.get_library(library, repo)
            if librarylib:
                librarymanager.uninstall_library(repo, librarylib)
                CodesysCommandParser.__timed_printer(
                    "Uninstalling Library: {}".format(library_list))
            else:
                CodesysCommandParser.__timed_printer(
                    "No library exists with given data.")
        CodesysCommandParser.__timed_printer(
            "Library uninstallation complete.")
        return "Success"

    def get_library_version(self, lib_name):
        """
        Gets the version of the given library from the current repository.
        Sends full library name to socket connection.

        *Arguments:*

        lib_name (str): Name of the library to be searched.

        *Returns:*

        library_string (str): Full name of the library.
        """
        if not lib_name:
            return "No Library"
        library_list = []
        libraries = librarymanager.get_all_libraries()
        for library in libraries:
            if lib_name in str(library):
                library_list.append(str(library))
        library_string = "|".join(library_list)
        return library_string

    def create_gateway(self, gateway_name, address, port, driver, guid):
        """
        Creates a new gateway with the given name, address, port, driver and guid.

        *Arguments:*

        gateway (str): Gateway name.
        address (str): Address for gateway.
        port (str): Port for gateway.
        driver (str): Driver for gateway, default is TCP/IP if None given.
        guid (str): Id for gateway, new will be generated if None given.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer(
            "Creating gateway with following Args:")
        CodesysCommandParser.__timed_printer("Name: {}".format(gateway_name))
        CodesysCommandParser.__timed_printer("Address: {}".format(address))
        CodesysCommandParser.__timed_printer("Port: {}".format(port))
        CodesysCommandParser.__timed_printer("Driver: {}".format(driver))
        CodesysCommandParser.__timed_printer("Guid: {}".format(guid))
        param_dict = {
            'IP-Address': '{}'.format(address),
            'Port': '{}'.format(port)}
        if driver == "None":
            driver = None
        if guid == "None":
            guid = None
        online.gateways.add_new_gateway(gateway_name, param_dict, driver, guid)
        CodesysCommandParser.__timed_printer("New gateway created.")
        return "Success"

    def remove_gateway(self, gateway_name):
        """
        Removes a gateway with the given name.

        *Arguments:*

        gateway (str): Gateway name.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer(
            "Removing given gateway: {}".format(gateway_name))
        online.gateways.remove_gateway(online.gateways[gateway_name])
        CodesysCommandParser.__timed_printer("Gateway removed.")
        return "Success"

    def set_gateway(self, gateway_name):
        """
        Sets the given gateway_name as the current gateway in use. Creates a
        gateway object. Returns Success if successful.

        *Arguments:*

        gateway_name (str): The name of the gateway to be used.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer(
            "Setting gateway to {}.".format(gateway_name))
        try:
            self.gateway = online.gateways[gateway_name]
        except BaseException:
            return "Command failed: Given gateway does not exist."
        CodesysCommandParser.__timed_printer("Gateway set.")
        return "Success"

    def get_gateways(self):
        """Get all current gateways.

        *Returns:*

        ret_string (str): String with gateways divided by |.
        """
        ret_gateways = []
        for gateway in online.gateways:
            ret_gateways.append(gateway.name)
        ret_string = "|".join(ret_gateways)
        return ret_string

    def perform_scan(self):
        """
        Performs network scan in the gateway. Creates a scan result object.
        Uses the gateway object. Returns addresses if successful.

        *Returns:*

        addresses (str): All found addresses.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer("Performing network scan..")
        if not self.gateway:
            return "Command failed: No gateway set."
        self.scan_res = self.gateway.perform_network_scan()
        addresses = []
        for res in self.scan_res:
            addresses.append(res.address)
        addresses = " ".join(addresses)
        CodesysCommandParser.__timed_printer("Network scan completed.")
        return addresses

    def set_address_by_ip(self, ip):
        """
        Searches for devices with the given IP address and sets the found address of the device inside the project.
        Creates a address string. Returns Success if successful.

        *Arguments:*

        ip (str): IP address of the device to be searched.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        try:
            self.address = None
            CodesysCommandParser.__timed_printer(
                "Searching for address with ip: {}".format(ip))
            hex_addr = self._ip_to_device_hex(ip).upper()
            self.address = self.gateway.find_address_by_ip(ip)
            CodesysCommandParser.__timed_printer(
                "Address found {}.".format(self.address))
            if not self.address:
                return "Command failed: No address set."
            if hex_addr not in self.address:
                self.address = None
                return "Command failed: Found address not correct."
        except AttributeError:
            return "Command failed: No gateway set."
        except Exception as e:
            CodesysCommandParser.__timed_printer("Error: {}".format(e))
            CodesysCommandParser.__timed_printer(
                "Address not found as IP, trying normal scan and as device address. (IP HEX ENDING)")
            convert = self._ip_to_device_hex(ip)
            addresses = self.perform_scan().split(" ")
            for addr in addresses:
                if addr == ip or addr.endswith(convert):
                    self.set_address(addresses.index(addr))
                    break
            CodesysCommandParser.__timed_printer(
                "Address set to {}.".format(self.address))
            CodesysCommandParser.__timed_printer(
                "Setting gateway and address..")
        return "Success"

    def set_address(self, id_):
        """
        Sets the address from the scan result list. Returns Success if successful.

        *Arguments:*

        id (int): The index of the address from the scan list.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        if not self.scan_res:
            return "Command failed: No scan result available. Please use scan first."
        id_ = int(id_)
        CodesysCommandParser.__timed_printer(
            "Setting address from list with id: {}".format(id_))
        try:
            self.address = self.scan_res[id_].address
            CodesysCommandParser.__timed_printer(
                "Address set: {}".format(self.address))
        except IndexError:
            return "Command failed: Given index out of scan range."
        return "Success"

    def set_gateway_and_address_to_device(self):
        """
        Sets the gateway and address to be the current gateway and address to the device in the project.
        Requires device, gateway and address to be set to work. Returns Success if successful.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        if not self.device:
            return "Command failed: No device is set."
        if not self.gateway:
            return "Command failed: Gateway not set."
        if not self.address:
            return "Command failed: Address not set."
        CodesysCommandParser.__timed_printer(
            "Setting gateway and address to device.")
        self.device.set_gateway_and_address(self.gateway, self.address)
        CodesysCommandParser.__timed_printer(
            "Gateway and address set successfully.")
        return "Success"

    def _ip_to_device_hex(self, ip):
        """
        Convert given IP address to device address hex value.

        *Arguments:*

        ip (str): IP Address in normal format.

        *Returns:*

        address (str): IP Address in device address hex format.
        """
        hex_pattern = r'^[0-9A-Fa-f]+$'
        # Use re.match to check if the string matches the pattern from the beginning to the end.
        is_hexadecimal = bool(re.match(hex_pattern, ip))

        if is_hexadecimal:
            CodesysCommandParser.__timed_printer(
                "{} is already in hexadecimal format.".format(ip))
            return ip
        address_conversion = re.findall("\\d+", ip)
        address = ip
        if len(address_conversion) == 4:
            address_hex = hex(int(address_conversion[3])).strip("0x")
            address = "{}".format(address_hex)
            CodesysCommandParser.__timed_printer(
                "Converting {} to {}.".format(ip, address))
        return address

    def full_config(self, project, dev, version, gateway_name, ip):
        """
        Initiates a full configuration procedure beginning from project
        opening and ending up with a running online application in the device.
        Creates proj, onlineapp, gateway and address objects. Returns Success
        if successful.

        *Arguments:*

        project (str): Full directory path to the project.
        dev (str): Device name inside the project.
        version (str): Device description version.
        gateway_name (str): Name of the gateway to be used.
        ip (str): IP address of the device.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer(
            "Initiating full config procedure..")
        self.init_api_data()
        if not (project and dev and version and gateway_name and ip):
            return "Command failed: Arguments missing or empty."
        if not self.proj or self.proj.path != project:
            self.open_project(project)
        if not self.proj:
            return "Command failed: No project set."
        self.find_and_update_device(dev, version)
        if not self.device:
            return "Command failed: No device set."
        self.set_gateway(gateway_name)
        if not self.gateway:
            return "Command failed: Given gateway not found."
        self.set_address_by_ip(ip)
        if not self.address:
            return "Command failed: Given device address was not found as an IP or as an HW address."
        self.set_gateway_and_address_to_device()
        self.clean_app(True)
        self.login()
        CodesysCommandParser.__timed_printer("Application logged in.")
        res = self.start_app()
        return res

    def write_value(self, variable, value, force=False, check=True, check_running_app=True):
        """
        Write a value to a variable in the current online application.
        Requires online application to be logged in and running in the device.
        Returns Success if successful.

        *Arguments:*

        variable (str): The name of the variable to be written inside the current project.
        value (str): The value to be set to the variable.

        *Returns:*
            (str): Success if successful, Command failed if not.
        """
        # Convert 0x to CODESYS hexadecimal value.
        if "0x" in value:
            value = value.replace("0x", "16#").upper()
        # Convert 0b to CODESYS binary value.
        if "0b" in value:
            value = value.replace("0b", "2#")
        CodesysCommandParser.__timed_printer(
            "Writing {} to {}.".format(value, variable))
        with online.create_online_application(self.app) as onlineapp:
            if not onlineapp.is_logged_in:
                return "Command failed: Application is not logged in."
            if check_running_app:
                if not onlineapp.application_state == ApplicationState.run:
                    return "Command failed: Application is not running."
            for _ in range(10):
                try:
                    onlineapp.set_prepared_value(variable, value)
                except Exception as e:
                    return "Command failed: Invalid value given: {}".format(e)
                if force:
                    onlineapp.force_prepared_values()
                if onlineapp.is_logged_in:
                    onlineapp.write_prepared_values()
                    if check:
                        system.delay(200)
                        ret = self.__remove_datatypes(
                            self.read_value(variable))
                        if ret.isnumeric():
                            hex_ret = hex(int(ret)).upper()
                            bin_ret = bin(int(ret)).upper()
                        test_value = CodesysCommandParser.__value_converter(
                            value)
                        if test_value in ret or test_value in hex_ret or test_value in bin_ret:
                            CodesysCommandParser.__timed_printer(
                                "Writing completed.")
                            return "Success"
                    else:
                        CodesysCommandParser.__timed_printer(
                            "Writing completed.")
                        system.delay(200)
                        return "Success"
                else:
                    return "Command failed: Application not logged in."

        return "Command failed: Wanted value: {}, current value after 10 tries {}".format(
            test_value, ret)

    def read_value(self, variable, check_running_app=True):
        """
        Read a value from a variable in the current open project. Requires online application to be logged in and running in the device.
        Sends the variable value or Failure to the socket.

        *Arguments:*

        variable (str): The name of the variable to be read inside the current project.

        *Returns:*

        (str): Variable value.
        """
        with online.create_online_application(self.app) as onlineapp:
            CodesysCommandParser.__timed_printer(
                "Reading value from {}.".format(variable))
            if onlineapp.is_logged_in:
                # Read once to ensure value is updated.
                if check_running_app:
                    if not onlineapp.application_state == ApplicationState.run:
                        return "Command failed: Application is not running."
                onlineapp.read_value(variable)
                return onlineapp.read_value(variable)

            self.login_no_return()
            # Read once to ensure value is updated.
            onlineapp.read_value(variable)
            return onlineapp.read_value(variable)

    def unforce_values(self):
        """
        Unforce all forced values.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer("Unforcing all values.")
        with online.create_online_application(self.app) as onlineapp:
            if not onlineapp.is_logged_in:
                return "Command failed: Application is not logged in."
            onlineapp.unforce_all_values()

    def cold_reset(self):
        """
        Initiates a cold reset in the device.
        Returns Success if successful.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer("Initiating cold reset.")
        with online.create_online_application(self.app) as onlineapp:
            if not onlineapp.is_logged_in:
                return "Command failed: Application is not logged in."
            onlineapp.reset(reset_option=ResetOption.Cold, force_kill=True)
            system.delay(200)
        return "Success"

    def warm_reset(self):
        """
        Initiates a warm reset in the device.
        Returns Success if successful.

        *Returns:*
            (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer("Initiating warm reset.")
        with online.create_online_application(self.app) as onlineapp:
            if not onlineapp.is_logged_in:
                return "Command failed: Application is not logged in."
            onlineapp.reset(reset_option=ResetOption.Warm, force_kill=True)
            system.delay(200)
        return "Success"

    def origin_reset(self):
        """
        Initiates a original reset in the device.
        Returns Success if
        successful.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer("Initiating origin reset.")
        with online.create_online_application(self.app) as onlineapp:
            if not onlineapp.is_logged_in:
                return "Command failed: Application is not logged in."
            onlineapp.reset(
                reset_option=ResetOption.Original, force_kill=True)
            system.delay(200)
        return "Success"

    def login(self):
        """
        Logs in the current online application to the device.
        Returns Success if successful.

        *Returns:*

        *Arguments:*(str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer("Logging in application.")
        with online.create_online_application(self.app) as onlineapp:
            for _ in range(10):
                if onlineapp.is_logged_in:
                    return "Success"

                onlineapp.login(OnlineChangeOption.Try, True)
                continue
        return "Command failed: Login not successful after 10 tries."

    def login_no_return(self):
        """
        Logs in the current online application to the device.
        """
        CodesysCommandParser.__timed_printer("Logging in application.")
        with online.create_online_application(self.app) as onlineapp:
            for _ in range(10):
                if onlineapp.is_logged_in:
                    return

                system.delay(200)
                onlineapp.login(OnlineChangeOption.Try, True)
                continue

    def logout(self):
        """
        Logs out the current online application from the device.
        Returns Success if successful.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        with online.create_online_application(self.app) as onlineapp:
            if onlineapp.is_logged_in:
                CodesysCommandParser.__timed_printer(
                    "Logging out application.")
                onlineapp.logout()
            if not onlineapp.is_logged_in:
                CodesysCommandParser.__timed_printer("Device logged out.")
                return "Success"

    def start_app(self):
        """
        Starts the currently logged in online application.
        Returns Success if successful.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer("Starting application..")
        with online.create_online_application(self.app) as onlineapp:
            if not onlineapp.is_logged_in:
                return "Command failed: Application is not logged in."
            for _ in range(10):
                if not onlineapp.application_state == ApplicationState.run:
                    onlineapp.start()
                    CodesysCommandParser.__timed_printer(
                        "Application started.")
                system.delay(200)
                if onlineapp.application_state == ApplicationState.run:
                    self.appstate = onlineapp.application_state
                    return "Success"

                system.delay(1000)
                continue
            return "Command failed: Application start failed."

    def stop_app(self):
        """
        Stops the currently logged in online application.
        Returns Success if successful.

        *Returns:*

        (str): Success if successful, Command failed if not.
        """
        CodesysCommandParser.__timed_printer("Stopping application..")
        with online.create_online_application(self.app) as onlineapp:
            if not onlineapp.is_logged_in:
                return "Command failed: Application is not logged in."
            onlineapp.stop()
            CodesysCommandParser.__timed_printer("Application stopped.")
            if onlineapp.application_state != ApplicationState.run:
                self.appstate = onlineapp.application_state
                system.delay(200)
                return "Success"
            return "Command failed: Application stop failed."

    def find_used_libraries(self, _filter=None):
        """
        Find all the libraries from the current project and their dependencies.

        *Arguments:*

         _filter (str): Filter for library output.

        *Returns:*

        (str): Set converted into a string divided by |.
        """
        proj = self.proj
        if not proj:
            proj = projects.primary
        if not proj:
            return "Command failed: No project open."
        libraries = []
        CodesysCommandParser.__timed_printer(
            "Getting all children of project.")
        objects = proj.get_children(recursive=True)
        CodesysCommandParser.__timed_printer(
            "Looping through library manager content.")
        dependencies = []
        for candidate in filter(
                lambda cand_name: cand_name if cand_name.is_libman else None,
                objects):
            for libref in filter(
                    lambda lib: lib if lib.is_placeholder else None,
                    iter(candidate)):
                if libref.is_placeholder:
                    if _filter and _filter not in libref.name:
                        continue
                    dependencies += libref.get_dependencies()
                    if libref.effective_resolution:
                        libraries.append(libref.effective_resolution)
                    else:
                        libraries.append(libref.default_resolution)
        # Use a set to remove duplicates
        for dependency in dependencies:
            if _filter and _filter not in dependency.name:
                continue
            if hasattr(dependency, "effective_resolution") and dependency.effective_resolution:
                libraries.append(dependency.effective_resolution)
            elif hasattr(dependency, "default_resolution") and dependency.default_resolution:
                libraries.append(dependency.default_resolution)
        libraries_set = set(libraries)
        return "|".join(libraries_set)

    def find_missing_libraries(self):
        """
        Find all the libraries from the current project that are not yet imported.

        *Returns:*

        missing (list): List with missing libraries.
        """
        proj = self.proj
        if not proj:
            proj = projects.primary
        if not proj:
            return "Command failed: No project open."
        missing = []
        CodesysCommandParser.__timed_printer(
            "Getting all children of project.")
        objects = proj.get_children(recursive=True)
        dependencies = []
        CodesysCommandParser.__timed_printer(
            "Looping through library manager content.")
        for candidate in filter(
                lambda cand_name: cand_name if cand_name.is_libman else None,
                objects):
            for libref in filter(
                    lambda lib: lib if lib.is_placeholder else None,
                    iter(candidate)):
                try:
                    if libref.is_placeholder:
                        if libref.effective_resolution is not None:
                            libInfo = str(libref.effective_resolution)
                            libMissing = False
                            dependencies += libref.get_dependencies()
                        elif libref.default_resolution is not None:
                            print(libref.default_resolution)
                            libInfo = str(libref.default_resolution)
                            CodesysCommandParser.__timed_printer(
                                "{} is a missing library.".format(libInfo))
                            libMissing = True
                        if libMissing:
                            missing.append(libInfo)
                    elif libref.is_managed:
                        libInfo = str(libref.managed_library)
                    else:
                        libInfo = str(libref.name)
                except Exception as e:
                    CodesysCommandParser.__timed_printer(e)
                    missing.append(libref.name)

        for dependency in dependencies:
            if hasattr(dependency, "effective_resolution") and dependency.effective_resolution:
                continue
            if hasattr(dependency, "default_resolution") and dependency.default_resolution:
                libInfo = str(dependency.default_resolution)
                missing.append(libInfo)
                CodesysCommandParser.__timed_printer(
                    "{} is a missing dependency.".format(libInfo))
        if len(missing) == 0:
            return ""

        # Remove duplicates
        missing = set(missing)
        return "|".join(missing)

    def __install_library_url(self, url, librarymanager):
        """
        Download given URL and install the library.

        *Arguments:*

        url (str): URL to download library from.
        librarymanager (obj): Librarymanager object from Codesys.
        """
        if not url.startswith("http"):
            return

        downloaddir = os.path.join(os.environ["USERPROFILE"], "downloads")
        if not os.path.exists(downloaddir):
            os.makedirs(downloaddir)
        basename, extension = os.path.splitext(url)
        localname = os.path.join(downloaddir, "dl" + extension)
        self.__timed_printer("Downloading {} to {}\n".format(url, localname))

        web_client = WebClient()
        web_client.DownloadFile(url, localname)
        repo = librarymanager.repositories[0]
        self.__timed_printer("Installing {}\n".format(url))
        librarymanager.install_library(localname, repo, True)

    def __create_download_link(self, libInfo):
        """
        Create and test download link.
        """

        m = re.findall('([^,]+), ([^(]+) \\(([^)]+)\\)', libInfo)
        urls = []
        print(m)
        if len(m) > 0:
            libname, libversion, libvendor = m[0]
            if libversion == "*":
                libversions = ["3.5.15.0", "3.5.16.0", "3.5.17.0"]
            else:
                libversions = [libversion]
            for libversion in libversions:
                indexurl = "https://store.codesys.com/CODESYSLibs/%s/%s/%s/index" % (
                    libvendor, libname, libversion)
                web_client = WebClient()
                try:
                    filename = web_client.DownloadString(indexurl).rstrip()
                except Exception as e:
                    self.__timed_printer(
                        "The given library not found with URL: {}".format(libname))
                    self.__timed_printer("Error: {}".format(e))
                    filename = None

                if filename is not None:
                    liburl = "https://store.codesys.com/CODESYSLibs/%s/%s/%s/%s" % (
                        libvendor, libname, libversion, filename)
                    urls.append(liburl)
                else:
                    continue
        if urls:
            return urls
        return ""

    def download_missing_libs(self):
        """
        Tries to download all missing libraries that exist in CODESYS store to current open project.

        *Returns:*

        (str): Success if successful, command failed otherwise.
        """
        # Check for missing libraries
        if self.proj:
            proj = self.proj
        else:
            return "Command failed: No project open."
        # search for libman
        install_urls = []
        objects = proj.get_children(recursive=True)
        for object_ in objects:
            if object_.is_libman:
                for libref in iter(object_):
                    if libref.is_placeholder:
                        # Dependencies
                        for dependency in libref.get_dependencies():
                            if dependency.is_placeholder:
                                if dependency.effective_resolution is None:
                                    if dependency.default_resolution is not None:
                                        liburls = self.__create_download_link(
                                            str(dependency.default_resolution))
                                        if liburls:
                                            for liburl in liburls:
                                                if liburl not in install_urls:
                                                    install_urls.append(liburl)
                        # Initial Library
                        if libref.effective_resolution is None and libref.default_resolution is not None:
                            libInfo = str(libref.default_resolution)
                            liburls = self.__create_download_link(libInfo)
                            if liburls:
                                for liburl in liburls:
                                    if liburl not in install_urls:
                                        install_urls.append(liburl)

        other_libs = self.find_missing_libraries()
        print(other_libs)
        for lib in other_libs.split("|"):
            liburls = self.__create_download_link(lib)
            if liburls:
                for liburl in liburls:
                    if liburl not in install_urls:
                        install_urls.append(liburl)
        for url in install_urls:
            self.__install_library_url(url, librarymanager)

        return "Success"

    def shutdown_server(self):
        """
        Return Success and shutdown running server in Codesys.

        *Returns:*

        (str): Success if successful.
        """
        return "Success"

    def shutdown_codesys(self):
        """
        Return Success and shutdown Codesys instance.

        *Returns:*

        (str): Success if successful.
        """
        return "Success"

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
        return "Success"

    def change_task_cyclic_interval(self, task_name, interval):
        """
        Change the cyclic interval of the given task name.
        NOT POSSIBLE WHEN DEVICE IS ONLINE

        *Arguments:*

        task_name (str): Name of the task, for example MainTask.
        interval (str): Interval of the task, for example 10.
        """
        result_list = projects.primary.find(task_name, True)
        result = result_list[0]
        result.interval = interval
        return "Success"


class CodesysTCPHandler(SocketServer.BaseRequestHandler):
    """
    CodesysTCPHandler class for Codesys control.
    """
    shutdown = False
    restart = False
    commander = CodesysCommandParser()

    @staticmethod
    def __timed_printer(data):
        """
        Just a print function that adds current time to print.

        *Arguments:*

        data (str): The string to print with a timestamp.
        """
        time = datetime.now().strftime("%H:%M:%S")
        print("[ {} ] - {}".format(time, data))

    def handle(self):
        """
        The main handler function for incoming data.
        Parses the data for commands and variables and executes them inside Codesys.
        """
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(65536).strip().decode()
        try:
            ret = CodesysTCPHandler.commander.handle_request(self.data)
            if "shutdown_server" in ret and "Success" in ret:
                CodesysTCPHandler.shutdown = True
            if "restart_server" in ret and "Success" in ret:
                CodesysTCPHandler.shutdown = True
                CodesysTCPHandler.restart = True
            self.request.sendall(ret.encode())
            if "shutdown_codesys" in ret and "Success" in ret:
                system.exit()
        except Exception as e:
            CodesysTCPHandler.__timed_printer(e)
            self.request.sendall("Command failed: {}".format(e))


def start_server(host, port):
    """
    Start server and handle requests.

    *Arguments:*

    host (str): Host address for server.
    port (int): Port for server.
    """
    CodesysTCPHandler.restart = False
    CodesysTCPHandler.shutdown = False
    server = SocketServer.TCPServer((host, port), CodesysTCPHandler)
    print("CODESYS READY")
    # Handles requests until shutdown variable is set to True
    while not CodesysTCPHandler.shutdown:
        server.handle_request()
    server.server_close()


if __name__ == "__main__":
    # Starts a socketserver inside Codesys with the given HOST and PORT arguments.
    try:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
    except BaseException:
        HOST = "localhost"
        PORT = 9000
    start_server(HOST, PORT)
    while CodesysTCPHandler.restart:
        start_server(HOST, PORT)
