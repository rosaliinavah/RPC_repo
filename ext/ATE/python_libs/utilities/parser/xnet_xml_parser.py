"""
File to implement class and methods to parse XNET DB channels from Veristand XML file and save them into a Robot Framework resource file.
"""
import os
import sys
import re
import xml.etree.ElementTree as ET


class xnet_xml_parser:
    """
    A class to parse XNET DB channels from an XML file with nested sections and save them into a Robot Framework resource file.
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        """
        Initialize the XNET DB channels parser class with the XML file path.
        """
        self.xml_file_path = None
        self.robot_resource_file_path = None
        self.xnet_db_items = {}
        self.xnet_db_comments = {}

    def read_xnet_db_channels(self, xml_file_path):
        """
        Reads XNET DB channels from the XML file and stores them in the dictionary with section names as prefixes.

        *Arguments:*

        xml_file_path (str): The path to the XML file to be parsed.

        *Returns:*

        (dict): A dictionary where keys are prefixed XNET DB channel names and values are the corresponding paths.
        """
        # Check if XML file exists
        if not os.path.isfile(xml_file_path):
            raise FileNotFoundError(
                f"Given XML file not found:{xml_file_path}")

        self.xml_file_path = xml_file_path
        tree = ET.parse(self.xml_file_path)
        root = tree.getroot()

        # Start parsing from the 'Root' element
        root_section = root.find('.//Root')
        if root_section is not None:
            self._parse_section(root_section, [])

        return self.xnet_db_items

    def _parse_section(self, section, section_names):
        """
        Recursively parses a section and its sub-sections.

        *Arguments:*

        section (xml.etree.ElementTree.Element): The current XML section element.
        section_names (list): The list of parent section names.
        """
        for child in section:
            if child.tag in ['TargetSections', 'Target', 'Section']:
                # Append the current section name and continue parsing
                current_section_name = child.get('Name')
                self._parse_section(child, section_names +
                                    [current_section_name])
            elif child.tag == 'Channel':
                # Interested only if channel is defined to parent NI-XNET
                if "NI-XNET" in section_names:
                    current_section_name = child.get('Name')
                    self._add_xnet_db_item(child, section_names)

    def _add_xnet_db_item(self, xml_item: ET.Element, section_names):
        """
        Adds an XNET DB item to the dictionary with section names as prefixes.

        *Arguments:*

        xml_item (xml.etree.ElementTree.Element): The XNET DB XML element.
        section_names (list): The list of parent section names.
        """
        xnet_db_item_name = xml_item.get('Name')
        # Remove 'single-point' item
        robot_var_names = [
            name for name in section_names if "Single-Point" not in name]
        # Variable name list - from CAN item to the end of the list
        start_index = robot_var_names.index("CAN")+1
        # Remove CO-ID from list item using regular expression to match content within parentheses (including the parentheses)
        pattern = r'\s*\([^)]*\)'
        # Using list comprehension to remove any content within parentheses from each item
        robot_var_names = [re.sub(pattern, '', item)
                           for item in robot_var_names]
        # Create robot variable string
        prefixed_name = '_'.join(
            robot_var_names[start_index:] + [xnet_db_item_name])
        # Create path for robot variable value
        path = '/'.join(section_names + [xnet_db_item_name])
        # Variable name to upper case and replace spaces with underscore
        prefixed_name = "XNET_" + prefixed_name.upper().replace(' ', '_')
        self.xnet_db_items[prefixed_name] = path
        # Get comment for a robot file
        description = xml_item.find(".//Description").text
        self.xnet_db_comments[prefixed_name] = description

    def save_to_robot_resource(self, resource_file_path):
        """
        Saves the XNET DB items into a Robot Framework resource file as variables.

        *Arguments:*

        resource_file_path (str): The path to the Robot Framework resource file where XNET DB channels will be saved.
        """
        with open(resource_file_path, 'w', encoding='utf8') as file:
            file.write("*** Settings ***\n")
            file.write(
                "Documentation\tThis file is generated from veristand XML.\n...\tVariables are mapped to NI-XNET DB CAN PDOs.\n\n\n")
            file.write("*** Variables ***\n")
            for xnet_db_item, path in self.xnet_db_items.items():
                if self.xnet_db_comments[xnet_db_item] is not None:
                    comment = self.xnet_db_comments[xnet_db_item] + '\n'
                    file.write(f'# {comment}')
                file.write(f'${{{xnet_db_item}}} =\n...    {path}\n')

            self.robot_resource_file_path = resource_file_path

    def read_robot_variables(self, robot_resource_file_path=None):
        """
        Parses a Robot Framework resource file and extracts variables from the 'Variables' section.
        Removes '${}' characters from variable names and trims spaces and '=' from values.

        *Arguments:*

        robot_resource_file_path: Path to the Robot Framework resource file.

        *Returns:*

        (dict): Dictionary with modified variable names as keys and their trimmed values as dictionary values.
        """
        variables = {}  # Initialize an empty dictionary to store variables
        with open(robot_resource_file_path, 'r', encoding='utf8') as file:
            lines = file.readlines()
            current_var = None  # Variable to keep track of the current variable being read

            for line in lines:
                line = line.strip()  # Remove leading and trailing whitespace

                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue

                # Check if the line defines a new variable
                if line.startswith('${') and '=' in line:
                    parts = line.split('=')
                    current_var = parts[0].strip()
                    # Remove unwanted characters from the variable name
                    current_var = current_var.replace(
                        '$', '').replace('{', '').replace('}', '')
                    value = parts[1].strip() if len(parts) > 1 else ''
                    # Add or update the variable in the dictionary
                    variables[current_var] = value
                elif current_var and line.startswith('...'):
                    # Continuation of the value from the previous line
                    # Append the additional value, removing the leading '...'
                    variables[current_var] += line[3:].strip()
                else:
                    current_var = None  # Reset current variable if the line is not a continuation
        return variables

    def compare_xnet_files(self, xml_file_path=None, robot_resource_file_path=None):
        """
        Compares XNET DB channels and variables in Veristand XML and Robot Framework resource files.

        *Arguments:*

        xml_file_path: Path to Veristand XML file
        robot_resource_file_path: Path to Robot Framework resource file
        """

        if xml_file_path is None or robot_resource_file_path is None:
            raise AttributeError(
                "Define XML file and Robot resource file paths.")

        xnet_db_dict = self.read_xnet_db_channels(xml_file_path)
        robot_vars_dict = self.read_robot_variables(robot_resource_file_path)
        # Check if keys mismatch
        if xnet_db_dict.keys() != robot_vars_dict.keys():
            raise KeyError("Dictionary keys do not match")

        # Check values and raise Exception if value mismatch
        for key, value in xnet_db_dict.items():
            if value != robot_vars_dict[key]:
                raise ValueError(
                    f"Value mismatch for key '{key}': '{value}' != '{robot_vars_dict[key]}'")


def create_variable_file(arguments):
    """
    Main function to execute the script. Adjust the paths to the CSV and output files as needed.

    *Arguments:*

    arguments: command line arguments
    """
    xml_file = arguments[0]
    robot_resource_file = arguments[1]
    xml_parser = xnet_xml_parser()
    xml_parser.read_xnet_db_channels(xml_file)
    xml_parser.save_to_robot_resource(robot_resource_file)


def compare_variable_files(arguments):
    """
    Compare XML and Robot resource files to indicate if there are mismatch.

    *Arguments:*

    arguments: command line arguments
    """
    xml_file = arguments[0]
    robot_resource_file = arguments[1]
    xml_parser = xnet_xml_parser()
    xml_parser.compare_xnet_files(xml_file, robot_resource_file)


if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) < 3:
        print("****\nNot enough arguments\nUse: python .\\python_libs\\utilities\\xml_parser\\xnet_xml_parser.py "
              ".\\veristand\\Epec Base Project\\Epec Base Project.nivssdf .\\robot\\resources\\veristand_xnet_db.resource\n****")
        sys.exit(1)

    # Ignore first argument, the file itself
    args = sys.argv[1:]

    create_variable_file(args)
