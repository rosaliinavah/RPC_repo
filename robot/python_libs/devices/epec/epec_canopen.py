"""
File which implements class for EPEC product.
"""
import os
import threading
import logging
from utilities.bit_operations.bit_operations import bit_operations
from protocols.can_open.can_open import can_open
from robot.api import logger as ROBOT_LOGGER


class epec_canopen(can_open):
    """
    Base class which defined API towards EPEC product using CANOpen protocol.
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    # An error register object is a bit field of 8 bits.
    # This object reflects the internal error status of a device.
    # Each bit indicates an error status.
    EMCY_ERROR_REGISTERS = {
        0:  "Generic error",
        1:	"Current error",
        2:	"Voltage error",
        3:	"Temperature error",
        4:	"Communication error(overrun, error state)",
        5:	"Device profile specific error",
        6:	"Reserved(always 0)",
        7:	"Manufacturer-specific error"
    }

    def __init__(self, bustype: str = None, channel: int = None, bitrate: int = None, emcy_error_codes=None) -> None:
        can_open.__init__(self, bustype=bustype,
                          channel=channel, bitrate=bitrate)
        self.logger = logging.getLogger()
        self.original_log_level = self.logger.getEffectiveLevel()
        self.bit_api = bit_operations()
        self.thread = None
        self.thread_status = None
        self.emcy_error_codes = emcy_error_codes
        # Init as dict, gives understandable error when key dont' exist.
        if emcy_error_codes is None:
            self.emcy_error_codes = {}

    def get_etpu_version(self, node_id: int = None):
        """
        Read eTPU version from index 0x1F50 and sub-index 15 (0xF).

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*

        (str): Returns eTPU version information.
        """
        if node_id is None:
            raise ValueError("No node id given.")

        return self.read_sdo_raw(node_id=node_id, index_name=0x1F50, sub_name=15, datatype='STR')

    def get_detailed_version_info(self, node_id: int = None):
        """
        Read detailed version from index 0x1F50 and sub-index 12 (0xC).

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*

        (str): Returns special more detailed version information.
        """
        if node_id is None:
            raise ValueError("No node id given.")

        return self.read_sdo_raw(node_id=node_id, index_name=0x1F50, sub_name=12, datatype='STR')

    def get_latest_boot_error_log_identifier(self, node_id: int):
        """
        Read identifier of latest boot error log from index 0x1F50 and sub-index 11 (0xB).

        *Arguments:*

        node_id (int): The identifier for the node on the CANopen network.

        *Returns:*

        (int): Returns error identifier based on error.h
        """
        fw_log = self.read_sdo_raw(
            node_id=node_id, index_name=0x1F50, sub_name=0xB, datatype='DOMAIN')
        error_logs = self.bit_api.binary_to_system_log_entry(
            binary_data=fw_log)
        item = error_logs[-1]
        ROBOT_LOGGER.info(
            f"identifier:{item.get('identifier')},info:{item.get('info')},timestamp:{item.get('timestamp')},"
            f"error:{item.get('error')},error name:{item.get('error_name')}\n")
        return item.get('identifier')

    def get_boot_error_log(self, node_id: int, from_err_id: int = 0):
        """
        Read boot error log from index 0x1F50 and sub-index 11 (0xB).

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.

        *Returns: *

        (list): Returns list of error numbers based on error.h
        """
        ret_val = []
        fw_log = self.read_sdo_raw(
            node_id=node_id, index_name=0x1F50, sub_name=0xB, datatype='DOMAIN')
        error_logs = self.bit_api.binary_to_system_log_entry(
            binary_data=fw_log)
        # Gather error names from list of logs
        for item in error_logs:
            if from_err_id == 0 or from_err_id < item["identifier"]:
                ROBOT_LOGGER.info(
                    f"identifier:{item.get('identifier')},info:{item.get('info')},timestamp:{item.get('timestamp')},"
                    f"error:{item.get('error')},error name:{item.get('error_name')}\n")
                ret_val.append(str(item["error"]))

        return ret_val

    def get_latest_firmware_error_log_identifier(self, node_id: int):
        """
        Read identifier of latest firmware error log from index 0x1F50 and sub-index 0x12.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.

        *Returns: *

        (list): Returns list of error numbers based on error.h
        """
        fw_log = self.read_sdo_raw(
            node_id=node_id, index_name=0x1F50, sub_name=0x12, datatype='DOMAIN')
        error_logs = self.bit_api.binary_to_system_log_entry(
            binary_data=fw_log)
        item = error_logs[0]
        ROBOT_LOGGER.info(
            f"identifier:{item.get('identifier')},info:{item.get('info')},timestamp:{item.get('timestamp')},"
            f"error:{item.get('error')},error name:{item.get('error_name')}\n")
        return item.get('identifier')

    def get_firmware_error_log_latest_25(self, fw_node_id: int, from_err_id: int = 0):
        """
        Read latest 25 firmware error log from index 0x1F50 and sub-index 0x12.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        from_error_id(int): Reference to get logs from this log id.

        *Returns: *

        (list): Returns list of error numbers based on error.h
        """
        ret_val = []
        fw_log = self.read_sdo_raw(
            node_id=fw_node_id, index_name=0x1F50, sub_name=0x12, datatype='DOMAIN')
        error_logs = self.bit_api.binary_to_system_log_entry(
            binary_data=fw_log)
        # Gather error names from list of logs
        for item in error_logs:
            if from_err_id == 0 or from_err_id < item["identifier"]:
                ROBOT_LOGGER.info(
                    f"identifier:{item.get('identifier')},info:{item.get('info')},timestamp:{item.get('timestamp')},"
                    f"error:{item.get('error')},error name:{item.get('error_name')}\n")
                ret_val.append(str(item["error"]))

        return ret_val

    def get_firmware_error_log(self, fw_node_id: int, from_err_id: int = 0):
        """
        Read all firmware error log from index 0x1F50 and sub-index 0x5.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        from_error_id(int): Reference to get logs from this log id.

        *Returns: *

        (list): Returns list of error numbers based on error.h
        """
        ret_val = []
        fw_log = self.read_sdo_raw(
            node_id=fw_node_id, index_name=0x1F50, sub_name=5, datatype='DOMAIN')
        error_logs = self.bit_api.binary_to_system_log_entry(
            binary_data=fw_log)
        # Gather error names from list of logs
        for item in error_logs:
            if from_err_id == 0 or from_err_id < item["identifier"]:
                ROBOT_LOGGER.info(
                    f"identifier:{item.get('identifier')},info:{item.get('info')},timestamp:{item.get('timestamp')},"
                    f"error:{item.get('error')},error name:{item.get('error_name')}\n")
                ret_val.append(str(item["error"]))

        return ret_val

    def read_protection_status(self, node_id: int = None):
        """
        Read protection status from index 2032h sub-index 1 (size 1 byte).

        If value=0 continue to next step.
        If value=AAh, unit already unlocked.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.

        * Returns: *

        (int, str): Identifier code, explanation text
        """
        if node_id is None:
            raise ValueError("No node id given.")

        ret_val = self.read_sdo_raw(
            node_id=node_id, index_name=0x2032, sub_name=1, datatype='U8')

        if ret_val == 0:
            return (0, "continue to next step.")
        if ret_val == 170:
            return (170, "unit already unlocked, download is enabled.")
        if ret_val == 255:
            return (255, "password was wrong and reboot is required.")

        raise ValueError(f"Invalid status:{ret_val}")

    def write_controlunit_password(self, node_id: int = None, password: str = None):
        """
        Writes password to device. By default last 4 digits of serial number.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        password(str): control unit password string to index 2031h sub-index 1
        """
        if password is None:
            raise ValueError("No password defined, can't be None")

        self.write_sdo_raw(node_id=node_id, index_name=0x2031,
                           sub_name=1, data=password.encode())

    def reset_control_unit_password(self, node_id: int = None):
        """
        Resets password to default value by writing nonsense data to 0x2031sub3.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        """
        if node_id is None:
            raise ValueError("No node id given.")

        # Password can be reset by writing any data
        nonsense_data = b'\xFF\xFF\xFF\xFF'
        try:
            orig_timeout = None
            node = self.network.nodes[node_id]
            orig_timeout = node.sdo.RESPONSE_TIMEOUT
            node.sdo.RESPONSE_TIMEOUT = 1
            node.sdo.download(index=0x2031,
                              subindex=3, data=nonsense_data)
            node.sdo.RESPONSE_TIMEOUT = orig_timeout
        except Exception as ex:
            # Restore original timeout
            if orig_timeout is not None:
                node.sdo.RESPONSE_TIMEOUT = orig_timeout
            raise ex

    def write_control_unit_puk_code(self, node_id: int = None, puk_code: str = None):
        """
        Opens protection. Default PUK-code can be calculated from device serial number.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        puk_code(str): Control unit PUK-code string
        """
        if node_id is None:
            raise ValueError("No node id given.")
        if puk_code is None:
            raise ValueError("No PUK-code defined, can't be None")

        self.write_sdo_raw(node_id=node_id, index_name=0x2034,
                           sub_name=1, data=puk_code.encode())

    def _download_file(self, node_id: int = None, index: int = None, subindex: int = None, bin_path: str = None, expect_error: bool = False):
        """
        Downloads file to device via CANOpen.

        *Arguments: *

        node_id (int): The identifier for the node on the CANopen network.
        index (int): CANOpen index
        subindex (int): CANOpen subindex
        bin_path (str): Path to binary file.
        expect_error (bool): When False, logic raises an exception when fails
        """
        try:
            orig_timeout = None

            if not os.path.isfile(bin_path):
                raise AttributeError("Invalid binary path.")

            self.thread_status = None
            # Get app binary file size
            app_file_size = os.path.getsize(bin_path)
            # Open app bin file
            with open(bin_path, 'rb') as app_bin_file:
                # Get CANOpen node
                node = self.network.nodes[node_id]
                # Get original timeout
                orig_timeout = node.sdo.RESPONSE_TIMEOUT
                # Set new timeout
                node.sdo.RESPONSE_TIMEOUT = 30
                # Open the data stream as a file like object.
                # https://canopen.readthedocs.io/en/stable/sdo.html#canopen.sdo.SdoClient.open
                outfile = node.sdo[index][subindex].open(
                    'wb', size=app_file_size, buffering=1024, block_transfer=False)
                # Write app bin file to CANOpen file object
                outfile.write(app_bin_file.read())
                # Restore original timeout
                node.sdo.RESPONSE_TIMEOUT = orig_timeout

        except Exception as ex:
            # For thread status, running this in thread failed.
            self.thread_status = repr(ex)
            # Restore original timeout
            if orig_timeout is not None:
                node.sdo.RESPONSE_TIMEOUT = orig_timeout
            if expect_error is True:
                return
            raise ex

    def download_application(self, node_id: int = None, app_bin_path: str = None):
        """
        Downloads application to device via CANOpen.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        app_bin_path: Path to application binary file.
        """
        self._download_file(
            node_id=node_id, index=0x1F50, subindex=0x3, bin_path=app_bin_path, expect_error=False)

    def download_application_in_subprocess(self, node_id: int = None, app_bin_path: str = None):
        """
        Downloads application to device via CANOpen in subprocess.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        app_bin_path: Path to application binary file.
        """
        self.thread = threading.Thread(
            target=self._download_file, args=(node_id, 0x1F50, 0x3, app_bin_path, True))
        self.thread.start()

    def wait_download_application_subprocess(self, timeout_s=10):
        """
        Waits Application download thread to finish and join.

        *Arguments: *

        timeout_s: subprocess wait in seconds

        * Raises: *

        (RuntimeError): if unable to join during timeout.
        """
        # Wait thread to join
        self.thread.join(timeout=timeout_s)
        # Waited and still running, timeout occurred
        if self.thread.is_alive():
            raise RuntimeError("Thread is alive, should not be.")
        if self.thread_status is not None:
            print(f"Exception in thread:{self.thread_status}")

    def remove_application(self, node_id: int = None):
        """
        Device remains in stopped state and the application is cleared from flash.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        """
        try:
            orig_timeout = None
            node = self.network.nodes[node_id]
            orig_timeout = node.sdo.RESPONSE_TIMEOUT
            node.sdo.RESPONSE_TIMEOUT = 30
            node.sdo[0x1F50][0x3].raw = b'\xFF\xFF\xFF\xFF'
            node.sdo.RESPONSE_TIMEOUT = orig_timeout
        except Exception as ex:
            # Restore original timeout
            if orig_timeout is not None:
                node.sdo.RESPONSE_TIMEOUT = orig_timeout
            raise ex

    def download_firmware(self, node_id: int = None, fw_bin_path: str = None):
        """
        Downloads the firmware binary to device.
        Download Firmware binary file(for example firmware.bin) to index 1F50h sub-index 2h.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        fw_bin_path: Path to firmware binary file.
        """
        self._download_file(
            node_id=node_id, index=0x1F50, subindex=0x2, bin_path=fw_bin_path, expect_error=False)

    def download_firmware_in_subprocess(self, node_id: int = None, fw_bin_path: str = None):
        """
        Downloads the firmware binary to device in subprocess.
        Download Firmware binary file(for example firmware.bin) to index 1F50h sub-index 2h.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        fw_bin_path: Path to firmware binary file.
        """
        self.thread = threading.Thread(
            target=self._download_file, args=(node_id, 0x1F50, 0x2, fw_bin_path, True))
        self.thread.start()

    def wait_download_firmware_subprocess(self, timeout_s=10):
        """
        Waits Firmware download thread to finish and join.

        *Arguments: *

        timeout_s: subprocess wait in seconds

        * Raises: *

        (RuntimeError): if unable to join during timeout.
        """
        # Wait thread to join
        self.thread.join(timeout=timeout_s)
        # Waited and still running, timeout occurred
        if self.thread.is_alive():
            raise RuntimeError("Thread is alive, should not be.")
        if self.thread_status is not None:
            print(f"Exception in thread:{self.thread_status}")

    def download_etpu(self, node_id: int = None, etpu_bin_path: str = None):
        """
        Downloads the eTPU binary to the control unit.
        Download eTPU binary file(for example eTPU.bin) to index 1F50h sub-index Dh.

        *Arguments: *

        node_id(int): The identifier for the node on the CANopen network.
        fw_bin_path: Path to firmware binary file.
        """
        self._download_file(
            node_id=node_id, index=0x1F50, subindex=13, bin_path=etpu_bin_path, expect_error=False)

    def get_active_emcy_codes(self, node_id: int):
        """
        Get all active EMCY messages from given node

        * Arguments: *

        node_id(int): The index of CAN node

        * Returns: *

        (list): Active EMCYs(code: hex, mask: hex, register: hex, data: list, description: str)
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        node = self.network.nodes[node_id]

        ret_val = []
        for emcy in node.emcy.active:
            found = False
            emcy_code_hex = hex(emcy.code)[2:]
            emcy_code_hex = '0x' + emcy_code_hex.upper()

            emcy_register_hex = hex(emcy.register)[2:]
            emcy_register_hex = '0x' + emcy_register_hex.upper()

            for emcy_error_code in self.emcy_error_codes:
                if emcy.code & int(emcy_error_code['mask'], 0) == int(emcy_error_code['code'], 0):
                    ret_val.append([
                        f"{emcy_code_hex}, {emcy_register_hex}, {list(emcy.data)}, {emcy_error_code['description']}"])
                    found = True
                    break

            if found is False:
                ret_val.append([
                    f"{emcy_code_hex}, {emcy_register_hex}, {list(emcy.data)}, Item-not-in-the-robot-list"])

        return ret_val

    def get_all_emcy_codes(self, node_id: int):
        """
        Get all received EMCY messages from given node

        * Arguments: *

        node_id(int): The index of CAN node

        * Returns: *

        (list): All received EMCYs(code: hex, mask: hex, register: hex, data: list, description: str)
        """
        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        node = self.network.nodes[node_id]

        ret_val = []
        for emcy in node.emcy.log:
            found = False
            emcy_code_hex = hex(emcy.code)[2:]
            emcy_code_hex = '0x' + emcy_code_hex.upper()

            emcy_register_hex = hex(emcy.register)[2:]
            emcy_register_hex = '0x' + emcy_register_hex.upper()

            for emcy_error_code in self.emcy_error_codes:
                if emcy.code & int(emcy_error_code['mask'], 0) == int(emcy_error_code['code'], 0):
                    ret_val.append([
                        f"{emcy_code_hex}, {emcy_register_hex}, {list(emcy.data)}, {emcy_error_code['description']}"])
                    found = True
                    break

            if found is False:
                ret_val.append([
                    f"{emcy_code_hex}, {emcy_register_hex}, {list(emcy.data)}, Item-not-in-the-robot-list"])

        return ret_val

    def reset_all_emcy_codes(self, node_id: int):
        """
        Reset log and active lists.

        *Arguments: *

        node_id(int): The index of CAN node
        """

        if node_id is None:
            raise ValueError("No node id given.")

        if self.network.nodes.get(node_id) is None:
            raise ValueError(
                "No such node id, remember to add node using add_node method.")

        node = self.network.nodes[node_id]
        node.emcy.reset()

    def set_minimum_logging_level_to_critical(self):
        """
        Sets the logging level to logging.CRITICAL.
        """
        self.logger.setLevel(logging.CRITICAL)

    def set_minimum_logging_level_to_error(self):
        """
        Sets the logging level to logging.ERROR.
        """
        self.logger.setLevel(logging.ERROR)

    def set_minimum_logging_level_to_default(self):
        """
        Sets the logging level to default.
        """
        self.logger.setLevel(self.original_log_level)
