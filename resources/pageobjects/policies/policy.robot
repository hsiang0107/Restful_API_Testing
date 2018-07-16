*** Settings ***
Resource  policy_variables.robot

*** Keywords ***
Verify Filter Options
    Wait Until Page Contains Element  css= ${POLICY_TYPE_FILTER_RADIO}
    Click Element  css=${POLICY_TYPE_FILTER_RADIO}
    Click Element  css=${POLICY_SET_FILTER_BUTTON}
    Click Element  css=${POLICY_DIRECTORIES_CHECKBOX}
    Select From List By Label  css=${POLICY_DIRECTORIES_DROPDOWN}  Product Directory
    Element Should Be Visible  css=${POLICY_PRODUCT_DIRECTORY_AREA}
    Select From List By Label  css=${POLICY_DIRECTORIES_DROPDOWN}  Active Directory
    Element Should Be Visible  css=${POLICY_AD_DIRECTORY_AREA}
    Select From List By Label  css=${POLICY_DIRECTORIES_DROPDOWN}  OfficeScan domain hierarchy
    Element Should Be Visible  css=${POLICY_OFFICESCAN_DOMAIN_HIERARCHY_AREA}

Close Welcome Window
    Wait Until Page Contains Element  css=${HOW_TO_DIALOG_CLOSE_BUTTON}  timeout=20
    Click Element  css=${HOW_TO_DIALOG_CLOSE_BUTTON}

Select Product Type
    [Arguments]  ${product_type}
    Wait Until Page Contains Element  css= ${PRODUCT_ID_DROPDOWN}  timeout=30
    Select From List By Label  css=${PRODUCT_ID_DROPDOWN}  ${product_type}
