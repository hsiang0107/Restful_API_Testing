*** Settings ***
Resource  one_time_reports_variable.robot

*** Keywords ***
Click Add One Time Reports
    Click Element  css=${ONE_TIME_REPORTS_ADD}

Click Static Templates
    Click Element  css=${ONE_TIME_REPORTS_STATIC_TEMPLATES}
