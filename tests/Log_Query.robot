*** Settings ***
Resource  ../resources/CM.robot
Resource  ../resources/pageobjects/log_query/log_query.robot
Library  ../resources/pageobjects/log_query/log_query.py

#Suite Setup  Log Query Suite Setup
Test Setup  Begin Testing
Test Teardown  End Testing
#Suite Teardown

*** Test Cases ***
(RAT-0001)Query Logs By DataView/Product/Time Range/Advanced Filter
    [Tags]  RAT
    Clear Log
    log_query.Send Log  ${TEST_NAME}  LogQuery_RAT_0001.csv
    Go To Log Query
    Check Product  Local Folder  New Entity  OSCE1
    Set Fix Time Range  last7days
    Expand Advance Search
    Set Match Logic In Advanced Filter  and
    Add Criteria In Advanced Filter  Endpoint  contains  A
    Click Element  css=${LOG_QUERY_SEARCH_BUTTON}
    Wait Until Page Contains Element  css=${LOG_QUERY_TABLE_CONTAINER}
    Element Text Should Be  css=${LOG_QUERY_LOG_TOTAL_COUNT_LABEL}  10
    Download Log Query Csv
    Downloaded Result Should Same As Expected  ${TEST_NAME}  expected.csv
    Remove Result Files

(RAT-1153)Virus/Malware - Drill Down to Endpoint Virus/Malware Information by [Host Details]
    [Tags]  RAT
    Clear Log
    log_query.Send Log  (FAST-0002)  LogQuery_FAST_0002.csv
    Go To Log Query
    Click Element  css=${LOG_QUERY_SEARCH_BUTTON}
    Wait Until Page Contains Element  css=${LOG_QUERY_TABLE_CONTAINER}
    Click Link  css=${LOG_QUERY_HOST_DETAILS_LINK}
    Wait Until Page Does Not Contain  css=${LOG_QUERY_BACK_BUTTON_HIDE}
    Download Log Query Csv
    Downloaded Result Should Same As Expected  ${TEST_NAME}  expected_Host Details.csv
    Click Element  css=${LOG_QUERY_CUSTOMIZE_COLUMNS_DROPDOWN}
    ${column_items}=  Get WebElements  css=${LOG_QUERY_CUSTOMIZE_COLUMNS_DROPDOWN_ITEM}
    Column Items Should Be  ${LOG_QUERY_VIRUS_HOST_DETAIL_COLUMN_ITEMS}  ${column_items}
    Click Element  css=${LOG_QUERY_SAVE_QUERY_BUTTON}
    Element Value Should Be  css=${LOG_QUERY_SAVE_QUERY_NAME_TEXTBOX}  Endpoint Virus/Malware Information_\\d\\d\\d\\d_\\d\\d_\\d\\d_\\d\\d
    Remove Result Files

(RAT-0129)Save the applied search (Default)
    [Tags]  RAT
    Clear Log
    log_query.Send Log  (FAST-0002)  LogQuery_FAST_0002.csv
    Go To Log Query
    Click Element  css=${LOG_QUERY_SEARCH_BUTTON}
    Wait Until Page Contains Element  css=${LOG_QUERY_TABLE_CONTAINER}
    Click Element  css=${LOG_QUERY_SAVE_QUERY_BUTTON}
    Element Value Should Be  css=${LOG_QUERY_SAVE_QUERY_NAME_TEXTBOX}  Virus/Malware detections_\\d\\d\\d\\d_\\d\\d_\\d\\d_\\d\\d
    ${saved_query_name}=  Get Element Attribute  css=${LOG_QUERY_SAVE_QUERY_NAME_TEXTBOX}  value
    Click Element  css=${LOG_QUERY_SAVE_QUERY_SAVE_BUTTON}
    Click Element  css=${LOG_QUERY_SAVED_QUERIES_BUTTON}
    Element Text Should Be  css=${LOG_QUERY_SAVED_QUERIES_ITEM_NAME_LABEL}  ${saved_query_name}
    Click Element  css=${LOG_QUERY_SAVED_QUERIES_BUTTON}
    Click Element  css=${LOG_QUERY_SAVED_QUERIES_ITEM_DELETE_BUTTON}

(RAT-0144)Share the save applied search + (RAT-0145)Unshare the shared save applied search
    [Tags]  RAT
    Clear Log
    log_query.Send Log  (FAST-0002)  LogQuery_FAST_0002.csv
    Go To Log Query
    Click Element  css=${LOG_QUERY_SEARCH_BUTTON}
    Wait Until Page Contains Element  css=${LOG_QUERY_TABLE_CONTAINER}
    Click Element  css=${LOG_QUERY_SAVE_QUERY_BUTTON}
    Click Element  css=${LOG_QUERY_SAVE_QUERY_SAVE_BUTTON}
    Click Element  css=${LOG_QUERY_SAVED_QUERIES_BUTTON}
    Page Should Contain Element  css=${LOG_QUERY_SAVED_QUERIES_ITEM_SHARE_BUTTON}
    Page Should Contain Element  css=${LOG_QUERY_SAVED_QUERIES_ITEM_DELETE_BUTTON}
    Click Element  css=${LOG_QUERY_SAVED_QUERIES_ITEM_SHARE_BUTTON}
    Click Element  css=${LOG_QUERY_SAVED_QUERIES_BUTTON}
    Page Should Contain Element  css=${LOG_QUERY_SAVED_QUERIES_ITEM_STOP_SHARING_BUTTON}
    Page Should Contain Element  css=${LOG_QUERY_SAVED_QUERIES_ITEM_DELETE_BUTTON}
    # (RAT-0145)Unshare the shared save applied search
    Click Element  css=${LOG_QUERY_SAVED_QUERIES_ITEM_STOP_SHARING_BUTTON}
    Click Element  css=${LOG_QUERY_SAVED_QUERIES_BUTTON}
    Page Should Contain Element  css=${LOG_QUERY_SAVED_QUERIES_ITEM_SHARE_BUTTON}
    Page Should Not Contain Element  css=${LOG_QUERY_SAVED_QUERIES_ITEM_STOP_SHARING_BUTTON}
    Log Off
    Log In With Account  read_only
    Go To Log Query
    Click Element  css=${LOG_QUERY_SAVED_QUERIES_BUTTON}
    Page Should Not Contain Element  css=${LOG_QUERY_SAVED_QUERIES_ITEM}

(RAT-1001)Export to CSV
    [Tags]  RAT
    Clear Log
    log_query.Send Log  (RAT-0001)  LogQuery_RAT_0001.csv
    Go To Log Query
    Click Element  css=${LOG_QUERY_SEARCH_BUTTON}
    Wait Until Page Contains Element  css=${LOG_QUERY_TABLE_CONTAINER}
    Click Element  css=${LOG_QUERY_SAVE_QUERY_BUTTON}
    Element Value Should Be  css=${LOG_QUERY_SAVE_QUERY_NAME_TEXTBOX}  Virus/Malware detections_\\d\\d\\d\\d_\\d\\d_\\d\\d_\\d\\d
    Download Log Query Csv
    Downloaded Result Should Same As Ui

(1027)Threat Detection Results - Virus/Malware
    [Tags]  RAT
    Clear Log
    log_query.Send Log  (RAT-0001)  LogQuery_RAT_0001.csv
    Go To Log Query
    Click Element  css=${LOG_QUERY_SEARCH_BUTTON}
    Wait Until Page Contains Element  css=${LOG_QUERY_TABLE_CONTAINER}
    Element Text Should Be  css=${LOG_QUERY_LOG_TOTAL_COUNT_LABEL}  20
    Element Text Should Be  css=${LOG_QUERY_CUSTOMIZE_COLUMNS_DROPDOWN}  Customize Columns
    Element Text Should Be  css=${LOG_QUERY_ADVANCED_FILTER_LINK}  Show advanced filters
    Element Text Should Be  css=${LOG_QUERY_CUSTOMIZE_COLUMNS_DROPDOWN}  Customize Columns

(RAT-0001)Query Machine Learning Detail Information View
    [Tags]  RAT
    Clear Log
    log_query.Send Log  (MLINT-RAT-0001)  MachineLearning.csv
    Go To Log Query
    Set Data View By Value  MachineLearningDetail
    Set Fix Time Range  last7days
    Click Element  css=${LOG_QUERY_SEARCH_BUTTON}
    Wait Until Page Contains Element  css=${LOG_QUERY_TABLE_CONTAINER}
    Element Text Should Be  css=${LOG_QUERY_LOG_TOTAL_COUNT_LABEL}  10
    Click Element  css=${LOG_QUERY_CUSTOMIZE_COLUMNS_DROPDOWN}
    ${column_items}=  Get WebElements  css=${LOG_QUERY_CUSTOMIZE_COLUMNS_DROPDOWN_ITEM}
    Column Items Should Be  ${LOG_QUERY_MACHINE_LEARNING_COLUMN_ITEMS}  ${column_items}
