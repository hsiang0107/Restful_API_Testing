*** Settings ***
Resource  custom_intelligence_variable.robot

*** Keywords ***
Click Add UDSO
    Click Element  css=${UDSO_ADD}
    Wait Until Page Contains Element  css=${UDSO_ADD_TABLE}

Select UDSO Add Type
    [Arguments]  ${type}
    Select From List By Label  css=${UDSO_ADD_TYPE}  ${type}

Switch To Frame UDSO
    Wait Until Page Contains Element  css=${FRAME_UDSO}
    Select Frame  css=${FRAME_UDSO}
