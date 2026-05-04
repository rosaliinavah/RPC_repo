"""
File which implements class to parse CSV file which describes data for Slave type of EPEC product.
"""
import csv
import os


class pdo_item:
    """
    Class to represent a PDO item.
    """

    def __init__(self) -> None:
        """
        Initialize a new instance of the pdo_item class.
        """
        self.pdo_index = None
        self.pdo_hex = None
        self.pdo_dec = None
        self.transmission_type = None
        self.inhibit_time = None
        self.event_timer = None
        self.sync_start_value = None
        self.data = []  # [index:subindex's parameters name]

    def get_by_hex(self, hex_value):
        """
        Check if the given hex value matches the PDO's hex value.

        *Arguments:*

        hex_value (str): The hexadecimal value to compare.

        *Returns:*

        (bool): True if the hex value matches, False otherwise.
        """
        return self.pdo_hex == hex_value

    def get_by_dec(self, dec_value):
        """
        Check if the given decimal value matches the PDO's decimal value.

        *Arguments:*

        dec_value (int): The decimal value to compare.

        *Returns:*

        (bool): True if the decimal value matches, False otherwise.
        """
        return self.pdo_dec == dec_value


class csv_parser:
    """
    Class to parse a CSV file containing PDO items and provide access to the parsed data.

    *Arguments:*

    file_path (str): The path to the CSV file.
    items (list): A list of pdo_item instances parsed from the CSV file.
    """

    def __init__(self, file_path):
        """
        Initialize a new instance of the CsvParser class.

        *Arguments:*

        file_path (str): The path to the CSV file.
        """
        if file_path is None or not os.path.exists(file_path):
            raise ValueError(
                "Invalid file path. Ensure the file exists and the path is correct.")
        self.file_path = file_path
        self.items = self._parse_csv()

    def _parse_csv(self):
        """
        Parse the CSV file and populate the items attribute with pdo_item instances.

        *Returns:*

        (list): A list of pdo_item instances.
        """
        items = []

        with open(self.file_path, 'r', encoding='UTF-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            _ = next(reader)  # Skip header row

            for row in reader:
                item = pdo_item()
                item.pdo_hex = row[0]
                item.pdo_dec = int(row[1])
                item.pdo_index = row[2]
                item.transmission_type = row[3]
                item.inhibit_time = row[4]
                item.event_timer = row[5]
                item.sync_start_value = row[6]

                # Skip first 7 columns as they are fixed attributes
                byte_values = row[7:]

                for value in byte_values:
                    if value:  # Only add non-empty values
                        item.data.append(value.strip())

                items.append(item)

        return items

    def get_pdo_item(self, value):
        """
        Retrieve a pdo_item instance based on the provided hex or decimal value.

        *Arguments:*

        value (str or int): The hex or decimal value to search for.

        *Returns:*

        (pdo_item): The matching pdo_item instance, or None if no match is found.
        """
        if isinstance(value, str) and value.startswith('0x'):
            for item in self.items:
                if item.get_by_hex(value):
                    return item
        elif isinstance(value, int):
            for item in self.items:
                if item.get_by_dec(value):
                    return item

        return None
