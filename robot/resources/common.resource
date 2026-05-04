*** Settings ***
Documentation       Common keywords for all other libraries to use.

Resource            libraries_and_variables.resource


*** Keywords ***
Create List Of Given Values
    [Documentation]    Create list by given arguments
    [Arguments]   ${length}=1   ${value}=0

    ${list} =   Create List
    FOR   ${_}   IN RANGE   ${length}
        Append To List   ${list}   ${value}
    END
    RETURN   ${list}

Compare Numbers As Bits
    [Documentation]    Bitwise XOR operation. The evaluate expression returns zero when the numbers are equal which results to passed.
    [Arguments]        ${value}    ${expected}

    # Convert expected value to list
    ${expected_list} =  BuiltIn.Evaluate    ${expected} if type(${expected}) is list else [${expected}]
    # Convert to int and sum all values in list
    ${sum} =            BuiltIn.Evaluate    sum(map(int, ${expected_list}))
    # Bitwise XOR values
    ${ret} =            BuiltIn.Evaluate    ${value} ^ ${sum}
    # Test is passed if the outcome of the XOR is zero.
    Should Not Be True    ${ret}
