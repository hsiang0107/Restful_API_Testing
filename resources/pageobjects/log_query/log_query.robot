*** Settings ***
Resource  log_query_variable.robot
Library  String
Library  OperatingSystem
Library  log_query.py
Library  ../../../lib/ExtendSeleniumLibrary.py

*** Keywords ***
Expand Advance Search
    Click Element  css=${LOG_QUERY_ADVANCED_FILTER_LINK}

Log Query Suite Setup With Register
    Log Query Suite Setup
    Begin Testing

Set Data View By Value
    [Arguments]  ${data_view_value}
    Click Element  css=${LOG_QUERY_DATA_VIEW_DROPDOWN}
    Select Radio Button  logDataView  ${data_view_value}
    Click Element  css=${LOG_QUERY_DATA_VIEW_DROPDOWN_OK_BUTTON}

Set Fix Time Range
    # time_range should be last24hours, today, last7days, last14days, last30days
    [Arguments]  ${time_range}
    ${time_range_selector}=  Replace String  ${LOG_QUERY_TIME_RANGE_DROPDOWN_ITEM}  %s  ${time_range}
    Click Element  css=${LOG_QUERY_TIME_RANGE_DROPDOWN}
    Click Element  css=${time_range_selector}

Check Product
    [Arguments]  @{product_path}
    Click Element  css=${LOG_QUERY_PRODUCT_DROPDOWN}
    Check Product In Log Query  ${product_path}
    Click Element  css=${LOG_QUERY_PRODUCT_DROPDOWN_OK_BUTTON}

Set Match Logic In Advanced Filter
    # logic should be and, or
    [Arguments]  ${logic}
    ${radios}=  Get WebElements  css=${LOG_QUERY_ADVANCED_FILTER_MATCH_RADIO}
    Run keyword If  '${logic}' == 'and'  Click Element  ${radios[0]}  ELSE  Click Element  ${radios[1]}

Add Criteria In Advanced Filter
    [Arguments]  @{args}
    Set Advanced Filter In Log Query  ${args}

Downloaded Result Should Same As Ui
    ${ui_table_result}=  Parse Log Query Table Result
    Verify Csv With Ui  ${ui_table_result}
