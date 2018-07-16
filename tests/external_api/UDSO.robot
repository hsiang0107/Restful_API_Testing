*** Settings ***
Resource  ../../resources/CM.robot
Resource  ../../resources/automation_api.robot
Library  ../../resources/backend_objects/external_api.py
Variables  ../../resources/backend_objects/external_api_variables.py

Suite Setup  External Api Suite Setup
Test Setup
#Suite Teardown  External Api Suite Tear Down

*** Test Cases ***

(C5744145)Upload a valid SO file from external
    [Tags]  RAT
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_file_udso_from_external]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  blacklist  1
    Uploaded So Tables Should Be  ${TEST_NAME}

(C5744146)Upload a valid SO file with each of the file_scan_action
    [Tags]  FAST
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_file_udso_from_external]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Verify Response  ${TEST_NAME}  ${response}  200
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Verify Response  ${TEST_NAME}  ${response}  200
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request3.json
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  blacklist  3
    Uploaded So Tables Should Be  ${TEST_NAME}  request1.json
    Uploaded So Tables Should Be  ${TEST_NAME}  request2.json
    Uploaded So Tables Should Be  ${TEST_NAME}  request3.json

(C5744149)Upload a valid SO file from external with unexpected request content
    [Tags]  FET
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_file_udso_from_external]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Table Count Should Be  blacklist  0

(C5752026)Query a valid UDSO From OpenIoC/STIX Extraction link
    [Tags]  TOFT3
    Truncate Tables
    ${file_hash_id}=  Set Variable  C5752026C5752026C5752026C5752026C5752026
    Create Ioc Udsomap Data  ${file_hash_id}  C5752026  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0
    ${api}=  Set Variable  &{API_INFO}[query_udso_from_extration]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5752114)Query two valid UDSO From OpenIoC/STIX Extraction link
    [Tags]  TOFT3
    Truncate Tables
    ${file_hash_id1}=  Set Variable  C5752114C5752114C5752114C5752114C5752114
    ${file_hash_id2}=  Set Variable  C5752114C5752114C5752114C5752114C5752115
    Create Ioc Udsomap Data  ${file_hash_id1}  C5752114  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  1
    Create Ioc Udsomap Data  ${file_hash_id2}  C5752115  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA1  2
    ${api}=  Set Variable  &{API_INFO}[query_udso_from_extration]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5752115)Query one valid, one invalid UDSO From OpenIoC/STIX Extraction link
    [Tags]  TOFT3
    Truncate Tables
    ${file_hash_id1}=  Set Variable  C5752115C5752115C5752115C5752115C5752115
    ${file_hash_id2}=  Set Variable  C5752115C5752115C5752115C5752115C5752116
    Create Ioc Udsomap Data  ${file_hash_id1}  C5752115  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  1
    Create Ioc Udsomap Data  ${file_hash_id2}  C5752116  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA1  2
    ${api}=  Set Variable  &{API_INFO}[query_udso_from_extration]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
