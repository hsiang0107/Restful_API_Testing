*** Settings ***
Library  backend_objects/external_api.py

*** Keywords ***
IOC Query Initialization
    Truncate Tables
    Initialize Ioc Test Data

STIX Query Initialization
    Truncate Tables
    Initialize Stix Test Data

YARA Query Initialization
    Truncate Tables
    Initialize Yara Test Data

Verify Query Result
    [Arguments]  ${TEST_NAME}  ${response}  ${type}
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ${type}
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta  FeatureCtrl

Verify Response
    [Arguments]  ${TEST_NAME}  ${response}  ${expected_response_code}
    Return Code Should Be  ${response}  ${expected_response_code}
    Response Body Should Be  ${TEST_NAME}  ${response}