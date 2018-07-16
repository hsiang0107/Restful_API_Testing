*** Settings ***
Resource  AD_compliance_variable.robot
Library  String

*** Variable ***
@{compliance_list_values}  Latest Only  1 version old or newer  2 versions old or newer  3 versions old or newer  4 versions old or newer  5 versions old or newer

*** Keywords ***
Go To AD Setting
    Click Element  css=${AD_SETTING_TAB}

Go To Compliance
    Click Element  css=${COMPLIANCE_TAB}

Go To Sites
    Click Element  css=${SITES_TAB}

Go To Reporting Lines
    Click Element  css=${REPORTING_LINES_TAB}

Enable AD Setting
    Click Element  css=${AD_SETTING_ON_OFF_CHECKBOX}

Click Add AD Setting
    ${count}=  Get Element Count  css=input[type=\"password\"]
    Run Keyword If  ${count}==1  Click Element  css=${AD_SETTING_ADD_FIRST_BUTTON}
    ...  ELSE  Click Dynamic Add AD Setting  ${count}

Click Dynamic Add AD Setting
    [Arguments]  ${index}
    ${locator}=  Get Correct AD Locator For Dynamic Element  ${AD_SETTING_ADD_BUTTON}  ${index}
    Click Element  css=${locator}

Remove AD Setting
    [Arguments]  ${index}
    ${locator}=  Get Correct AD Locator For Dynamic Element  ${AD_SETTING_REMOVE_BUTTON}  ${index}
    Click Element  css=${locator}

Get Correct AD Locator For Dynamic Element
    [Arguments]  ${locator}  ${index}
    ${index}=  Evaluate  ${index}+1
    ${index}=  Convert To String  ${index}
    ${correct_locator}=  Replace String  ${locator}  <REPLACE_ME>  ${index}
    [Return]  ${correct_locator}

Check AD Setting Page Should Have Element
    Page Should Contain Element  css=${AD_SETTING_SAVE_BUTTON}

Check Compliance Page Should Have Elements
    Page Should Contain Element  css=${COMPLIANCE_ADD_EXCEPTION_BUTTON}
    Page Should Contain Element  css=${COMPLIANCE_SAVE_BUTTON}
    Page Should Contain Element  css=${COMPLIANCE_CANCEL_BUTTON}
    List Should Have Values  css=${COMPLIANCE_PATTERN_VERSION_SELECT_DROPDOWN}  ${compliance_list_values}
    Page Should Contain Element  css=${COMPLIANCE_LOW_SCROLL}
    Page Should Contain Element  css=${COMPLIANCE_HIGH_SCROLL}

Check Sites Page Should Have Elements
    Page Should Contain Element  css=${ADD_CUSTOM_BUTTON}
    Page Should Contain Element  css=${DELETE_CUSTOM_BUTTON}
    Page Should Contain Element  css=${MERGE_CUSTOM_BUTTON}
    Page Should Contain Element  css=${SPLIT_CUSTOM_BUTTON}
