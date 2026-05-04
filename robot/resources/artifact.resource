*** Settings ***
Documentation       Resource file for DUT related variables.

Resource            libraries_and_variables.resource


*** Keywords ***
Read FW Version From Artifact Info File
    [Documentation]     Reads FW version from firmware txt file
    [Arguments]         ${info_file}=${FW_INFO_FILE}

    ${file_content} =   OperatingSystem.Get File    path=${info_file}

    ${fw_version} =     String.Get Line             string=${file_content}      line_number=0
    ${fw_version} =     String.Get Substring        string=${fw_version}        start=9

    RETURN    ${fw_version}

Read ETPU Version From Artifact Info File
    [Documentation]     Reads ETPU version from firmware txt file
    [Arguments]         ${info_file}=${FW_INFO_FILE}

    ${file_content} =    OperatingSystem.Get File   path=${info_file}

    ${etpu_version} =    String.Get Line            string=${file_content}  line_number=1
    ${etpu_version} =    String.Get Substring       string=${etpu_version}  start=5

    RETURN    ${etpu_version}

Read APP Version From Artifact Info File
    [Documentation]     Reads APP version from application txt file
    [Arguments]         ${info_file}

    ${file_content} =   OperatingSystem.Get File    path=${info_file}

    ${app_version} =    String.Get Line         string=${file_content}  line_number=0
    ${app_version} =    String.Get Substring    string=${app_version}   start=12

    RETURN    ${app_version}
