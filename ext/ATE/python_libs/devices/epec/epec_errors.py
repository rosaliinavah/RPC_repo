"""
EPEC device FW and APP log returns an error codes when it encounters a problems.

Use the following dictionary to locate an error code message.

Example:
    epec_error_api = epec_errors()
    error_msg = epec_error_api.get_error_name_by_id(33000)
"""
import os
import re

# pylint:disable=too-few-public-methods


class epec_errors:
    """
    Class to parse EPEC device errors
    """

    def __init__(self) -> None:
        # Set the location of header file
        self.header_file_path = os.path.join(
            os.path.dirname(__file__), 'error.h')

    def _parse_error_header(self, header_file_path=None):
        """
        Parses the given C header file and returns a dictionary that maps
        error code integers to their symbolic names (e.g. 0 -> 'FW_ERR_OK').

        Ignore the comments and only focus on lines of the form:
            SYMBOLIC_NAME = NUMBER
        within the 'typedef enum ... { ... }'.

        Returns:
            dict[int, str]: { error_code: error_name }
        """
        error_map = {}

        # Regex to match lines like "FW_ERR_OK = 0," or "FW_ERR_FAIL = 33001"
        # Explanation:
        #   ^                 start of string
        #   \s*               optional leading whitespace
        #   (\w+)             capture 1: the error name (alphanumeric and underscores)
        #   \s*=\s*           equals sign with optional spaces
        #   (\d+)             capture 2: the numeric value
        #   \s*,?\s*$         optional trailing comma, optional whitespace, end of string
        pattern = re.compile(r'^\s*(\w+)\s*=\s*(\d+)\s*,?\s*$')

        inside_enum = False
        with open(header_file_path, 'r', encoding='UTF-8') as header_file:
            for line in header_file:
                stripped_line = line.strip()

                # Detect when we enter the enum block
                if re.search(r'typedef\s+enum', stripped_line):
                    inside_enum = True
                    continue
                # Detect when we exit the enum block
                if inside_enum and '}' in stripped_line:
                    inside_enum = False
                    continue

                # Only consider lines inside the enum definition
                if inside_enum:
                    match = pattern.match(stripped_line)
                    if match:
                        error_name = match.group(1)
                        error_code = int(match.group(2))
                        error_map[error_code] = error_name

        return error_map

    def get_error_name_by_id(self, error_id: int = None):
        """
        Given the path to a C header file and an integer error code,
        returns the 'symbolic name' (e.g., FW_ERR_OK) for that code
        if found, or 'Unknown error code' otherwise.

        *Parameters:*

        header_file_path (str): Path to C header file
        error_id (int): Error code id number

        *Returns:*

        (str): Symbolic name, 'Unknown error code' if not found

        """
        # Path given and file exists
        if self.header_file_path is None or not os.path.isfile(self.header_file_path):
            raise ValueError(
                f"Invalid header file path:{self.header_file_path}")

        error_map = self._parse_error_header(self.header_file_path)
        return error_map.get(error_id, "Unknown error code")
