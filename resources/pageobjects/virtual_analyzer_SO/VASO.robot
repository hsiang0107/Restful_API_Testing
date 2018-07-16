*** Settings ***
Resource  VASO_variable.robot

*** Keywords ***
Expire VASO Now
    Click Element  css=${VASO_EXPIRE_NOW}
    Confirm Action

Click Exception Tab
    Wait Until Page Contains Element  css=${VASO_EXCEPTION_TAB}
    Click Link  css=${VASO_EXCEPTION_TAB}

Click VASO Tab
    Click Element  css=${VASO_TAB}

Select All Objects
    Click Element  css=${VASO_SELECT_ALL}

Deselect All Objects
    Click Element  css=${VASO_SELECT_ALL}

Export All
    Click Element  css=${VASO_EXCEPTION_EXPORT_ALL}

Click Add Exception
    Wait Until Page Contains Element  css=${VASO_EXCEPTION_ADD}
    Wait Until Element Is Visible  css=${VASO_EXCEPTION_ADD}  5
    Sleep  3s
    Click Element  css=${VASO_EXCEPTION_ADD}

Add Exception
    [Arguments]  ${type}  ${data}  ${note}=''
    Click Add Exception
    Select From List By Value  css=${VASO_EXCEPTION_ADD_TYPE}  ${type}
    Input Text  css=${VASO_EXCEPTION_ADD_DATA}  ${data}
    run keyword if  '${note}' != ''  Input Text  css=${VASO_EXCEPTION_ADD_NOTE}  ${note}
    Click Element  css=${VASO_EXCEPTION_ADD_CONFIRM}

Delete Exception
    [Arguments]  ${index}
    Select Object  ${index}

Click Configure Scan Action
    Click Element  css=${VASO_CONFIGURE_ACTION}
    Wait Until Page Contains Element  css=${CONFIG_SCANACTION_TABLE}

VASO Page Should Have Elements
    [Arguments]  @{elements}
    :For  ${element}  IN  @{elements}
    \  Page Should Contain Element  css=${element}

Check Selects Under All Risk Level Should Have Elements
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_ALL_FILES_DROPDOWN}
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_ALL_IPS_DROPDOWN}
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_ALL_URLS_DROPDOWN}
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_ALL_DOMAINS_DROPDOWN}
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_ALL_APPLTO_DROPDOWN}

Check Selects Under Detail Risk Level Should Have Elements
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_HIGH_RISK_ACTION_DROPDOWN}
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_HIGH_RISK_APPLYTO_DROPDOWN}
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_MEDIUM_RISK_ACTION_DROPDOWN}
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_MEDIUM_RISK_APPLYTO_DROPDOWN}
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_LOW_RISK_ACTION_DROPDOWN}
    Page Should Contain Element  css=${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_LOW_RISK_APPLYTO_DROPDOWN}

