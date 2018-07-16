*** Settings ***
Resource  CM_variable.robot
Library  ../lib/ExtendSeleniumLibrary.py
Library  ../lib/ConfigHelper.py
Library  ../lib/xml_helper.py
Library  ../lib/process_helper.py

*** Keywords ***
Begin Testing
    ${address} =  Get Data From Config  CM  address
    ${browser} =  Get Data From Config  CM  browser
    Set Selenium Speed   0.3
    Remove Hiding Pages From System Configuration
    Kill Log Processor
    Open Browser  ${address}  ${browser}
    Maximize Browser Window
    Wait Until Page Contains Element  xpath=${LOGIN_ACCOUNT_INPUT}  10
    Log In With Account  admin

End Testing
    Close Browser

Close Whats New Window
    Reset Frame
    ${whats_new_body_exist}=  Run Keyword And Return Status  Page Should Contain Element  css=${WHATS_NEW_CLOSE_BUTTON}
    Run Keyword IF  ${whats_new_body_exist} == True  Click Element  css=${WHATS_NEW_CLOSE_BUTTON}

Reset Frame
    Unselect Frame
    Wait Until Page Contains Element  name=dow  10
    Select Frame  name=dow

Switch To Frame TMCM
    Wait Until Page Contains Element  id=${FRAME_TMCM}
    Select Frame  id=${FRAME_TMCM}

Log Off
    Reset Frame
    Click Element  css=${ACCOUNT_MENU_BUTTON}
    Click Link  css=${ACCOUNT_MENU_LOG_OFF_BUTTON}

Log In With Account
    [Arguments]  ${account}
    ${username} =  Get Data From Config  CM  ${account}  account
    ${password} =  Get Data From Config  CM  ${account}  password
    Wait Until Page Contains Element  xpath=${LOGIN_ACCOUNT_INPUT}  10
    Input Text  xpath=${LOGIN_ACCOUNT_INPUT}  ${username}
    Input Password  id=${LOGIN_PASSWORD_INPUT}  ${password}
    Click Link  id=${LOGIN_BUTTON}
    Close Whats New Window

Go To Dashboard
    Reset Frame
    Click Link  css=${MENU_DASHBOARD_NAVIGATION}
    Switch To Frame TMCM
    Wait Until Page Contains Element    id=compliance

Go To Inventory View
    Reset Frame
    Mouse Over  xpath=${MENU_DIRECTORIES_NAVIGATION}
    Click Link  xpath=${MENU_USER_ENDPOINTS_NAVIGATION}
    Switch To Frame TMCM
    Wait Until Page Contains Element    css=div.block.block2 > a

Go To Product Directory
    Reset Frame
    Mouse Over  xpath=${MENU_DIRECTORIES_NAVIGATION}
    Click Link  xpath=${MENU_PRODUCTS_NAVIGATION}
    Switch To Frame TMCM

Go To Policy Management
    Reset Frame
    Mouse Over  xpath=${MENU_POLICIES_NAVIGATION}
    Click Link  xpath=${MENU_POLICY_MANAGEMENT_NAVIGATION}
    Switch To Frame TMCM

Go To Policy Template Settings
    Reset Frame
    Mouse Over  xpath=${MENU_POLICIES_NAVIGATION}
    Mouse Over  xpath=${MENU_POLICY_RESOURCES_NAVIGATION}
    Click Link  xpath=${MENU_POLICY_TEMPLATE_SETTINGS_NAVIGATION}
    Switch To Frame TMCM

Go To DLP Data Identifiers
    Reset Frame
    Mouse Over  xpath=${MENU_POLICIES_NAVIGATION}
    Mouse Over  xpath=${MENU_POLICY_RESOURCES_NAVIGATION}
    Click Link  xpath=${MENU_DLP_DATA_IDENTIFIERS_NAVIGATION}
    Switch To Frame TMCM

Go To DLP Templates
    Reset Frame
    Mouse Over  xpath=${MENU_POLICIES_NAVIGATION}
    Mouse Over  xpath=${MENU_POLICY_RESOURCES_NAVIGATION}
    Click Link  xpath=${MENU_DLP_TEMPLATES_NAVIGATION}
    Switch To Frame TMCM

Go To Log Query
    Reset Frame
    Mouse Over  xpath=${MENU_LOGS_NAVIGATION}
    Click Link  xpath=${MENU_LOG_QUERY_NAVIGATION}
    Switch To Frame TMCM

Go To Log Aggregation Settings
    Reset Frame
    Mouse Over  xpath=${MENU_LOGS_NAVIGATION}
    Click Link  xpath=${MENU_LOG_AGGREGATION_SETTINGS_NAVIGATION}
    Switch To Frame TMCM

Go To Log Maintenance
    Reset Frame
    Mouse Over  xpath=${MENU_LOGS_NAVIGATION}
    Click Link  xpath=${MENU_LOG_MAINTENANCE_NAVIGATION}
    Switch To Frame TMCM

Go To Event Notification
    Reset Frame
    Mouse Over  xpath=${MENU_NOTIFICATIONS_NAVIGATION}
    Click Link  xpath=${MENU_EVENT_NOTIFICATIONS_NAVIGATION}
    Switch To Frame TMCM

Go To Notification Method Setting
    Reset Frame
    Mouse Over  xpath=${MENU_NOTIFICATIONS_NAVIGATION}
    Click Link  xpath=${MENU_NOTIFICAITON_METHOD_SETTINGS_NAVIGATION}
    Switch To Frame TMCM

Go To Contact Groups
    Reset Frame
    Mouse Over  xpath=${MENU_NOTIFICATIONS_NAVIGATION}
    Click Link  xpath=${MENU_OCNTACT_GROUPS_NAVIGATION}
    Switch To Frame TMCM

Go To My Reports
    Reset Frame
    Mouse Over  xpath=${MENU_REPORTS_NAVIGATION}
    Click Link  xpath=${MENU_MY_REPORTS_NAVIGATION}
    Switch To Frame TMCM

Go To One Time Reports
    Reset Frame
    Mouse Over  xpath=${MENU_REPORTS_NAVIGATION}
    Click Link  xpath=${MENU_ONE_TIME_REPORTS_NAVIGATION}
    Switch To Frame TMCM

Go To Scheduled Reports
    Reset Frame
    Mouse Over  xpath=${MENU_REPORTS_NAVIGATION}
    Click Link  xpath=${MENU_SCHEDULED_REPORTS_NAVIGATION}
    Switch To Frame TMCM

Go To Custom Templates
    Reset Frame
    Mouse Over  xpath=${MENU_REPORTS_NAVIGATION}
    Click Link  xpath=${MENU_CUSTOM_TEMPLATES_NAVIGATION}
    Switch To Frame TMCM

Go To Report Maintenance
    Reset Frame
    Mouse Over  xpath=${MENU_REPORTS_NAVIGATION}
    Click Link  xpath=${MENU_REPORT_MAINTENANCE_NAVIGATION}
    Switch To Frame TMCM

Go To Scheduled Update
    Reset Frame
    Mouse Over  xpath=${MENU_UPDATES_NAVIGATION}
    Click Link  xpath=${MENU_SCHEDULED_UPDATE_NAVIGATION}
    Switch To Frame TMCM

Go To Manual Update
    Reset Frame
    Mouse Over  xpath=${MENU_UPDATES_NAVIGATION}
    Click Link  xpath=${MENU_MANUAL_UPDATE_NAVIGATION}
    Switch To Frame TMCM

Go To My Account
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Mouse Over  xpath=${MENU_ACCOUNT_MANAGEMENT_NAVIGATION}
    Click Link  xpath=${MENU_MY_ACCOUNT_NAVIGATION}
    Switch To Frame TMCM

Go To User Accounts
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Mouse Over  xpath=${MENU_ACCOUNT_MANAGEMENT_NAVIGATION}
    Click Link  xpath=${MENU_USER_ACCOUNTS_NAVIGATION}
    Switch To Frame TMCM

Go To User Roles
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Mouse Over  xpath=${MENU_ACCOUNT_MANAGEMENT_NAVIGATION}
    Click Link  xpath=${MENU_USER_ROLES_NAVIGATION}
    Switch To Frame TMCM

Go To Server Registration
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Mouse Over  xpath=${MENU_MANAGED_SERVERS_NAVIGATION}
    Click Link  xpath=${MENU_SERVER_REGISTRATION_NAVIGATION}
    Switch To Frame TMCM

Go To Agent Communication Schedule
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Mouse Over  xpath=${MENU_MANAGED_SERVERS_NAVIGATION}
    Click Link  xpath=${MENU_AGENT_COMMUNICATION_SCHEDULE_NAVIGATION}
    Switch To Frame TMCM

Go To Communication Timeout Settings
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Mouse Over  xpath=${MENU_MANAGED_SERVERS_NAVIGATION}
    Click Link  xpath=${MENU_COMMUNICATION_TIME_OUT_SETTINGS_NAVIGATION}
    Switch To Frame TMCM

Go To Security Agent Download
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Click Link  xpath=${MENU_SECURITY_AGENT_DOWNLOAD_NAVIGATION}
    Switch To Frame TMCM

Go To Command Tracking
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Click Link  xpath=${MENU_COMMAND_TRACKING_NAVIGATION}
    Switch To Frame TMCM

Go To License CM
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Mouse Over  xpath=${MENU_LICENSE_MANAGEMENT_NAVIGATION}
    Click Link  xpath=${MENU_CONTROL_MANAGER_NAVIGATION}
    Switch To Frame TMCM

Go To License Managed Products
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Mouse Over  xpath=${MENU_LICENSE_MANAGEMENT_NAVIGATION}
    Click Link  xpath=${MENU_MANAGED_PRODUCTS_NAVIGATION}
    Switch To Frame TMCM

Go To Proxy Settings
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Mouse Over  xpath=${MENU_SETTINGS_NAVIGATION}
    Click Link  xpath=${MENU_PROXY_SETTINGS_NAVIGATION}
    Switch To Frame TMCM

Go To Web Console Settings
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION_NAVIGATION}
    Mouse Over  xpath=${MENU_SETTINGS_NAVIGATION_NAVIGATION}
    Click Link  xpath=${MENU_WEB_CONSOLE_SETTINGS_NAVIGATION_NAVIGATION}
    Switch To Frame TMCM

Go To Smart Protection Network Settings
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION_NAVIGATION}
    Mouse Over  xpath=${MENU_SETTINGS_NAVIGATION_NAVIGATION}
    Click Link  xpath=${MENU_SMART_PROTECTION_NETWORK_SETTINGS_NAVIGATION_NAVIGATION}
    Switch To Frame TMCM

Go To Active Directory and Compliance Settings
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Mouse Over  xpath=${MENU_SETTINGS_NAVIGATION}
    Click Link  xpath=${MENU_AD_COMPLIANCE_SETTINGS_NAVIGATION}
    Switch To Frame TMCM

Go To Virtual Analyzer Suspicious Objects
    Reset Frame
    Mouse Over  xpath=${MENU_CONNECTED_THREAT_DEFENSE_NAVIGATION}
    Mouse Over  xpath=${MENU_THREAT_INTELLIGENCE_NAVIGATION}
    Click Link  xpath=${MENU_VASO_NAVIGATION}
    Switch To Frame TMCM

Go To Custom Intelligence
    Reset Frame
    Mouse Over  xpath=${MENU_CONNECTED_THREAT_DEFENSE_NAVIGATION}
    Mouse Over  xpath=${MENU_THREAT_INTELLIGENCE_NAVIGATION}
    Click Link  xpath=${MENU_CUSTOM_INTELLIGENCE_NAVIGATION}
    Switch To Frame TMCM

Go To Distribution Settings
    Reset Frame
    Mouse Over  xpath=${MENU_CONNECTED_THREAT_DEFENSE_NAVIGATION}
    Mouse Over  xpath=${MENU_THREAT_INTELLIGENCE_NAVIGATION}
    Click Link  xpath=${MENU_DISTRIBUTION_SETTINGS_NAVIGATION}
    Switch To Frame TMCM

Go To Indicators of Compromise
    Reset Frame
    Mouse Over  xpath=${MENU_ADMINISTRATION_NAVIGATION}
    Click Link  xpath=${MENU_IOC_NAVIGATION}
    Switch To Frame TMCM

Go To MDR Page
    Reset Frame
    Mouse Over  xpath=${MENU_CONNECTED_THREAT_DEFENSE_NAVIGATION}
    Click Link  xpath=${MENU_MDR_NAVIGATION}
    Switch To Frame TMCM

Go To Schedule Update Page
    Reset Frame
    Mouse Over  xpath=${MENU_UPDATES_NAVIGATION}
    Click Link  xpath=${MENU_SCHEDULED_UPDATE_NAVIGATION}
    Switch To Frame TMCM

Go To Manual Update Page
    Reset Frame
    Mouse Over  xpath=${MENU_UPDATES_NAVIGATION}
    Click Link  xpath=${MENU_MANUAL_UPDATE_NAVIGATION}
    Switch To Frame TMCM
