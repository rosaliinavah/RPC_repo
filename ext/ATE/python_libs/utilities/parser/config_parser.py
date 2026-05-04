"""
File containing config_parser class. This is a keyword wrapper for Robot Framework.

This class wraps functionalities from ConfigParser.

Used to create, read and modify .cfg/.ini files in the following format:

[Section 1]
Key = Value

[Section 2]
Key_2 = Value_2
"""
import configparser
import os
import tempfile
import shutil
from pathlib import Path
from typing import Optional, List, Dict, Union, Any
from robot.api import logger


class config_parser:
    """Robot Framework library for configuration file operations using ConfigParser.

    Provides keywords for managing INI-style configuration files commonly used
    in embedded systems and automation projects. Supports reading, writing, and
    manipulating configuration files with proper error handling.

    Attributes:
    - `ROBOT_LIBRARY_SCOPE`: Suite-level scope for the library
    """

    ROBOT_LIBRARY_SCOPE = "SUITE"

    def __init__(self) -> None:
        """Initialize the ConfigParser wrapper.

        Creates a new ConfigParser instance and initializes file path tracking.
        """
        self.config = configparser.ConfigParser()
        self.config_file_path: Optional[str] = None

    # ============================================================================
    # PUBLIC METHODS - Robot Framework Keywords
    # ============================================================================

    def load_config_file(self, file_path: str, encoding: str = 'utf-8') -> None:
        """Load a configuration file from the specified path.

        Reads and parses an existing configuration file into memory for manipulation.
        The file path is stored for use with save operations.

        Arguments:
        - `file_path`: Path to the configuration file to load
        - `encoding`: File encoding to use when reading the file (default: utf-8)

        Raises:
        - `RuntimeError`: If the file cannot be found or loaded

        Examples:
        | Load Config File | ${CURDIR}/config/settings.ini |       | # Load config from current directory
        | Load Config File | /etc/myapp/config.ini         |       | # Load config with absolute path
        | Load Config File | config.ini                    | utf-8 | # Load with explicit encoding
        """
        resolved_path = str(Path(file_path).resolve())
        if not os.path.exists(resolved_path):
            raise RuntimeError(
                f"Configuration file not found: {resolved_path}")

        try:
            self.config.read(resolved_path, encoding=encoding)
            self.config_file_path = resolved_path
            logger.info(
                f"Successfully loaded configuration file: {resolved_path}")
        except Exception as e:
            raise RuntimeError(
                f"Failed to load configuration file '{file_path}': {e}") from e

    def create_new_config_file(self, file_path: str) -> None:
        """Create a new empty configuration file and load it into memory.

        Creates a new ConfigParser instance and saves an empty configuration
        file to the specified path. Directory structure is created if needed.

        Arguments:
        - `file_path`: Path where the new configuration file should be created

        Raises:
        - `RuntimeError`: If the file cannot be created

        Examples:
        | Create New Config File | ${TEMPDIR}/new_config.ini | # Create new config file
        | Add Config Section     | application               | # Add section to new config
        | Set Config Value       | application | name | MyApp | # Add configuration value
        """
        self.config = configparser.ConfigParser()
        resolved_path = str(Path(file_path).resolve())
        os.makedirs(os.path.dirname(resolved_path), exist_ok=True)

        try:
            # Create empty file
            with open(resolved_path, 'w', encoding='utf-8') as configfile:
                self.config.write(configfile)
            self.config_file_path = resolved_path
            logger.info(f"Created new configuration file: {resolved_path}")
        except Exception as e:
            raise RuntimeError(
                f"Failed to create configuration file '{file_path}': {e}") from e

    def add_config_section(self, section: str) -> None:
        """Add a new configuration section.

        Creates a new section in the configuration if it doesn't already exist.
        If the section already exists, no action is taken and no error is raised.

        Arguments:
        - `section`: Section name to create

        Raises:
        - `RuntimeError`: If there's an error creating the section

        Examples:
        | Add Config Section | new_feature  | # Create new feature section
        | Set Config Value   | new_feature  | enabled | true  | # Add option to new section
        | Add Config Section | logging      | # Create logging section
        """
        try:
            if not self.config.has_section(section):
                self.config.add_section(section)
                logger.info(f"Added configuration section: {section}")
            else:
                logger.warn(f"Section '{section}' already exists")
        except Exception as e:
            raise RuntimeError(
                f"Failed to add section '{section}': {e}") from e

    def set_config_value(self, section: str, option: str, value: Union[str, int, bool]) -> None:
        """Set a configuration value in memory.

        If the specified section does not exist, it will be created automatically.
        Changes are only in memory until saved with Save Config File.

        Arguments:
        - `section`: Configuration section name
        - `option`: Option/key name within the section
        - `value`: Value to set (converted to string for storage)

        Raises:
        - `RuntimeError`: If there's an error setting the value

        Examples:
        | Set Config Value | database | host  | localhost | # Set database host
        | Set Config Value | database | port  | 3306      | # Set database port
        | Set Config Value | app      | debug | ${True}   | # Set boolean value
        """
        try:
            if not self.config.has_section(section):
                self.config.add_section(section)
            self.config.set(section, option, str(value))
            logger.info(f"Set config value: [{section}] {option} = {value}")
        except Exception as e:
            raise RuntimeError(
                f"Failed to set config value [{section}] {option}: {e}") from e

    def save_config_file(self, file_path: Optional[str] = None, whitespace: bool = False) -> None:
        """Save the current configuration to a file using atomic write operations.

        If no file path is provided, saves to the originally loaded file path.
        The write operation is atomic to prevent corruption during concurrent access.

        Arguments:
        - `file_path`: Path to save the file (optional, uses loaded path if not specified)
        - `whitespace`: If set to True, there will be whitespace between the delimiters.
            key=value -> key = value

        Raises:
        - `RuntimeError`: If no file path is available or file cannot be saved

        Examples:
        | Save Config File |                           | # Save to originally loaded path
        | Save Config File | /backup/config_backup.ini | # Save to specific backup location
        | Save Config File | ${TEMPDIR}/test_config.ini| # Save to temporary location
        """
        save_path = file_path or self.config_file_path
        if not save_path:
            raise RuntimeError(
                "No file path specified and no file was previously loaded")

        resolved_save_path = str(Path(save_path).resolve())
        dest_dir = os.path.dirname(resolved_save_path)
        os.makedirs(dest_dir, exist_ok=True)

        try:
            # Atomic write: write to temp file then move
            with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=dest_dir, delete=False) as tmp_file:
                self.config.write(tmp_file, space_around_delimiters=whitespace)
                tmp_name = tmp_file.name
            shutil.move(tmp_name, resolved_save_path)
            self.config_file_path = resolved_save_path
            logger.info(f"Configuration saved to: {resolved_save_path}")
        except Exception as e:
            raise RuntimeError(
                f"Failed to save configuration file: {e}") from e


    # ============================================================================
    # PRIVATE METHODS - Available for internal use but hidden from Robot Framework
    # ============================================================================

    def _get_config_value(self, section: str, option: str, fallback: Optional[Any] = None,
                          return_type: str = 'str') -> Union[str, int, bool, float]:
        """Get a value from the configuration file with specified return type.

        Retrieves a configuration value and converts it to the specified type.
        Supports automatic type conversion for common data types used in configuration files.

        Arguments:
        - `section`: Configuration section name
        - `option`: Option/key name within the section
        - `fallback`: Default value if option is not found (should match return_type)
        - `return_type`: Type to return the value as ('str', 'int', 'bool', 'float')

        Returns:
        The configuration value in the specified type

        Raises:
        - `RuntimeError`: If section/option not found, no fallback provided, invalid type conversion, or unsupported return_type

        Examples:
        | ${host}=      | Get Config Value | database | host      |           |           | # Get string value
        | ${port}=      | Get Config Value | database | port      | 5432      | int       | # Get integer with fallback
        | ${debug}=     | Get Config Value | app      | debug     | ${True}   | bool      | # Get boolean value
        | ${threshold}= | Get Config Value | sensor   | temp_limit| 25.5      | float     | # Get float value
        """
        # Initialize value to None to remove linter error
        value = None
        # Validate return_type
        valid_types = {'str', 'int', 'bool', 'float'}
        if return_type not in valid_types:
            raise RuntimeError(
                f"Unsupported return_type '{return_type}'. Valid types: {valid_types}")

        try:
            # Use appropriate ConfigParser method based on return_type
            if return_type == 'str':
                value = self.config.get(section, option, fallback=fallback)
            elif return_type == 'int':
                value = self.config.getint(section, option, fallback=fallback)
            elif return_type == 'bool':
                value = self.config.getboolean(
                    section, option, fallback=fallback)
            elif return_type == 'float':
                value = self.config.getfloat(
                    section, option, fallback=fallback)

            logger.info(
                f"Retrieved config {return_type}: [{section}] {option} = {value}")
            return value

        except configparser.NoSectionError as e:
            raise RuntimeError(
                f"Section '{section}' not found in configuration") from e
        except configparser.NoOptionError as e:
            if fallback is not None:
                logger.info(
                    f"Using fallback {return_type} for [{section}] {option} = {fallback}")
                return fallback
            raise RuntimeError(
                f"Option '{option}' not found in section '{section}'") from e
        except ValueError as e:
            raise RuntimeError(
                f"Invalid {return_type} value for [{section}] {option}: {e}") from e
        except Exception as e:
            raise RuntimeError(
                f"Failed to get config value [{section}] {option}: {e}") from e

    def _config_section_exists(self, section: str) -> bool:
        """Check if a configuration section exists.

        Verifies whether a named section is present in the loaded configuration.
        Useful for conditional logic in test cases.

        Arguments:
        - `section`: Section name to check

        Returns:
        True if the section exists, False otherwise

        Examples:
        | ${exists}=       | Config Section Exists | database    | # Check if database section exists
        | Should Be True   | ${exists}             |             | # Verify section exists
        | Run Keyword If   | ${exists}             | Log         | Database configured
        """
        exists = self.config.has_section(section)
        logger.info(f"Section '{section}' exists: {exists}")
        return exists

    def _config_option_exists(self, section: str, option: str) -> bool:
        """Check if a configuration option exists in a section.

        Verifies whether a specific option is present within a given section.
        Useful for validating configuration completeness.

        Arguments:
        - `section`: Section name to check in
        - `option`: Option name to check for

        Returns:
        True if the option exists, False otherwise

        Examples:
        | ${has_port}= | Config Option Exists | database | port     | # Check for port option
        | ${has_ssl}=  | Config Option Exists | database | ssl_mode | # Check for SSL configuration
        """
        exists = self.config.has_option(section, option)
        logger.info(f"Option '[{section}] {option}' exists: {exists}")
        return exists

    def _get_config_sections(self) -> List[str]:
        """Get all section names from the configuration.

        Returns a list of all sections defined in the configuration file.
        Useful for iterating over all configuration areas.

        Returns:
        List of section names

        Examples:
        | @{sections}= | Get Config Sections |                | # Get all section names
        | FOR          | ${section}          | IN @{sections} | # Iterate through sections
        |              | Log                 | Found section: ${section} |
        | END          |                     |                |
        """
        sections = self.config.sections()
        logger.info(f"Configuration sections: {sections}")
        return sections

    def _get_config_options(self, section: str) -> List[str]:
        """Get all option names from a configuration section.

        Returns a list of all options (keys) defined within a specific section.
        Useful for discovering available configuration parameters.

        Arguments:
        - `section`: Section name to get options from

        Returns:
        List of option names in the section

        Raises:
        - `RuntimeError`: If the section does not exist

        Examples:
        | @{options}= | Get Config Options | database  | # Get all database options
        | @{app_opts}=| Get Config Options | app       | # Get all app options
        """
        try:
            options = self.config.options(section)
            logger.info(f"Options in section '{section}': {options}")
            return options
        except configparser.NoSectionError as e:
            raise RuntimeError(
                f"Section '{section}' not found in configuration") from e

    def _get_config_section_as_dictionary(self, section: str) -> Dict[str, str]:
        """Get all key-value pairs from a section as a dictionary.

        Converts an entire configuration section into a Python dictionary.
        Useful for bulk operations or when working with dynamic configurations.

        Arguments:
        - `section`: Section name to convert to dictionary

        Returns:
        Dictionary containing all option-value pairs from the section

        Raises:
        - `RuntimeError`: If the section does not exist

        Examples:
        | &{db_config}= | Get Config Section As Dictionary | database | # Get database config as dict
        | Log           | Host: ${db_config}[host]         |          | # Access dictionary values
        | Log           | Port: ${db_config}[port]         |          | # Access port from dict
        """
        try:
            section_dict = dict(self.config.items(section))
            logger.info(f"Section '{section}' as dictionary: {section_dict}")
            return section_dict
        except configparser.NoSectionError as e:
            raise RuntimeError(
                f"Section '{section}' not found in configuration") from e

    def _remove_config_section(self, section: str) -> None:
        """Remove a configuration section and all its options.

        Deletes an entire section and all options within it from the configuration.
        If the section doesn't exist, no action is taken and no error is raised.

        Arguments:
        - `section`: Section name to remove

        Raises:
        - `RuntimeError`: If there's an error removing the section

        Examples:
        | Remove Config Section | deprecated_feature | # Remove old feature section
        | Remove Config Section | temp_settings      | # Remove temporary configuration
        """
        try:
            if not self.config.has_section(section):
                logger.warn(f"Section '{section}' does not exist")
                return
            self.config.remove_section(section)
            logger.info(f"Removed configuration section: {section}")
        except Exception as e:
            raise RuntimeError(
                f"Failed to remove section '{section}': {e}") from e

    def _remove_config_option(self, section: str, option: str) -> None:
        """Remove a specific configuration option from a section.

        Deletes a single option from the specified section while leaving other
        options in the section intact. If the option doesn't exist, no action is taken.

        Arguments:
        - `section`: Section containing the option
        - `option`: Option name to remove

        Raises:
        - `RuntimeError`: If there's an error removing the option

        Examples:
        | Remove Config Option | database | old_password | # Remove deprecated password option
        | Remove Config Option | app      | temp_setting | # Remove temporary setting
        """
        try:
            if not self.config.has_option(section, option):
                logger.warn(f"Option '[{section}] {option}' does not exist")
                return
            self.config.remove_option(section, option)
            logger.info(f"Removed configuration option: [{section}] {option}")
        except Exception as e:
            raise RuntimeError(
                f"Failed to remove option '[{section}] {option}': {e}") from e

    def _clear_config(self) -> None:
        """Clear all configuration data from memory.

        Creates a new empty ConfigParser instance and resets file path tracking.
        Does not affect files on disk - only clears the in-memory configuration.

        Examples:
        | Clear Config      |                     | # Clear all configuration from memory
        | ${sections}=      | Get Config Sections | # Verify configuration is empty
        | Length Should Be  | ${sections}         | 0   | # Should have no sections
        """
        self.config = configparser.ConfigParser()
        self.config_file_path: Optional[str] = None
        logger.info("Configuration data cleared from memory")
