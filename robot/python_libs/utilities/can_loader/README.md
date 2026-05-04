[[_TOC_]]
TODO
# Introduction

- Generates temporary *.bat* and *.txt* files and uses them to execute canLoader.
- This library does neither handle setting the DUT or BSL-pin to specific state nor handle power-on reset cycles.

# Preconditions

At default, this library uses *canLoader2.exe* and *canLoader2.dll* files from this directory. If user wants use some other version of these files, user should call the *configure_connection()*-method to set the source directory (*source_dir*).

## This library and canLoader2 files
- can_loader.py
- canLoader2.dll
- canLoader2.exe

## User files
- This library can be used to clone user script files (*.txt*) to execution folder: *target_dir*
- If some script file references to binary file (e.g., canLoader 'load some_binary.bin'-command is used), the binary file must exist in the same folder as the script file. This library will try to copy the references binaries to target directory.
- This library will sanitize binary names by removing dots. This does not affect the original files.
  - Binary names are also sanitized from *.txt files. For example mc_boot_4.1.531.bin will become mc_boot_4_1_531.bin.

# Default values for optional parameters for this library
- canLoader bitrate = 1000k
- Source directory = The directory of this library
- Target directory = $cwd/~canloader/

# Usage

1. Import library
   - It's possible to set mandatory parameters at import: *can_card_serial* and *device_serial_number*
2. Configure Connection (Optional)
   - It's possible to configure all mandatory and optional parameters
3. Generates Files For Canloader
   1. Call this for each user script file (one or multiple calls) to be executed
   2. Library generates target folder for all temp files
   3. Library handles generating temp script files based on user file
   4. Library sanitizes binary calls, by removing extra dots (Does not affect the original files)
   5. If some external binary file is referenced, the library copies the binary to target folder
      1. Binary names are sanitized as well. (Does not affect the original files)
4. Execute Update
   1. Library copies canLoader2 .exe and .dll files to target folder
   2. Library handles generating login script with correct serial number
   3. Library handles generating login batch file
   4. Library checks that all the required files are found in the target folder
   5. Library executes the login command
   6. Library executes all defined script files
   7. Removes target directory, if remove_target_dir is set to True.
5. Generates Files For Canloader And Execute Update
   1. Does the same thing as Step3 but possibility to use multiple files (list)
   2. Does the same thing as Step4 for all files
6. Cleanup files
   1. If user wants to run update scripts multiple times (with different content), it's mandatory to clean up files to be executed so that the library does not run some old update scripts multiple times.
   2. Old script files are NOT REMOVED (by default) from disc though, since the cleanup only removes all items from internal list variable.
      1. Target directory IS REMOVED if remove_target_dir is set to True.