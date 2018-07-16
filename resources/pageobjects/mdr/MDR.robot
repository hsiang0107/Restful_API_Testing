*** Settings ***
Resource  MDR_variable.robot

*** Keywords ***

Go To MDR Pending Tab
    Click Link  css=${MDR_PENDING_TAB}

Go To MDR History Tab
    Click Element  css=${MDR_HISTORY_TAB}

Go To MDR Setting Tab
    Click Link  css=${MDR_SETTING_TAB}

Register MDR Service
    ${address} =  Get Data From Config  MDR  address
    ${token} =  Get Data From Config  MDR  token
    Input Text  css=${MDR_SERVER_ADDRESS}  ${address}
    Input Text  css=${MDR_SERVICE_TOKEN}  ${token}
    Click Button  css=${MDR_REGISTER_BUTTON}

Unregister MDR Service
    Go To Setting
    Click Button  css=${MDR_UNREGISTER_BUTTON}
    Click Button  css=${MDR_CANCEL_UNREGISTER}
    Click Button  css=${MDR_UNREGISTER_BUTTON}
    Click Button  css=${MDR_CONFIRM_UNREGISTER}

MDR Page Title Should Be Correct
    Element Text Should Be  css=${MDR_PAGE_TITLE}  Managed Detection and Response

MDR Page Should Have Button
    [Arguments]  @{buttons}
    :For  ${button}  IN  @{buttons}
    \  Page Should Contain Element  css=${button}

