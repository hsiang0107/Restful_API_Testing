*** Settings ***
Resource  ../resources/pageobjects/event_notifications/event_notifications.robot
Resource  ../resources/pageobjects/notification_method_settings/notification_method_settings.robot
Resource  ../resources/pageobjects/contact_groups/contact_groups.robot
Resource  ../resources/pageobjects/command_tracking/command_tracking.robot
Resource  ../resources/pageobjects/log_query/log_query.robot
Resource  ../resources/pageobjects/one_time_reports/one_time_reports.robot
Resource  ../resources/pageobjects/mdr/MDR.robot
Resource  ../resources/pageobjects/ScheduleUpdate/ScheduleUpdate.robot
Resource  ../resources/pageobjects/ManualUpdate/ManualUpdate.robot
Resource  ../resources/pageobjects/CMLicense/CMLicense.robot
Resource  ../resources/pageobjects/virtual_analyzer_SO/VASO.robot
Resource  ../resources/pageobjects/custom_intelligence/custom_intelligence.robot
Resource  ../resources/pageobjects/SO_distribution/SO_distribution.robot
Resource  ../resources/pageobjects/one_console/one_console.robot
Resource  ../resources/pageobjects/dashboard/dashboard.robot
Resource  ../resources/pageobjects/AD_compliance/AD_compliance.robot
Resource  ../resources/pageobjects/policies/policy.robot
Resource  ../resources/pageobjects/user_accounts/user_accounts.robot
Resource  ../resources/pageobjects/user_roles/user_roles.robot
Resource  ../resources/pageobjects/inventory_view/inventory_view.robot
Resource  ../resources/CM.robot



Suite Setup  Begin Testing
Suite Teardown  End Testing

*** Variables ***
@{udso_scan_action}  Log  Block


*** Test Cases ***
AD Compliance BVT
    Go To Active Directory and Compliance Settings
    Check AD Setting Page Should Have Element
    Go To Compliance
    Check Compliance Page Should Have Elements
    Go To Sites
    Check Sites Page Should Have Elements

VASO BVT
    Go To Virtual Analyzer Suspicious Objects
    Click Configure Scan Action
    Check Selects Under All Risk Level Should Have Elements
    Click Element  css=${CONFIG_SCANACTION_CUSTOMIZE_CHECKBOX}
    Check Selects Under Detail Risk Level Should Have Elements

UDSO BVT
    Go To Custom Intelligence
    Switch To Frame UDSO
    Click Add UDSO
    Select UDSO Add Type  Domain
    List Should Have Values  css=${UDSO_ADD_EDIT_SCANACTION}  ${udso_scan_action}

STIX BVT
    Go To Custom Intelligence
    Click Element  css=${STIX_TAB}
    Element Text Should Be  css=${STIX_ADD_BUTTON}  Add
    Element Text Should Be  css=${STIX_DELETE_BUTTON}  Delete
    Click Element  css=${STIX_ADD_BUTTON}
    Element Text Should Be  css=${STIX_ADD_MODAL_ADD_BUTTON}  Add

OpenIOC BVT
    Go To Custom Intelligence
    Click Element  css=${OPENIOC_TAB}
    Element Text Should Be  css=${OPENIOC_ADD_BUTTON}  Add
    Element Text Should Be  css=${OPENIOC_DELETE_BUTTON}  Delete
    Element Text Should Be  css=${OPENIOC_INVESTIGATE_BUTTON}  Investigate
    Element Text Should Be  css=${OPENIOC_EXTRACT_BUTTON}  Extract

SO Distribution BVT
    Go To Distribution Settings
    Go To Tipping Point Tab
    Page Should Contain Element  id=${DIRTRIBUTION_TP_SYNCNOW_BUTTON}
    Go To Hub CM Tab
    Page Should Contain Element  id=${DIRTRIBUTION_HUB_CM_REGISTER_BUTTON}
    Go To Managed Server Tab
    Page Should Contain Element  id=${DIRTRIBUTION_MANAGED_PRODUCTS_SYNCNOW_BUTTON}

One Console BVT
    Go To Security Agent Download
    Element Text Should Be  css=${ONE_CONSOLE_PAGE_TITLE}  Security Agent Download
    Page Should Contain Element  css=${ONE_CONSOLE_WIN64_RADIO}
    Page Should Contain Element  css=${ONE_CONSOLE_WIN32_RADIO}
    Page Should Contain Element  css=${ONE_CONSOLE_MAC_RADIO}

MDR BVT
    Go To MDR Page
    Go To MDR Setting Tab
    MDR Page Title Should Be Correct
    Page Should Contain Element  css=${MDR_REGISTER_BUTTON}
    Go To MDR Pending Tab
    Page Should Contain Element  css=${MDR_APPROVE_BUTTON}
    Page Should Contain Element  css=${MDR_REJECT_BUTTON}

Policy Management BVT
    CM.Go To Policy Management
    Wait Until Page Contains Element  css=${HOW_TO_DIALOG_CLOSE_BUTTON}  timeout=20
    Wait Until Page Contains Element  css= ${PRODUCT_ID_DROPDOWN}  timeout=30
    Click Element  css=${HOW_TO_DIALOG_CLOSE_BUTTON}
    Select From List By Label  css=${PRODUCT_ID_DROPDOWN}  OfficeScan Agent
    Click Element  css=${POLICY_CREATE_BUTTON}
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

User Account BVT
    CM.Go To User Accounts
    Wait Until Page Contains Element  css=${ACCOUNT_ADD_BUTTON}
    Click Element  css=${ACCOUNT_ADD_BUTTON}
    Wait Until Page Contains Element  css=${ACCOUNT_ENABLE_CHECKBOX}
    Page Should Contain Element  css=${ACCOUNT_ENABLE_CHECKBOX}
    Page Should Contain Element  css=${ACCOUNT_SEARCH_CHECKBOX}
    Page Should Contain Element  css=${ACCOUNT_USER_LIST}
    Page Should Contain Element  css=${ACCOUNT_IMPORT_LIST}

User Role BVT
    CM.Go To User Roles
    Wait Until Page Contains Element  css=${ROLE_ADD_BUTTON}
    Click Element  css=${ROLE_ADD_BUTTON}
    Wait Until Page Contains Element  css=${ROLE_SAVE_BUTTON}
    Page Should Contain Element  css=${ROLE_SAVE_BUTTON}
    Page Should Contain Element  css=${ROLE_POLICY_FULL_RADIO}
    Page Should Contain Element  css=${ROLE_POLICY_READONLY_RADIO}

Update Schedule BVT
    Go To Schedule Update Page
    Page Should Contain Element  css=${SCHEDULE_SAVE_BUTTON}
    Element Text Should Be  css=${SCHEDULE_SAVE_BUTTON}  ${SCHEDULE_SAVE_BUTTON_TEXT}
    Page Should Contain Element  css=${SCHEDULE_COMPONENT}
    Element Text Should Be  css=${SCHEDULE_COMPONENT}  ${SCHEDULE_COMPONENT_TEXT}

Update Manual BVT
    Go To Manual Update Page
    Page Should Contain Element  css=${MANUAL_DOWNLOADNOW_BUTTON}
    Element Text Should Be  css=${MANUAL_DOWNLOADNOW_BUTTON}  ${MANUAL_DOWNLOADNOW_BUTTON_TEXT}
    Page Should Contain Element  css=${MANUAL_SAVE_BUTTON}
    Element Text Should Be  css=${MANUAL_SAVE_BUTTON}  ${MANUAL_SAVE_BUTTON_TEXT}
    Page Should Contain Element  css=${MANUAL_COMPONENT}
    Element Text Should Be  css=${MANUAL_COMPONENT}  ${MANUAL_COMPONENT_TEXT}

CM License BVT
    Go To License CM
    Page Should Contain Element  css=${CMLICENSE_INFOTABLE}
    Page Should Contain Element  css=${CMLICENSE_UPDATELICENSEINFO_BUTTON}
    Element Should Contain  css=${CMLICENSE_UPDATELICENSEINFO_BUTTON}  ${CMLICENSE_UPDATELICENSEINFO_BUTTON_TEXT}

ONE TIME REPORTS BVT
    Go To One Time Reports
    Click Add One Time Reports
    Click Static Templates
    Page Should Contain Element  css=${ONE_TIME_REPORTS_RAMSOMWARE_GROUPBY}
    Page Should Contain Element  css=${ONE_TIME_REPORTS_TOP_USERS_WITH_THREATS}
    Page Should Contain Element  css=${ONE_TIME_REPORTS_TOP_ENDPOINTS_WITH_THREATS}

Dashboard BVT
    Go To Dashboard
    Page Should Contain Element     id=${DASHBOARD_COMPLIANCE_BLOCK}
    Page Should Contain Element     id=${DASHBOARD_CRITICAL_THREAT_BLOCK}
    Page Should Contain Element     id=${DASHBOARD_DETECTION_BLOCK}
    Page Should Contain Element     css=${DASHBOARD_MAP_BLOCK}
    Page Should Contain Element     css=${DASHBOARD_DETAIL_BLOCK}
    Page Should Contain Element     css=${DASHBOARD_MOREINFO_BUTTON}
    Page Should Contain Element     css=${DASHBOARD_SETTING_BUTTON}

Inventory View BVT
    Go To Inventory View
    Sleep  5
    Click Advanced Link
    Page Should Contain Element     css=${INVENTORY_VIEW_CRITERIA_DROPDOWN}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_THREATTYPE_OPTION}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_SECURITYTHREAT_OPTION}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_IMPORTANCE_OPTION}
    Switch to Endpoints
    Page Should Contain Element     xpath=${INVENTORY_VIEW_THREATSTATUS_OPTION}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_ACTIVEDIRECTORYSITE_OPTION}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_REPORTINGLINE_OPTION}
    Select Compliance
    Page Should Contain Element     xpath=${INVENTORY_VIEW_ANTIVIRUSPATTERN_OPTION}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_DATALOSSPREVENTION_OPTION}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_FULLYCOMPLIANT_OPTION}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_NONCOMPLICANT_OPTION}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_UNREACHABLE_OPTION}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_TABULARVIEW_OPTION}
    Page Should Contain Element     xpath=${INVENTORY_VIEW_TIMELINEVIEW_OPTION}

LOG QUERY BVT
    Go To Log Query
    Element Text Should Be  css=${LOG_QUERY_SEARCH_BUTTON}  Search
    Page Should Contain Element  css=${LOG_QUERY_FILTER}  limit=3
    Page Should Contain Element  css=${LOG_QUERY_SAVED_SEARCH_BUTTON}  limit=2
    Expand Advance Search
    Page Should Contain Element  css=${LOG_QUERY_AND_RADIO}
    Page Should Contain Element  css=${LOG_QUERY_OR_RADIO}
    Element Should Be Selected  css=${LOG_QUERY_AND_RADIO}

COMMAND TRACKING BVT
    Go To Command Tracking
    Page Should Contain Element  css=${COMMAND_TRACKING_COMMNAD_COMBOBOX}

CONTACT GROUPS BVT
    Go To Contact Groups
    Page Should Contain Element  css=${CONTACT_GROUPS_ADD_BUTTON_ICON}

NOTIFICATION METHOD SETTINGS BVT
    Go To Notification Method Setting
    Page Should Contain Element  css=${NOTIFICATION_METHOD_SETTINGS_SMTP_ADDRESS_TEXTBOX}

EVENT NOTIFICATIONS BVT
    Go To Event Notification
    Page Should Contain Element  css=${EVENT_NOTIFICATIONS_CATEGORYS}  limit=7
    Page Should Contain Element  css=${EVENT_NOTIFICATIONS_SELECTED_CATEGORYS}  limit=1

