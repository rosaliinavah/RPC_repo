"""
File to implement class and methods to parse aliases from Veristand XML file and save them into a Robot Framework resource file.
"""
import os
import sys
import xml.etree.ElementTree as ET


class alias_xml_parser:
    """
    A class to parse aliases from an XML file with nested sections and save them into a Robot Framework resource file.
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        """
        Initialize the XMLAliasParser class with the XML file path.
        """
        self.xml_file_path = None
        self.robot_resource_file_path = None
        self.aliases = {}

    def read_aliases(self, xml_file_path):
        """
        Reads aliases from the XML file and stores them in the aliases dictionary with section names as prefixes.

        *Arguments:*

        xml_file_path (str): The path to the XML file to be parsed.

        *Returns:*

        (dict): A dictionary where keys are prefixed alias names and values are the corresponding paths.
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

        return self.aliases

    def _parse_section(self, section, section_names):
        """
        Recursively parses a section and its sub-sections.

        *Arguments:*

        section (xml.etree.ElementTree.Element): The current XML section element.
        section_names (list): The list of parent section names.
        """
        for child in section:
            if child.tag == 'Section':
                # Append the current section name and continue parsing
                current_section_name = child.get('Name')
                self._parse_section(child, section_names +
                                    [current_section_name])
            elif child.tag == 'Alias':
                self._add_alias(child, section_names)

    def _add_alias(self, alias, section_names):
        """
        Adds an alias to the aliases dictionary with section names as prefixes.

        *Arguments:*

        alias (xml.etree.ElementTree.Element): The alias XML element.
        section_names (list): The list of parent section names.
        """
        alias_name = alias.get('Name')
        path = alias.find(".//DependentNode").get('Path')
        prefixed_name = '_'.join(section_names + [alias_name])
        prefixed_name = prefixed_name.upper()

        if self.aliases.get(prefixed_name) is not None:
            if self.aliases.get(prefixed_name) != path:
                raise ValueError(
                    f"Alias '{prefixed_name}' found with different mapping value '{self.aliases.get(prefixed_name)}' != '{path}'")

        self.aliases[prefixed_name] = path

    def save_to_robot_resource(self, resource_file_path):
        """
        Saves the aliases into a Robot Framework resource file as variables.

        *Arguments:*

        resource_file_path (str): The path to the Robot Framework resource file where aliases will be saved.
        """
        with open(resource_file_path, 'w', encoding='utf8') as file:
            file.write("*** Settings ***\n")
            file.write(
                "Documentation\tThis file is generated from veristand XML.\n...\tVariables are mapped to ATE IOs.\n\n\n")
            file.write("*** Variables ***\n")
            for alias_name, path in self.aliases.items():
                file.write(f'${{{alias_name}}} =    {path}\n')

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
        variables = {}
        in_variables_section = False

        if robot_resource_file_path is None:
            raise FileExistsError("Robot resource file not defined.")

        if not os.path.isfile(robot_resource_file_path):
            raise FileExistsError(
                f"File don't exist:{robot_resource_file_path}")

        with open(robot_resource_file_path, 'r', encoding='utf8') as file:
            for line in file:
                line = line.strip()

                # Check for the start of the Variables section
                if line == '*** Variables ***':
                    in_variables_section = True
                    continue

                # Check for the end of the Variables section (or end of file)
                if in_variables_section and (line.startswith('***') or line == ''):
                    break

                # Parse variables
                if in_variables_section and '=' in line:
                    var_name, var_value = line.split('=', 1)
                    var_name = var_name.strip().replace(
                        '${', '').replace('}', '')
                    var_value = var_value.strip()
                    variables[var_name] = var_value

        return variables

    def compare_aliases_files(self, veristand_folder=None, robot_resource_file_path=None):
        """
        Compares aliases and variables in Veristand XMLs and Robot Framework resource files.

        *Arguments:*

        veristand_folder: Path to Veristand folder with XML files
        robot_resource_file_path: Path to Robot Framework resource file
        """

        if veristand_folder is None or robot_resource_file_path is None:
            raise AttributeError(
                "Define XML file and Robot resource file paths.")

        nivssdf_files = self.get_nivssdf_files(veristand_folder)

        for file in nivssdf_files:
            self.read_aliases(file)

        robot_vars_dict = self.read_robot_variables(robot_resource_file_path)
        # Check if keys mismatch
        if self.aliases.keys() != robot_vars_dict.keys():
            raise KeyError(
                "Veristand and Robot alias dictionary keys do not match")

        # Check values and raise Exception if value mismatch
        for key, value in self.aliases.items():
            if value != robot_vars_dict[key]:
                raise ValueError(
                    f"Value mismatch for key '{key}': '{value}' != '{robot_vars_dict[key]}'")

    def get_nivssdf_files(self, folder):
        """
        Get all .nivssdf files in the given folder.

        *Arguments:*

        folder (str): Relative path to the folder where to search for .nivssdf files.

        *Returns:*

        (list): List of .nivssdf files found in the folder.
        """
        nivssdf_files = []
        # folder = str(folder).rstrip("/").rstrip("\\")
        folder = os.path.normpath(folder)

        # Walk through the directory
        for root, _, files in os.walk(folder):
            # Filter and append .nivssdf files
            for file in files:
                if file.endswith(".nivssdf"):
                    nivssdf_files.append(os.path.join(root, file))

        return nivssdf_files


def create_variable_file(arguments):
    """
    Main function to execute the script. Adjust the paths to the CSV and output files as needed.

    *Arguments:*

    arguments: command line arguments
    """
    xml_parser = alias_xml_parser()
    veristand_folder = arguments[0]
    robot_resource_file = arguments[1]
    nivssdf_files = xml_parser.get_nivssdf_files(veristand_folder)

    for file in nivssdf_files:
        xml_parser.read_aliases(file)
    xml_parser.save_to_robot_resource(robot_resource_file)


if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) < 3:
        print("****\nNot enough arguments\nUse: python .\\python_libs\\utilities\\alias_xml_parser\\alias_xml_parser.py "
              ".\\veristand\\Epec Base Project .\\robot\\resources\\veristand_aliases.resource\n****")
        sys.exit(1)
    # Ignore first argument, the file itself
    args = sys.argv[1:]
    create_variable_file(args)
