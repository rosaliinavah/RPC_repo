"""This file implements class which acts as an API towards Codesys using RPC API.
"""
from ast import literal_eval
from functools import wraps
from robot.libraries.Remote import Remote
from robot.api import logger


def require_remote(func):
    """
    Decorator to ensure that remote connection exists before calls are done.
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.remote is None:
            raise RuntimeError(
                f"Remote connection not yet initialized, unable to execute {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper


class codesys_rpc_client:
    """Interface class to control Codesys through RPC protocol
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    RET_TYPES = {
        "bin": bin,
        "hex": hex,
        "int": int,
        "float": float,
        "bool": bool
    }

    def __init__(self, uri=None, timeout=None):
        self.timeout = timeout
        self.uri = uri
        self.remote = None

    def __parse_datatypes(self, value: str, ret_type: str | None):
        """Removes datatype from return value.
        For example BYTE#, INT#, etc.
        Additionally can convert return value into int/float/bin/hex/bool

        *Arguments:*

        data (str): Initial data string.
        ret_type (str): Changes the return type based on given.

        *Returns:*

        (str): Parsed data.
        """
        # pattern = r'^\w+#'
        # value = re.sub(pattern, '', value)
        if not ret_type:
            return value
        elif ret_type in ["bin", "hex", "int", "float"]:
            value = int(value)
            value = self.RET_TYPES[ret_type](value)
        elif ret_type == "bool":
            if value.isnumeric():
                value = int(value)
            else:
                value = "TRUE" == value.upper()
            value = self.RET_TYPES[ret_type](value)
        return value

    def connect(self):
        """
        Connects to RPC server
        """
        if not self.uri:
            raise ValueError("Server URI must be set before connecting.")

        logger.debug(
            f"If a timeout ({self.timeout}) is specified, use it when creating the Remote instance")
        self.remote = Remote(
            self.uri, timeout=self.timeout) if self.timeout else Remote(self.uri)

    @require_remote
    def stop_remote_server(self):
        """
        Stops Codesys RPC remote server
        """
        args = ()
        kwargs = {}
        self.remote.run_keyword("stop_remote_server", args, kwargs)
        self.remote = None

    @require_remote
    def set_communication_parameters(self, device_ip: str = "", device_name: str = "", gateway_name: str = 'Gateway-1'):
        """
        Sets communication parameters for communication between CODESYS and the device where application should run.

        *Arguments:*

        :param device_ip(str): IP-address of the device. No need to pass if communication settings are saved into the codesys project
        :param device_name(str): Name of the device. No need to pass if communication settings are already saved into the codesys project.
        :param gateway_name(str): Name of the gateway used in communication. Gateway-1 as default.
        """
        logger.info(
            f"Device IP:{device_ip}, Device Name:{device_name}, Gateway:{gateway_name}")
        # Convert to tuple
        args = (device_ip, device_name, gateway_name)
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("set_communication_parameters", args, kwargs)

    @require_remote
    def perform_network_scan(self):
        """
        Performs a network scan on this gateway
        """
        # Convert to tuple
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("perform_network_scan", args, kwargs)

    @require_remote
    def get_project(self):
        """
        Get currently opened project.
        """
        args = ()
        kwargs = {}
        return self.remote.run_keyword("get_project", args, kwargs)

    def is_connected(self):
        """
        Check if client is currently connected to a server
        """
        if self.remote:
            return True
        return False

    @require_remote
    def login(self):
        """
        Performs application login and downloads the source archive to the device.
        """
        # Convert to tuple
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("login", args, kwargs)

    @require_remote
    def login_without_download(self):
        """
        Performs application login.
        """
        # Convert to tuple
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("login_without_download", args, kwargs)

    @require_remote
    def logout(self):
        """
        Performs application logout
        """
        # Convert to tuple
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("logout", args, kwargs)

    @require_remote
    def start_app(self):
        """
        Starts the application.
        """
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("start_app", args, kwargs)

    @require_remote
    def stop_app(self):
        """
        Stops the application running.
        """
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("stop_app", args, kwargs)

    @require_remote
    def read_variables(self, *variables, ret_type: str | None = None):
        """
        Reads the values variables given as an argument.

        *Arguments:*

        :param variables: indeterminable number of variable names as separate arguments.
        :param ret_type: defines return type for values, See: RET_TYPES

        *Returns:*

        (dict): Dictionary of variables and their values.
        """
        try:
            args = variables
            kwargs = {}
            # Call remote server using RPC API
            ret_val = self.remote.run_keyword("read_variables", args, kwargs)
            logger.info(f"Ret val:{ret_val}")
            # Loop all items from dict
            for key, val in ret_val.items():
                logger.info(f"Key:{key}, value:{val}")
                # Parse datatype based on the argument
                value_tmp = self.__parse_datatypes(
                    value=val, ret_type=ret_type)
                # Overwrite value with new datatype
                ret_val[key] = value_tmp
            return ret_val
        except Exception as ex:
            raise Exception(f"Read variables failed, exception:{ex}") from ex

    @require_remote
    def read_variable(self, variable: str, ret_type: str | None = None):
        """
        Reads the variable value for the given argument.

        *Arguments:*

        variables (str): One variable name as str.
        ret_type (str): Defines return type for values, See: RET_TYPES

        *Returns:*

        (Any): The variable value.
        """
        try:
            args = (variable,)
            kwargs = {}
            # Call remote server using RPC API
            value = self.remote.run_keyword("read_variable", args, kwargs)
            logger.info(f"Variable:{variable}")
            logger.info(f"Value:{value}")
            # Parse datatype based on the argument
            value = self.__parse_datatypes(value=value, ret_type=ret_type)
            return value
        except Exception as ex:
            raise Exception(f"Reading value failed, exception:{ex}") from ex

    @require_remote
    def write_variables(self, **variables_and_values):
        """
        Sets the values of given variables to desired values.

        *Arguments:*

        variables_and_values (dict [key,val]): indeterminable number of variables and their desired values as key-value pairs.
        """
        try:
            for key, val in variables_and_values.items():
                # Value is in hex format
                if val.startswith("0x"):
                    # Convert hex to dec
                    variables_and_values[key] = str(literal_eval(val))
                # Value is in binary format
                elif val.startswith("0b"):
                    # Remove empty spaces if format is 1111 0000
                    val = val.replace(" ", "")
                    # Convert bin to dec
                    variables_and_values[key] = str(int(val, 2))
                # Value in Codesys format
                elif val.startswith("2#") or val.startswith("16#"):
                    # Don't convert, use as is
                    variables_and_values[key] = val
                # Value assumable in dec format
                else:
                    # Don't convert, use as is
                    variables_and_values[key] = val

            logger.debug(f"Variables and values:{variables_and_values}")
            args = ()
            kwargs = variables_and_values
            # Call remote server using RPC API
            self.remote.run_keyword("write_variables", args, kwargs)
        except Exception as ex:
            raise Exception(f"Write variables failed, exception:{ex}") from ex

    @require_remote
    def write_variable(self, variable: str, value: str):
        """
        Set the value of given variable to desired value.

        *Arguments:*

        variable (str): variable to be written.
        value (str): value to be written.
        """
        try:
            value_tmp = ""
            # Value is in hex format
            if value.startswith("0x"):
                # Convert hex to dec
                value_tmp = str(literal_eval(value))
            # Value is in binary format
            elif value.startswith("0b"):
                # Convert bin to dec
                value_tmp = str(int(value, 2))
            # Value in Codesys format
            elif value.startswith("2#") or value.startswith("16#"):
                # Don't convert, use as is
                value_tmp = value
            # Value assumable in dec format
            else:
                # Don't convert, use as is
                value_tmp = value

            logger.debug(f"Variable{variable} and value:{value_tmp}")
            args = (variable, value_tmp)
            kwargs = {}
            # Call remote server using RPC API
            self.remote.run_keyword("write_variable", args, kwargs)
        except Exception as ex:
            raise Exception(f"Write variable failed, ex:{ex}") from ex

    @require_remote
    def enter_debug_mode(self):
        """
        Enters debug mode.
        """
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("enter_debug_mode", args, kwargs)

    @require_remote
    def force_values(self, **variables_and_values: dict[str, str]):
        """
        Forces the values of given variables to desired values.

        *Arguments:*

        variables_and_values (dict [str,str]): indeterminable number of variables and their desired values as key-value pairs.
        """
        logger.debug(f"Variables and values:{variables_and_values}")
        args = ()
        kwargs = variables_and_values
        self.remote.run_keyword("force_values", args, kwargs)

    @require_remote
    def unforce_values(self):
        """
        Unforce all forced variables
        """
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("unforce_values", args, kwargs)

    @require_remote
    def open_project(self, project_path: str):
        """
        Opens the project.
        Sets default credentials.
        Cleans application build and creates online application.

        *Arguments:*

        project_path (str): Path to the Codesys project.
        """
        logger.debug(f"Project path:{project_path}")
        # Convert to tuple
        args = (project_path,)
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("open_project", args, kwargs)

    @require_remote
    def close_project(self):
        """
        Closes the active project
        """
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("close_project", args, kwargs)

    @require_remote
    def reset_warm(self):
        """
        Executes reset warm
        """
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("reset_warm", args, kwargs)

    @require_remote
    def reset_cold(self):
        """
        Executes reset cold
        """
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("reset_cold", args, kwargs)

    @require_remote
    def reset_original(self):
        """
        Executes reset original
        """
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("reset_original", args, kwargs)

    @require_remote
    def scan_network(self):
        """
        Scans Devices from Gateway-1
        """
        args = ()
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("scan_network", args, kwargs)

    @require_remote
    def set_default_credentials(self, username, password):
        """
        Set the default credentials for current CODESYS instance.

        *Arguments:*

        username (str): Username for the user manager of current device.
        password (str): Password for the user manager of current device.
        """
        args = (username, password)
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("set_default_credentials", args, kwargs)

    @require_remote
    def add_new_gateway(self, name='Gateway-1', port=1217, ip_addr='localhost'):
        """
        Adds new gateway to communication settings of Codesys

        *Arguments:*

        :param name: name of the new gateway, Gateway-1 as default.
        :param port: port number of the new gateway, 1217 as default.
        :param ip_addr: Ip-address of the gateway, localhost as default
        """
        args = (name, port, ip_addr)
        kwargs = {}
        # Call remote server using RPC API
        self.remote.run_keyword("add_new_gateway", args, kwargs)

    @require_remote
    def find_gateway(self, name='Gateway-1'):
        """
        Finds a gateway by given name

        *Arguments:*

        :param name: name of the new gateway, Gateway-1 as default.
        """
        args = (name,)
        kwargs = {}
        # Call remote server using RPC API
        return self.remote.run_keyword("find_gateway", args, kwargs)
