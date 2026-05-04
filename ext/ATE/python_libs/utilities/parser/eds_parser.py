"""
File which parses CAN EDS file and provides API to request data from parsed EDS information.
"""
import re


class index_item:
    """
    Class to contain Transmit index information from EDS file
    """

    def __init__(self) -> None:
        """
        Initialize an IndexClass instance.
        """
        self.index = None
        self.parameter_name = None
        self.object_type = None
        self.sub_number = None
        self.list_of_subs = []


class sub_index_item:
    """
    Class to contain Transmit sub index information from EDS file
    """

    def __init__(self) -> None:
        """
        Initialize a SubIndexClass instance.
        """
        self.index = None
        self.parameter_name = None
        self.object_type = None
        self.data_type = None
        self.access_type = None
        self.default_value = None
        self.pdo_mapping = None
        self.low_limit = None
        self.high_limit = None


class eds_parser:
    """
    Class to parse CAN EDS files and retrieve indexes and subindexes within a specified range.
    """

    DATA_TYPE_MAP = {
        "0x0001": "08",  # BOOLEAN - Single bit value
        "0x0002": "08",  # INTEGER8 - 8-bit signed integer.
        "0x0003": "10",  # INTEGER16 - 16-bit signed integer.
        "0x0010": "18",  # INTEGER24 - 24-bit signed integer.
        "0x0004": "20",  # INTEGER32 - 32-bit signed integer.
        "0x0012": "28",  # INTEGER40 - 40-bit signed integer.
        "0x0013": "30",  # INTEGER48 - 48-bit signed integer.
        "0x0014": "38",  # INTEGER56 - 56-bit signed integer.
        "0x0015": "40",  # INTEGER64 - 64-bit signed integer.
        "0x0005": "08",  # UNSIGNED8 - 8-bit unsigned integer.
        "0x0006": "10",  # UNSIGNED16 - 16-bit unsigned integer.
        "0x0016": "18",  # UNSIGNED24 - 24-bit unsigned integer.
        "0x0007": "20",  # UNSIGNED32 - 32-bit unsigned integer.
        "0x0018": "28",  # UNSIGNED40 - 40-bit unsigned integer.
        "0x0019": "30",  # UNSIGNED48 - 48-bit unsigned integer.
        "0x001A": "38",  # UNSIGNED56 - 56-bit unsigned integer.
        "0x001B": "40",  # UNSIGNED64 - 64-bit unsigned integer.
        "0x0008": "20",  # REAL32 - 32-bit single prec. float. point
        "0x0011": "40"   # REAL64 - 64-bit double prec. float. point
    }

    def __init__(self, file_path: str, min_index: int = 0x1000, max_index: int = 0xFFFF) -> None:
        """
        Initialize an EdsParser instance.

        *Arguments:*

        file_path (str): The path to the EDS file.
        min_index (int): The minimum index value.
        max_index (int): The maximum index value.
        """
        self.file_path = file_path
        self.min_index = min_index
        self.max_index = max_index
        self.indexes = self.parse_eds_file()

    def parse_eds_file(self):
        """
        Parse the EDS file to find indexes and subindexes within the specified range.

        *Returns:*

        (dict): A dictionary of index_item instances that fall within the range.
        """
        indexes = {}
        current_index = None
        current_subindex = None
        with open(self.file_path, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith(';'):
                    continue

                index_match = re.match(r'\[([0-9A-Fa-f]+)\]', line)
                subindex_match = re.match(
                    r'\[([0-9A-Fa-f]+)sub([0-9A-Fa-f]+)\]', line)

                if index_match:
                    current_index = index_match.group(1)
                    current_index_value = int(current_index, 16)
                    if self.min_index <= current_index_value <= self.max_index:
                        indexes[current_index] = index_item()
                        indexes[current_index].index = current_index
                    current_subindex = None

                elif subindex_match:
                    current_index = subindex_match.group(1)
                    subindex_number = subindex_match.group(2)
                    if current_index in indexes:
                        current_subindex = sub_index_item()
                        current_subindex.index = subindex_number
                        indexes[current_index].list_of_subs.append(
                            current_subindex)

                elif '=' in line:
                    key, value = map(str.strip, line.split('=', 1))
                    if current_subindex is None:
                        if current_index in indexes:
                            if key == 'ParameterName':
                                indexes[current_index].parameter_name = value
                            elif key == 'ObjectType':
                                indexes[current_index].object_type = value
                            elif key == 'SubNumber':
                                indexes[current_index].sub_number = value
                    else:
                        if current_index in indexes:
                            if key == 'ParameterName':
                                current_subindex.parameter_name = value
                            elif key == 'ObjectType':
                                current_subindex.object_type = value
                            elif key == 'DataType':
                                current_subindex.data_type = value
                            elif key == 'AccessType':
                                current_subindex.access_type = value
                            elif key == 'DefaultValue':
                                current_subindex.default_value = value
                            elif key == 'PDOMapping':
                                current_subindex.pdo_mapping = value
                            elif key == 'LowLimit':
                                current_subindex.low_limit = value
                            elif key == 'HighLimit':
                                current_subindex.high_limit = value

        return indexes

    def get_by_index(self, index: str, subindex: str = None):
        """
        Retrieve an index and optionally a specific subindex.

        *Arguments:*

        index (str): The index to retrieve.
        subindex (str, optional): The subindex to retrieve. Defaults to None.

        *Returns:*

        (class): The index class or the specific subindex class.
        """
        if index not in self.indexes:
            return None

        if subindex is None:
            return self.indexes[index]

        subindex_instance = next(
            (sub for sub in self.indexes[index].list_of_subs if sub.index == subindex), None)
        return subindex_instance

    def create_pdo_mapping_value(self, index: str, parameter_name: str):
        """
        Creates a pdo mapping value for Robot by EDS index and its subindex parameter name.

        *Arguments:*

        index (str): index of the EDS item
        parameter_name (str): The parameter name to search for from index.

        *Returns:*

        (str): 0x<index><sub-index><length>  0x<index><sub-index><length>
        """
        # 0x<index><sub-index><length>
        ret_val = f"0x{index}"

        # Get index 'master' from EDS
        index_pdo_item = self.get_by_index(index)
        if index_pdo_item is None:
            raise ValueError(f"PDO not found from EDS by index: '{index}'")

        # Get subindex item located as subindex of 'master' item
        for subindex_item in index_pdo_item.list_of_subs:
            if parameter_name == subindex_item.parameter_name:
                # Pad the hexadecimal string with leading zeros to ensure it has at least 2 digits
                ret_val += subindex_item.index.zfill(2)
                ret_val += eds_parser.DATA_TYPE_MAP.get(
                    subindex_item.data_type) + "  "
                return ret_val

        raise ValueError(
            f"Subindex not found from EDS file by index: '{index}' and subindex's parameter name: '{parameter_name}'")
