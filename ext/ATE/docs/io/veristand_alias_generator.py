"""
Create VeriStand aliases script
=================

Script that processes excel and creates csv file for VeriStand import
"""
import sys
import csv
import openpyxl

class veristand_alias_generator:
    """
    Class to generate VeriStand aliases txt file from excel file
    """
    def __init__(self, veristand_xlsx_path, alias_csv_path) -> None:
        """
        Initialize class variables.
        """
        self.alias_list = []
        self.veristand_xlsx_path = veristand_xlsx_path
        self.alias_csv_path = alias_csv_path

    def process_xlsx(self, sheet_name='Aliases', start_row=2, alias_path_column=0, channel_path_column=1):
        """
        Processes excel rows and columns to get alias path and channel paths.

        :param sheet_name(str): Excel sheet name where alias mapping exists.
        :param start_row(int): The row of excel sheet from which the processing is started.
        :param alias_path_column(int): The column of excel sheet from which the alias names are extracted.
        :param channel_path_column(int): The column of excel sheet from which the channel paths are extracted.
        """
        # data_only = True --> Get the values of the cells, not formulas
        wb = openpyxl.load_workbook(self.veristand_xlsx_path, data_only=True, read_only=True)
        # Define variable to read sheet
        ws = wb[sheet_name]

        # Init list for rows in CSV
        skip_list=['TBD', 'NONE', '0']

        # Iterate all rows to read the cell values
        for i, row in enumerate(ws.iter_rows(min_row=start_row, values_only=True)):
            alias_path = str(row[alias_path_column])
            channel_path = str(row[channel_path_column])
            # Skip values which are forbidden
            if (alias_path.upper() in skip_list or
                channel_path.upper() in skip_list):
                print(f"Skipped row: {i+1:<5} Channel Path: {channel_path:<120} Alias Path: {alias_path}")
            else:
                # Append values to list
                self.alias_list.append([channel_path, alias_path])
        # Get all rows
        max_rows = ws.max_row
        print(f"Number of all rows processed: {max_rows}")


    # Write Alias list to CSV file
    def csv_writer(self):
        """
        Processes the list of aliases (including channel paths) and writes them into file in csv format.
        """
        with open(self.alias_csv_path, 'w', newline='', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, delimiter='\t',        # Use tab to separate values (VeriStand native format)
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(self.alias_list)

if __name__ == "__main__":
    VERISTAND_XLSX_PATH = "ATE IO Mappings.xlsx"
    ALIAS_CSV_PATH = "generated_aliases.txt"
    argv = sys.argv[1:]

    if 0 < len(argv) >= 2:
        VERISTAND_XLSX_PATH = argv[0]
        ALIAS_CSV_PATH = argv[1]

    alias_generator = veristand_alias_generator(VERISTAND_XLSX_PATH, ALIAS_CSV_PATH)
    alias_generator.process_xlsx()
    alias_generator.csv_writer()
