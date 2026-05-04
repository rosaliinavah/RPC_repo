"""
NI XNET library for interacting with National Instruments XNET.
"""
import os
import xml.etree.ElementTree as ET
from nixnet import system


class xnet_db_utility:
    """
    Class acts as an interface for National Instruments XNET
    """

    def __init__(self, veristand_sdf_filepath: str = None, xnet_db_folder: str = None) -> None:
        """
        Initialize the XNET DB Utility with the Veristand SDF XML file path.
        """
        if veristand_sdf_filepath is None or xnet_db_folder is None:
            raise ValueError(
                "Invalid Veristand SDF file or XNET DB folder path")

        if not os.path.exists(veristand_sdf_filepath):
            raise ValueError(
                f"Veristand SDF file don't exist:{veristand_sdf_filepath}")

        self.veristand_sdf_filepath = veristand_sdf_filepath
        self.xnet_databases = []
        self.xnet_db_folder = xnet_db_folder

    def register_xnet_databases(self):
        """
        Register NI XNET Databases defined in DSF XML file
        """
        # Check if XML file exists
        if not os.path.isfile(self.veristand_sdf_filepath):
            raise FileNotFoundError(
                f"Given XML file not found:{self.veristand_sdf_filepath}")

        db_aliases = self._read_xnet_databases()

        for db_alias in db_aliases:
            xnet_db_file_path = os.path.join(
                self.xnet_db_folder, db_alias + ".xml")
            self._add_db(database_alias=db_alias,
                         database_filepath=xnet_db_file_path)

    def unregister_xnet_databases(self):
        """
        Unregister NI XNET Databases
        """
        if len(self.xnet_databases) == 0:
            raise IndexError(
                "No databases fetched from SDF file and registered.")

        for db_alias in self.xnet_databases:
            self._remove_db(database_alias=db_alias)

    def _read_xnet_databases(self):
        """
        Reads XNET Databases from the XML file and stores them in the dictionary with section names as prefixes.

        *Returns:*

        (dict): A dictionary where keys are prefixed XNET DB channel names and values are the corresponding paths.
        """
        tree = ET.parse(self.veristand_sdf_filepath)
        root = tree.getroot()

        # Start parsing from the 'Root' element
        root_section = root.find('.//Root')
        if root_section is not None:
            self._parse_section(root_section, [])

        return self.xnet_databases

    def _parse_section(self, section, section_names):
        """
        Recursively parses a section and its sub-sections.

        *Arguments:*

        section (xml.etree.ElementTree.Element): The current XML section element.
        section_names (list): The list of parent section names.
        """
        for child in section:
            # Only dive into certain XML elements
            if child.tag in ['TargetSections', 'Target', 'Section']:
                if "XNET Databases" in section_names:
                    self.xnet_databases += [child.get('Name')]
                else:
                    # Append the current section name and continue parsing
                    current_section_name = child.get('Name')
                    self._parse_section(child, section_names +
                                        [current_section_name])

    def _check_db_exists(self, database_alias: str = None):
        """
        Checks whether Alias-named database is already mapped to system.

        *Arguments:*

        database_alias (str): Name of the database

        *Returns:*

        (bool): True, when database found by Alias.
        """
        if database_alias is None:
            raise ValueError("No database alias given.")

        with system.System() as my_system:
            if database_alias in my_system.databases.keys():
                return True

        return False

    def _add_db(self, database_alias: str = None, database_filepath: str = None):
        """
        Adds Alias-named database to system.

        *Arguments:*

        database_alias (str): Name of the database
        database_filepath (str): The path to the database XML file
        """
        if database_alias is None or database_filepath is None:
            raise ValueError("No alias or database path given.")

        if not os.path.exists(database_filepath):
            raise ValueError(f"{database_filepath} don't exist.")

        with system.System() as my_system:
            if not self._check_db_exists(database_alias):
                my_system.databases.add_alias(
                    database_alias, database_filepath)

    def _remove_db(self, database_alias: str = None):
        """
        Removes Alias-named database from system.

        *Arguments:*

        database_alias (str): Name of the database
        """
        if database_alias is None:
            raise ValueError("No database alias given.")

        with system.System() as my_system:
            del my_system.databases[database_alias]
