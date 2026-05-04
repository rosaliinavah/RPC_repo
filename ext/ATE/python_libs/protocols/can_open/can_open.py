"""
File which implements can_open class to communicate with EPEC device using CANopen protocol.
"""
import struct
import time
from enum import Enum
import datetime
import canopen


class can_bitrate(Enum):
    """
    Enumerations for CANOpen bitrate speeds
    """
    CAN_BITRATE_50K = 50000
    CAN_BITRATE_125K = 125000
    CAN_BITRATE_250K = 250000
    CAN_BITRATE_500K = 500000
    # CAN_BITRATE_800K = 800000 # Not supported in python canlib library
    CAN_BITRATE_1000K = 1000000


class can_open:
    """
    A class for managing a CANopen node using the `canopen` Python library.

    This class allows for the connection to and control of a CANopen node,
    including setting its operational state and resetting the node or its communication.
    """
    FORMAT_CHARACTERS = {
        "BOOL": "?",
        "I8": "b",
        "I16": "h",
        "I32": "i",
        "U8": "B",
        "U16": "H",
        "U32": "I",
        "R32": "f",
        "STR": "s",
        "R64": "d",
        "I64": "q",
        "U64": "Q"
    }

    def __init__(self, bustype: str = None, channel: int = None, bitrate: int = None):
        self.bustype = bustype
        self.channel = channel
        self.bitrate = bitrate
        self.network = None
        self.boot_up_msg_received = False

    def connect(self, bustype: str = None, channel: int = None, bitrate: int = None):
        """
        Connect CANopen adapter

        *Arguments:*

        bustype (str): The type of bus used (e.g., 'kvaser', 'socketcan'). Defaults to 'kvaser'.
        channel (int): The channel or interface used for communication. Defaults to 0.
        bitrate (int): The bitrate for the CAN bus. Defaults to 250000.
        """

        # Overwrite args given in init
        if bustype is not None:
            self.bustype = bustype
        if channel is not None:
            self.channel = channel
        if bitrate is not None:
            self.bitrate = bitrate

        if self.bustype is None:
            raise ValueError("No bustype given.")
        if self.channel is None:
            raise ValueError("No channel given.")
        if self.bitrate is None:
            raise ValueError("No bitrate given.")

        self.network = canopen.Network()
        self.network.connect(bustype=self.bustype,
                             channel=self.channel, bitrate=self.bitrate)

    def disconnect(self):
        """
        Disconnect CANopen
        """
        self.network.sync.stop()
        self.network.disconnect()

    def scan_nodes(self):
        """
        Scans nodes 1 - 127

        *Returns:*

        (list): Node ids
        """
        self.network.scanner.search()
        # We may need to wait a short while here to allow all nodes to respond
        time.sleep(0.5)
        return self.network.scanner.nodes

    def reset_nodes(self):
        """
        Reset (remove) all nodes
        """
        self.network.scanner.reset()

    def disconnect_and_scan_all_bit_rates(self, bustype: str = None, channel: int = None):
        """
        Disconnects, clear nodes and scans CANOpen nodes 1 - 127 using using all bit rates

        *Returns:*

        (Dict): <bitrate, [node-id1, node-id2]>
        """
        ret_val = {}
        self.disconnect()

        for item in can_bitrate:
            print(f"Bitrate:{item.value}")
            self.connect(bustype=bustype, channel=channel, bitrate=item.value)
            time.sleep(0.5)
            nodes = self.scan_nodes()

            # Add nodes to dict if any
            if len(nodes) > 0:
                ret_val[item.value] = nodes

            self.disconnect()
            time.sleep(0.5)

        return ret_val

    def add_node(self, node_id: int = None, eds_file_path: str = None):
        """
        Add CANopen Node.

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.
        eds_file_path (str): The Electronic Data Sheet file for the node.
        """

        if self.network is None:
            raise ValueError(
                "CANOpen network not connected, please call connect before adding node.")
        if node_id is None:
            raise ValueError("No Node ID given.")

        # Load the node with the provided EDS file and node ID
        node = canopen.RemoteNode(node_id, eds_file_path)
        self.network.add_node(node)

    def nmt_set_operational(self, node_id: int = None):
        """
        Sets the CANopen node to the operational state.

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.
        """
        # No node id defined, send broadcast message
        if node_id is None:
            self.network.nmt.state = 'OPERATIONAL'
            return

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        # Send message to Node
        self.network.nodes[node_id].nmt.state = 'OPERATIONAL'

    def nmt_set_pre_operational(self, node_id: int = None):
        """
        Sets the CANopen node to the pre-operational state.

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.
        """
        # No node id defined, send broadcast message
        if node_id is None:
            self.network.nmt.state = 'PRE-OPERATIONAL'
            return

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        # Send message to Node
        self.network.nodes[node_id].nmt.state = 'PRE-OPERATIONAL'

    def nmt_set_stopped(self, node_id: int = None):
        """
        Sets the CANopen node to the stopped state.

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.
        """
        # No node id defined, send broadcast message
        if node_id is None:
            self.network.nmt.state = 'STOPPED'
            return

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        # Send message to Node
        self.network.nodes[node_id].nmt.state = 'STOPPED'

    def nmt_reset_node(self, node_id: int = None):
        """
        Resets the CANopen node.

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.
        """
        # No node id defined, send broadcast message
        if node_id is None:
            self.network.nmt.state = 'RESET'
            return

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        # Send message to Node
        self.network.nodes[node_id].nmt.state = 'RESET'

    def nmt_reset_communication(self, node_id: int = None):
        """
        Resets the communication for the CANopen node.

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.
        """
        # No node id defined, send broadcast message
        if node_id is None:
            self.network.nmt.state = 'RESET COMMUNICATION'
            return

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        # Send message to Node
        self.network.nodes[node_id].nmt.state = 'RESET COMMUNICATION'

    def nmt_get_operation_mode(self, node_id: int = None):
        """
        Retrieves the current operational state of the CANopen node.

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*
        (str): The current NMT state of the node.
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        return self.network.nodes[node_id].nmt.state

    def nmt_get_timestamp(self, node_id: int = None, epoch=False):
        """
        Gets NMT message timestamp of the CANOpen node.

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*
        (float): Timestamp as EPOCH.
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        epoch_time = self.network.nodes[node_id].nmt.timestamp

        if epoch is True:
            return epoch_time

        # Convert epoch to datetime object
        datetime_obj = datetime.datetime.fromtimestamp(epoch_time)
        # Format the datetime object
        return datetime_obj.strftime("%Y%m%d %H:%M:%S.%f")[:-3]

    def send_gfc_message(self):
        """
        Control unit is set in a safe state.

        Send GFC message (COB-ID 1h, DLC 0) to CAN bus.
        """
        if not self.network:
            raise ValueError("Can not initialized, network is None.")

        self.network.send_message(can_id=0x1, data=0)

    def get_device_type(self, node_id: int = None):
        """
        Describes the type of device and its functionality.

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*

        (int): Device type
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        return self.read_sdo_raw(node_id=node_id, index_name=0x1000, datatype='U32')

    def get_manufacturer_device_name(self, node_id: int = None):
        """
        Manufacturer Device Name

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*

        (str): Control unit name, e.g. SC52
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        return self.read_sdo_raw(node_id=node_id, index_name=0x1008, datatype='STR')

    def get_manufacturer_software_version(self, node_id: int = None):
        """
        Manufacturer Software Version

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*

        (str): Manufacturer Software Version
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        return self.read_sdo_raw(node_id=node_id, index_name=0x100A, datatype='STR')

    def get_vendor_id(self, node_id: int = None):
        """
        Gets Vendor ID from device.

        Index 1018h
        Sub 1: Vendor-ID

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*

        (int): Vendor-ID
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        return self.read_sdo_raw(
            node_id=node_id, index_name=0x1018, sub_name=1, datatype='U32')

    def get_product_code(self, node_id: int = None):
        """
        Gets Product Code from device.

        Index 1018h
        Sub 2: Product Code

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*

        (int): Product Code
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        return self.read_sdo_raw(
            node_id=node_id, index_name=0x1018, sub_name=2, datatype='U32')

    def get_revision_number(self, node_id: int = None):
        """
        Gets Revision Number from device.

        Index 1018h
        Sub 3: Revision Number

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*

        (int): Revision Number
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        return self.read_sdo_raw(
            node_id=node_id, index_name=0x1018, sub_name=3, datatype='U32')

    def get_serial_number(self, node_id: int = None):
        """
        Gets Serial Number from device.

        Index 1018h
        Sub 4: Serial Number

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*

        (int): Serial Number
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        return self.read_sdo_raw(
            node_id=node_id, index_name=0x1018, sub_name=4, datatype='U32')

    def save_all_parameters(self, node_id: int = None):
        """
        Save all parameters

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        Store parameters to non-volatile memory.
        Write = 65766173h, where (s = 73h, a = 61h, v = 76h, e = 65h)
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        try:
            orig_timeout = None
            node = self.network.nodes[node_id]
            # Get original timeout
            orig_timeout = node.sdo.RESPONSE_TIMEOUT
            # Set new timeout, 1s
            node.sdo.RESPONSE_TIMEOUT = 1
            self.write_sdo_raw(node_id=node_id, index_name=0x1010,
                               sub_name=1, data=b'save')
            # Restore original timeout
            node.sdo.RESPONSE_TIMEOUT = orig_timeout
        except Exception as ex:
            # Restore original timeout
            if orig_timeout is not None:
                node.sdo.RESPONSE_TIMEOUT = orig_timeout
            raise ex

    def restore_all_default_parameters(self, node_id: int = None):
        """
        Restore all parameters to default values

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        Restore default parameter values.
        Write = 64616F6Ch, where (l = 6Ch, o = 6Fh, a = 61h, d = 64h)
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        try:
            orig_timeout = None
            node = self.network.nodes[node_id]
            # Get original timeout
            orig_timeout = node.sdo.RESPONSE_TIMEOUT
            # Set new timeout, 1s
            node.sdo.RESPONSE_TIMEOUT = 1
            self.write_sdo_raw(node_id=node_id, index_name=0x1011,
                               sub_name=1, data=b'load')
            # Restore original timeout
            node.sdo.RESPONSE_TIMEOUT = orig_timeout

        except Exception as ex:
            # Restore original timeout
            if orig_timeout is not None:
                node.sdo.RESPONSE_TIMEOUT = orig_timeout
            raise ex

    def wait_boot_up_message(self, *node_ids: int, timeout: int = 5):
        """
        Waits boot up message from given node ids.

        *Arguments:*

        node_ids (*args): The identifier for the nodes on the CANopen network.
        timeout (int): Timeout in seconds
        """
        if len(node_ids) == 0:
            raise ValueError("No node ids given.")

        for node_id in node_ids:
            if self.network.nodes.get(node_id) is None:
                raise ValueError(
                    "No such node id, remember to add node using add_node method.")

        self.boot_up_msg_received = False

        for node_id in node_ids:
            # Subscribe to boot-up message for a specific node ID
            self.network.subscribe(
                0x700 + node_id, self._boot_up_message_callback)

        # Wait boot up message and raise exception if timeout exceeded.
        end_time = time.time() + timeout
        while True:
            now = time.time()
            if now > end_time:
                for node_id in node_ids:
                    self.network.unsubscribe(
                        0x700 + node_id, self._boot_up_message_callback)
                self.boot_up_msg_received = False
                raise RuntimeError(
                    "Timeout waiting for boot-up message")
            if self.boot_up_msg_received is True:
                for node_id in node_ids:
                    self.network.unsubscribe(
                        0x700 + node_id, self._boot_up_message_callback)
                return

    def _boot_up_message_callback(self, _can_id, _data, _timestamp):
        """
        Callback method for boot up message.
        """
        self.boot_up_msg_received = True

    def read_sdo(self, node_id: int, index_name: str, sub_name: str = None):
        """
        Reads a SDO message from the specified CANopen node.

        *Arguments:*

        node_id (int): The index of CAN node
        index_name (str): The index or name of the Object Dictionary to be read from.
        sub_name (str): The subindex or name of the Object Dictionary. Optional, defaults to None.

        *Returns:*

        (any): The data read from the SDO.
        """
        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        # Convert index_name and sub_name to their numeric representations if applicable
        index_name_converted = self._identify_and_convert(index_name)
        sub_name_converted = self._identify_and_convert(
            sub_name) if sub_name is not None else None

        node = self.network.nodes[node_id]

        # Access the canopen object depending on whether sub_name is provided
        if sub_name_converted is None:
            return node.sdo[index_name_converted].raw

        return node.sdo[index_name_converted][sub_name_converted].raw

    def write_sdo(self, node_id: int, index_name: str, data, sub_name: str = None):
        """
        Writes a SDO message to the specified CANopen node.

        *Arguments:*

        node_id (int): The index of the Object Dictionary to be read from.
        index_name (str): The index of the Object Dictionary to be read from.
        data (str): The data to be written to the Object Dictionary.
        sub_name (int): The subindex of the Object Dictionary. Optional, defaults to None.
        """
        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        # Convert index_name and sub_name to their numeric representations if applicable
        index_name_converted = self._identify_and_convert(index_name)
        sub_name_converted = self._identify_and_convert(
            sub_name) if sub_name is not None else None

        node = self.network.nodes[node_id]

        # Access the canopen object depending on whether sub_name is provided
        if sub_name_converted is None:
            node.sdo[index_name_converted].raw = data
            return

        node.sdo[index_name_converted][sub_name_converted].raw = data

    def read_sdo_raw(self, node_id: int, index_name: str, sub_name: str = 0, datatype: str = None):
        """
        Reads a SDO message to the specified CANopen node.

        *Supported datatypes are:*

        "BOOL", "I8", "I16", "I32", "I64", "U8", "U16", "U32", "U64",
        "R32", "R64", and "STR".

        *Arguments:*

        node_id (int): The index of CAN node
        index_name (str): The index or name of the Object Dictionary to be read from.
        sub_name (str): The subindex or name of the Object Dictionary. Optional, defaults to None.
        datatype (str): The datatype what data will be converted to. Optional, defaults to None.

        *Returns:*

        (Any): The data read from the SDO.
        """
        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        # Convert index_name and sub_name to their numeric representations if applicable
        index_name_converted = self._identify_and_convert(index_name)
        sub_name_converted = self._identify_and_convert(
            sub_name) if sub_name is not None else None

        node = self.network.nodes[node_id]

        # Get original timeout
        orig_timeout = node.sdo.RESPONSE_TIMEOUT
        # Set new timeout, 1s
        node.sdo.RESPONSE_TIMEOUT = 1
        data = node.sdo.upload(index=index_name_converted,
                               subindex=sub_name_converted)
        # Restore original timeout
        node.sdo.RESPONSE_TIMEOUT = orig_timeout

        # No conversion requested or DOMAIN datatype used
        if datatype is None or datatype.upper() == 'DOMAIN':
            return data

        return self._convert_binary_to_datatype(data, datatype)

    def write_sdo_raw(self, node_id: int, index_name: str, data: bytes, sub_name: str = 0):
        """
        Writes a SDO message to the specified CANopen node.

        *Arguments:*

        node_id (int): The index of the Object Dictionary to be read from.
        index_name (str): The index of the Object Dictionary to be read from.
        data (bytes): The data to be written to the Object Dictionary.
        sub_name (int): The subindex of the Object Dictionary. Optional, defaults to None.
        """
        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        # Convert index_name and sub_name to their numeric representations if applicable
        index_name_converted = self._identify_and_convert(index_name)
        sub_name_converted = self._identify_and_convert(
            sub_name) if sub_name is not None else None

        node = self.network.nodes[node_id]

        node.sdo.download(index=index_name_converted,
                          subindex=sub_name_converted, data=data)

    def verify_od_entry(self, node_id: int, index_name: str, sub_name: str = None):
        """
        Verifies that entry is found from Object Dictionary (EDS).

        *Arguments:*

        node_id (int): The index of the Object Dictionary to be read from.
        index_name (str): The index of the Object Dictionary to be read from.
        sub_name (int): The subindex of the Object Dictionary. Optional, defaults to None.

        *Returns:*

        (bool): True if found, else False.
        """
        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        # Convert index_name and sub_name to their numeric representations if applicable
        index_name_converted = self._identify_and_convert(index_name)
        sub_name_converted = self._identify_and_convert(
            sub_name) if sub_name is not None else None

        node = self.network.nodes[node_id]

        return bool(node.object_dictionary.get_variable(index_name_converted, sub_name_converted))

    def _convert_binary_to_datatype(self, data, datatype):
        """
        Converts binary data to a specified datatype using Python's struct module.

        *Supported datatypes are:*

        "BOOL", "I8", "I16", "I32", "I64",
        "U8", "U16", "U32", "U64",
        "R32", "R64", and "STR".

        *Parameters:*

        data (bytes): The binary data to convert.
        datatype (str): The target datatype to convert the binary data to.

        *Returns:*

        (Any): The converted data in the specified datatype.

        * Raises:*

        (ValueError): If the specified datatype is not supported.
        """

        if datatype not in can_open.FORMAT_CHARACTERS:
            raise ValueError("Unsupported datatype")

        if datatype == "STR":
            # For strings, simply decode the binary data assuming UTF-8 encoding or any other suitable encoding
            data_decoded = data.decode('utf-8')
            # Use rstrip to remove trailing \x00
            return data_decoded.rstrip('\x00')

        format_char = can_open.FORMAT_CHARACTERS[datatype]
        return struct.unpack(format_char, data)[0]

    def _convert_to_binary(self, data, datatype):
        """
        Converts the given data into its binary string representation based on the specified datatype.
        Each datatype is represented by a specific format character as per the Python `struct` module.

        *Parameters:*

        data (any): The data to be converted.
        datatype (str): A string representing the type of data to be converted.

        *Returns:*

        (str): A string representing the binary representation of the input data, with each byte separated by a space.

        Raises:
        (ValueError): If an unsupported datatype is specified.
        """
        # Check if the datatype is supported
        if datatype not in can_open.FORMAT_CHARACTERS:
            raise ValueError(f"Unsupported datatype: {datatype}")

        # Special handling for strings
        if datatype == "STR":
            # For strings, we need to ensure the format character is followed by the length of the string
            format_str = str(len(data)) + can_open.FORMAT_CHARACTERS[datatype]
            packed_data = struct.pack(format_str, data.encode())
        else:
            format_str = can_open.FORMAT_CHARACTERS[datatype]
            packed_data = struct.pack(format_str, data)

        return packed_data

    def _identify_and_convert(self, value: str):
        """
        Identifies the content of a string and converts it to its numeric representation if applicable.

        This function takes a string `value` and checks if it represents a hexadecimal number
        (prefixed with '0x' or '0X') or an integer. If `value` is a valid hexadecimal string,
        it converts it to an integer using base 16. If `value` represents an integer, it converts
        it directly to an integer. If `value` does not represent a numeric value, it returns the
        original string.

        Parameters:
        - value (str): The string to be analyzed and potentially converted. This string may
        represent a hexadecimal number, an integer, or be a non-numeric string.

        Returns:
        - int: If `value` is a valid hexadecimal or integer string, returns its integer representation.
        - str: If `value` does not represent a numeric value, returns the original string unchanged.

        Examples:
        - identify_and_convert("0x1A") returns 26 (hexadecimal conversion)
        - identify_and_convert("123") returns 123 (integer conversion)
        - identify_and_convert("Hello") returns "Hello" (non-numeric, so unchanged)
        """
        # Check if the value is a string that represents a hexadecimal number
        if str(value).lower().startswith('0x'):
            try:
                return int(value, 16)  # Convert hexadecimal string to integer
            except ValueError:
                pass  # Invalid hexadecimal, treat as a regular string

        # Check if the value is a string that represents an integer
        try:
            return int(value)  # Convert integer string to integer
        except ValueError:
            pass  # Not an integer, treat as a regular string

        # Return the original value if it's a non-convertible string
        return value
