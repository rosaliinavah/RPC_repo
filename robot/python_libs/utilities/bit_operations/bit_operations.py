"""
File to contains a class with bunch of methods to do various bit operations.
"""
import struct
from devices.epec.epec_errors import epec_errors


class system_log_entry:
    """
    Class to pack SystemLogEntry information from FW
    """

    def __init__(self, identifier, info, timestamp, error):
        self.identifier = identifier
        self.info = info
        self.timestamp = timestamp
        self.error = error


class bit_operations:
    """
    Class to handle different bit operations
    """

    def __init__(self) -> None:
        self.error_api = epec_errors()

    def binary_to_system_log_entry(self, binary_data):
        """
        Converts a binary to a list of system_log_entry instances.

        Each system_log_entry instance contains four 32-bit integers representing 'identifier', 'info', 'timestamp', and 'error'.
        The binary data is expected to be in a format where each set of these four 32-bit integers is sequentially organized.

        *Parameters:*

        binary_data: The binary string containing the data.

        *Returns:*

        (str): Returns list of dict log items [{identifier, info, timestamp, error, error_name}, ...]
        """
        # Each 32-bit integer takes up 4 bytes, so we have 16 bytes per system_log_entry instance.
        chunk_size = 16
        data_structures = []
        ret_val = []
        for i in range(0, len(binary_data), chunk_size):
            # Unpack 4 big-endian 32-bit unsigned integers from the binary data.
            unpacked_data = struct.unpack(
                '>IIII', binary_data[i:i + chunk_size])
            data_structure = system_log_entry(*unpacked_data)
            data_structures.append(data_structure)

        if len(data_structures) > 0:
            for item in data_structures:
                error_name = self.error_api.get_error_name_by_id(item.error)
                ret_val.append({"identifier": item.identifier, "info": item.info,
                               "timestamp": item.timestamp, "error": item.error, "error_name": error_name})

        return ret_val

    def calculate_puk_code_from_serial_number(self, serial_number: str = None):
        """
        Calculates PUK-code from device serial number.

        Each system_log_entry instance contains four 32-bit integers representing 'identifier', 'info', 'timestamp', and 'error'.
        The binary data is expected to be in a format where each set of these four 32-bit integers is sequentially organized.

        *Arguments: *

        serial_number (str): The device serial number.

        *Returns:*

        (str): Calculated PUK-code
        """
        if serial_number is None:
            raise ValueError("No serial number given.")

        # Reverse serial number string and convert to number
        reversed_sn = serial_number[::-1]
        reversed_sn_number = int(reversed_sn)

        # Bitwise operation with U32 number bit mask
        mask_u32 = 0xFFFFFFFF
        bitwise_puk_code = int(reversed_sn_number ^ mask_u32)

        puk_code = str(bitwise_puk_code)
        return puk_code
