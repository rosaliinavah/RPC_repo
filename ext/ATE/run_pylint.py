"""
    Script to run pylint from command prompt.

    Examples:
    | python | run_pylint.py | ./python_libs/interfaces |
    | python | run_pylint.py | ./python_libs/interfaces/veristand/veristand.py |
"""
import os
import sys
from pylint.lint import Run


def lint_files(file_paths) -> None:
    """ Pylint file(s) from the path.

    Exit codes:
      (1): Invalid file or folder.
      (2): Fatal errors when linting files.
      (3): Errors when linting files.
      (4): Linting score is not met.

    Args:
        file_paths (str): Path where python files are located.

    Raises:
        SystemExit: Raised when exit code is not 0 during function call.

    """
    exit_code = 0
    for file_path in file_paths:
        if os.path.isfile(file_path) and file_path.endswith('.py') and '__init__' not in file_path:
            results = Run([file_path], exit=False)
            if results.linter.stats.fatal > 0:
                print(
                    f"Fatal errors({results.linter.stats.fatal}) in file: {file_path}")
                exit_code = 2
            elif results.linter.stats.error > 0:
                print(
                    f"Errors({results.linter.stats.error}) in file: {file_path}")
                exit_code = 3
            elif results.linter.stats.global_note < 9.0:
                print(
                    f"The code in {file_path} does not meet the required rating (>= 9.0).")
                exit_code = 4

        elif os.path.isdir(file_path):
            python_files = [os.path.join(root, f) for root, _, files in os.walk(
                file_path) for f in files if f.endswith('.py') and '__init__' not in f]
            print(f"FILES:{python_files}")
            results = Run(python_files, exit=False)
            if results.linter.stats.fatal > 0:
                print(
                    f"Fatal errors({results.linter.stats.fatal}) in file: {file_path}")
                exit_code = 2
            elif results.linter.stats.error > 0:
                print(
                    f"Errors({results.linter.stats.error}) in file: {file_path}")
                exit_code = 3
            elif results.linter.stats.global_note < 9.0:
                print(
                    f"The code in one of the files in {file_path} does not meet the required rating (>= 9.0).")
                exit_code = 4
        else:
            print(f"Invalid file or folder: {file_path}")
            exit_code = 1

    if exit_code == 0:
        print("Linting passed successfully! Code meets the required rating (>= 9.0).")
    else:
        print("Linting failed!")
        sys.exit(exit_code)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pylint.py <file or folder>")
        sys.exit(1)
    files_or_folders = sys.argv[1:]
    lint_files(files_or_folders)
