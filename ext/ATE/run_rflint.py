"""
Script to run robocop from command prompt.

Examples:
| python | run_rflint.py | ./robot/tests |
| python | run_rflint.py | ./robot/tests/example_test.robot |
| python | run_rflint.py | ./robot/tests | ./robot/tests/example_test.robot |
"""
import os
import sys
import subprocess
from pathlib import Path
from typing import List

CONFIG_FILE = "robocop.toml"


def lint_files(file_paths: List[str]) -> int:
    """Robot lint file(s) from the specified path(s).

    Executes robocop linting tool on provided Robot Framework files or directories.
    Prints linting results to console and returns appropriate exit code based on
    findings.

    Args:
    - `file_paths`: List of file or directory paths containing Robot Framework files (.robot, .resource)

    Returns:
    - Exit code (0 for success, non-zero for issues found)
    """
    try:
        # Get the directory where this script is located
        script_dir = Path(__file__).parent.resolve()

        # Find config file in the same folder
        config_file = script_dir / CONFIG_FILE

        # Check if config file exists
        if config_file.exists():
            print(f"Using config file: {config_file}")
        else:
            print(f"Config file not found: {config_file}")

        # Convert paths to string format
        paths = [os.fspath(path) for path in file_paths]
        print(f"Linting paths: {paths}")

        # Run robocop using subprocess with config file
        cmd = [sys.executable, "-m", "robocop", "check"]

        if config_file.exists():
            cmd.extend(["--config", str(config_file)])

        cmd.extend(paths)

        result = subprocess.run(cmd, capture_output=False, check=False)

        return result.returncode

    except Exception as e:
        print(f"Error during linting: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_rflint.py <file(s) or folder(s)>")
        sys.exit(1)

    files_or_folders = sys.argv[1:]
    exit_code = lint_files(files_or_folders)

    if exit_code == 0:
        print("Linting passed successfully!")
    else:
        print(
            f"Linting found issues (exit code: {exit_code})", file=sys.stderr)
