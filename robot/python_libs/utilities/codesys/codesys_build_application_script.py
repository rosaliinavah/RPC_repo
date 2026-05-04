"""
This script opens project, builds application and generates version text file.
Used only as input script with CODESYS scripting engine.
"""
from __future__ import print_function

import sys
import os
from io import open

# Codesys using IronPython 2.7 so plus lot of other linting errors
# pylint:disable=consider-using-f-string, invalid-name, deprecated-method, undefined-variable, unused-argument, too-many-instance-attributes
# pylint:disable=consider-using-enumerate, import-error


def create_boot_project(application, output_folder):
    """Cleans, generates code and creates boot application: Application.app to defined folder.

    *Arguments:*

    :param application(ScriptApplication): Codesys ScriptApplication object
    :param output_folder(str): Path to folder which Application.app is built
    :return ret_val(int): 0=Success, 1=Failure
    """
    print("---------------CREATE BOOT PROJECT---------------")
    # Output Application.app to folder defined in argument
    output_path = os.path.join(output_folder, "Application.app")
    print('-APP CLEAN-')
    application.clean()
    print('-APP GENERATE CODE-')
    application.generate_code()
    build_message_guid = "{97f48d64-a2a3-4856-b640-75c046e37ea9}"
    log = system.get_message_objects(
        build_message_guid, severities=Severity.Error)
    print(("---------------BUILD ERRORS FOUND IN PROJECT---------------"), len(log))
    if len(log) != 0:
        for line in log:
            print('ERROR:', line)
            print("--APPLICATION NOT BUILT BECAUSE OF ERRORS--")
        raise RuntimeError("Create application failed")
    print("-CREATE BOOT APPLICATION-")
    application.create_boot_application(
        output_path, update_compile_info=True, write_visu_files=False)
    print("--APPLICATION BUILT TO LOCATION--", output_path)


def get_project_version(project):
    """Gets current project version from Codesys Project Information.

    *Arguments:*

    :param project(ScriptProject): Codesys ScriptProject object
    :return:  version(String): Version as string x.x.x.x
    """
    info = project.get_project_info()
    proj_vers = info.version
    if proj_vers is None:
        version = '0.0.0.0'
        print('Version not found. Set to default: ', version)
    else:
        print('Current version: ', proj_vers)
        version = str(proj_vers)
    return version


def get_project_title(project):
    """Gets current project title from Codesys Project Information.

    *Arguments:*

    :param project(ScriptProject): Codesys ScriptProject object
    :return:  title(String): Title as string
    """
    info = project.get_project_info()
    proj_title = info.title
    if proj_title is None:
        title = 'CICD'
        print('Project title not found. Set to default: ', title)
    else:
        print('Current project title: ', proj_title)
        title = str(proj_title)
    return title


def project_save(project):
    """Saves current project

    *Arguments:*

    :param project(ScriptProject): Codesys ScriptProject object
    """
    print("---------------SAVE PROJECT---------------")
    project.save()
    print('--PROJECT SAVE OK--')


def check_args():
    """Checks arguments given to this script

    """
    print("--------------------CHECK ARGUMENTS--------------------")
    if len(sys.argv) == 3:
        print("--Arguments OK--")
    else:
        print("--Arguments NOT OK--")
        raise RuntimeError("Check arguments failed")


def open_project(project_path):
    """Opens project in CODESYS

    *Arguments:*

    :param project_path(String): Codesys project path to open
    :return project(ScriptProject): Codesys ScriptProject object
    """
    print("---------------------OPEN PROJECT----------------------")
    if projects.primary is not None:
        projects.primary.close()
        system.delay(500)

    project = projects.open(project_path,
                            update_flags=VersionUpdateFlags.SilentMode | VersionUpdateFlags.NoUpdates)
    system.delay(500)
    print("--PROJECT OPENED SUCCESSFULLY--")
    return project


def write_version_file(project, output_folder):
    """Writes version information file for later usage

    *Arguments:*

    :param project(ScriptProject): Codesys ScriptProject object
    :param output_folder(str): Path to folder which Application.txt is written

    """
    print("---------------------WRITE VERSION INFO TO FILE---------------------")
    vers = get_project_version(project)
    title = get_project_title(project)

    # Generate ApplicationTitle and ApplicationVersion string
    file_content = 'app_version=' + vers + '\n' + 'app_title=' + title
    print('Write version info content:\n', file_content)

    filename = 'Application.txt'
    # Output version file to folder defined in argument
    filepath = os.path.join(output_folder, filename)
    print('File path: ', filepath)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(file_content)
        print("--WRITE FILE OK--")


def get_application(project):
    """Saves current project

    *Arguments:*

    :param project(ScriptProject): Codesys ScriptProject object
    :return application(ScriptApplication): Codesys ScriptApplication object
    """
    print("-------------------GET PROJECT ACTIVE APPLICATION-------------------")
    application = project.active_application
    print("Application name: " + str(application.get_name()))

    print("--GET APPLICATION OK--")
    return application


def main():
    """Main function.
    - Opens project in CODESYS
    - Generates version information file Application.txt
    - Builds application and creates Application.app
    - Saves project
    """
    check_args()
    try:
        proj = open_project(sys.argv[1])
        write_version_file(proj, output_folder=sys.argv[2])
        app = get_application(proj)
        create_boot_project(
            application=app, output_folder=sys.argv[2])
    except Exception as e:
        print("Exception: ", e)

    project_save(proj)


if __name__ == '__main__':
    print("---------------START OF PYTHON SCRIPT--------------")
    print("This script opens project, builds application and generates version text file")
    print("Arguments expected:\n- (Script path)\n- Codesys project path\n- Output folder for generated files ")
    print("Sys.argv: ", len(sys.argv), " elements:")
    # Print arguments
    for arg in sys.argv:
        print(" - ", arg)
    main()
