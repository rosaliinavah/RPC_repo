"""
This module provides a class for handling common file system operations.
"""
import os
from pathlib import Path
import zipfile


class file_system_utility:
    """ A utility class for file system operations. """

    def __init__(self):
        """
        This is the constructor of the class where you can initialize attributes or perform setup tasks.
        """

    def find_folder_from_folder_by_prefix(self, path, prefix):
        """
        Search for folders within the given path that start with the specified prefix.

        Args:
        - `path`: Path to search within.
        - `prefix`: Prefix to match folder names against.

        Returns:
        - Name of the first matching folder, or None if no match is found.
        """
        # Ensure the path exists and is a directory
        if not os.path.isdir(path):
            print(f"The path {path} is not a valid directory.")
            return None

        # Iterate over items in the directory
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            # Check if the item is a directory and starts with the prefix
            if os.path.isdir(item_path) and item.startswith(prefix):
                return item  # Return the first matching folder name

        # If no folder matches the prefix
        return None

    def unzip_file(self, src_path, dest_path) -> None:
        """
        Unzips a file from the source path to the destination path.

        Args:
        - `src_path`: Path to the ZIP file to be extracted.
        - `dest_path`: Destination path where contents will be extracted.

        Examples:
        | Unzip File | results.zip | results_folder |
        """
        # Ensure the source path exists and is a file
        if not os.path.isfile(src_path):
            print(f"The source path {src_path} is not a valid file.")
            return

        # Ensure the destination directory exists or create it
        if not os.path.exists(dest_path):
            os.makedirs(dest_path, exist_ok=True)

        # Open the zip file and extract its contents
        with zipfile.ZipFile(src_path, 'r') as zip_ref:
            zip_ref.extractall(dest_path)
            print(f"File extracted successfully to {dest_path}")

    def zip_files(self, zip_name: str, *file_paths) -> None:
        """
        Create a ZIP archive containing the given files.

        This keyword is intended to be used from Robot Framework.
        Each input file is added to the root of the ZIP archive
        using its filename (directory structure is not preserved).

        Args:
        - `zip_name`: Path to the ZIP file to create. If the file already exists, it will be overwritten.
        - `file_paths`: One or more file paths to include in the ZIP archive. Can be passed as multiple keyword args or as a list.

        Raises:
        - `FileNotFoundError`: If any of the input files do not exist.
        - `ValueError`: If no input files are provided.

        Examples:
        | Zip Files  | results.zip  | out.txt      | log.txt |
        | VAR        | @{file_list} | out.txt      | log.txt |
        | Zip Files  | results.zip  | ${file_list} |
        """
        if not file_paths:
            raise ValueError("At least one file must be provided")

        zip_path = Path(zip_name)
        # If single argument and it's a list/tuple → unwrap
        if len(file_paths) == 1 and isinstance(file_paths[0], (list, tuple)):
            files = list(file_paths[0])
        else:
            files = list(file_paths)

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for file in files:
                path = Path(file)
                print(path)

                if not path.exists():
                    raise FileNotFoundError(f"File not found: {path}")

                # Store file without directory structure
                zip_file.write(path, arcname=path.name)
