*** Settings ***
Resource  ../../resources/CM.robot
Resource  ../../resources/automation_api.robot
Library  ../../resources/backend_objects/external_api.py
Variables  ../../resources/backend_objects/external_api_variables.py

Suite Setup  External Api Suite Setup
Test Setup
#Suite Teardown  External Api Suite Tear Down

*** Variables ***
${upload_stix_description_pattern}  Upload\\sSTIX.*
${delete_stix_description_pattern}  Delete\\sSTIX.*
${upload_stix_incorrect_parameter_pattern}  Upload\\sSTIX.*Incorrect\\sParameter
${delete_stix_incorrect_parameter_pattern}  Delete\\sSTIX.*Incorrect\\sParameter

*** Test Cases ***

(C5816940)Upload a valid STIX file
    [Tags]  RAT
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  stix  1
    Audit Should Be  12001  1  ${upload_stix_description_pattern}
    Uploaded Data Should Be  ${response}  stix

(C5816941)Upload two valid STIX file
    [Tags]  FAST
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  stix  2
    Audit Should Be  12001  1  ${upload_stix_description_pattern}
    Uploaded Data Should Be  ${response}  stix

(C5816942)Upload one valid, one invalid STIX file
    [Tags]  FAST
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  206
    Table Count Should Be  stix  1
    Audit Should Be  12004  1  ${upload_stix_description_pattern}
    Uploaded Data Should Be  ${response}  stix

(C5816950)Upload with unexpected STIX request payload
    [Tags]  FET
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  stix  0
    Audit Should Be  12001  1  ${upload_stix_incorrect_parameter_pattern}  0

    Truncate Tables
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  stix  0
    Audit Should Be  12001  1  ${upload_stix_incorrect_parameter_pattern}  0

(C5816943)Upload with unexpected STIX request content
    [Tags]  FET
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  stix  0
    Audit Should Be  12001  1  ${upload_stix_incorrect_parameter_pattern}  0

    Truncate Tables
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  stix  0
    Audit Should Be  12001  1  ${upload_stix_incorrect_parameter_pattern}  0

(C5816951)Download a valid STIX file
    [Tags]  RAT
    Truncate Tables
    Create Stix Data  C5816951  C5816951C5816951C5816951C5816951C5816951
    ${api}=  Set Variable  &{API_INFO}[download_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5816952)Download a non-existing STIX file
    [Tags]  FAST
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[download_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5816954)Download with unexpected STIX FileHashID
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[download_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request3.json
    Return Code Should Be  ${response}  400

(C5816953)Download with unexpected STIX request content
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[download_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5816955)Delete a valid STIX file
    [Tags]  RAT
    Truncate Tables
    Create Stix Data  C5816955  C5816955C5816955C5816955C5816955C5816955
    ${api}=  Set Variable  &{API_INFO}[delete_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  stix  0
    Audit Should Be  12003  1  ${delete_stix_description_pattern}

(C5816956)Delete two valid STIX files
    [Tags]  FAST
    Truncate Tables
    Create Stix Data  C5816956  C5816956C5816956C5816956C5816956C5816956
    Create Stix Data  C5816957  C5816956C5816956C5816956C5816956C5816957
    ${api}=  Set Variable  &{API_INFO}[delete_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  stix  0
    Audit Should Be  12003  1  ${delete_stix_description_pattern}

(C5816957)Delete one valid, one invalid files
    [Tags]  FAST
    Truncate Tables
    Create Stix Data  C5816957  C5816957C5816957C5816957C5816957C5816957
    Create Stix Data  C5816958  C5816957C5816957C5816957C5816957C5816958
    ${api}=  Set Variable  &{API_INFO}[delete_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  stix  1
    Audit Should Be  12003  1  ${delete_stix_description_pattern}

(C5816959)Delete a STIX file with unexpected FileHashID
    [Tags]  FET
    Truncate Tables
    Create Stix Data  C5816955  C5816955C5816955C5816955C5816955C5816955
    ${api}=  Set Variable  &{API_INFO}[delete_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  stix  1
    Audit Should Be  12003  1  ${delete_stix_incorrect_parameter_pattern}  0

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  stix  1
    Audit Should Be  12003  2  ${delete_stix_incorrect_parameter_pattern}  0

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request3.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  stix  1
    Audit Should Be  12003  3  ${delete_stix_incorrect_parameter_pattern}  0

(C5816958)Delete a STIX file with unexpected request content
    [Tags]  FET
    Truncate Tables
    Create Stix Data  C5816955  C5816955C5816955C5816955C5816955C5816955
    ${api}=  Set Variable  &{API_INFO}[delete_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  stix  1
    Audit Should Be  12003  1  ${delete_stix_incorrect_parameter_pattern}  0

(C5816962)Query a valid of extracting information of STIX file
    [Tags]  RAT
    Truncate Tables
    ${file_hash_id}=  Set Variable  C5816962C5816962C5816962C5816962C5816962
    Create Ioc Udsomap Data  ${file_hash_id}  C5816962  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  2
    ${api}=  Set Variable  &{API_INFO}[query_stix_extracted_info]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5816963)Query two valid of extracting information of STIX files
    [Tags]  FAST
    Truncate Tables
    ${file_hash_id1}=  Set Variable  C5816963C5816963C5816963C5816963C5816963
    ${file_hash_id2}=  Set Variable  C5816963C5816963C5816963C5816963C5816964
    Create Ioc Udsomap Data  ${file_hash_id1}  C5816963  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  2
    Create Ioc Udsomap Data  ${file_hash_id2}  C5816964  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA1  2
    ${api}=  Set Variable  &{API_INFO}[query_stix_extracted_info]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5816964)Query one valid, one invalid of extracting information of STIX files
    [Tags]  FAST
    Truncate Tables
    ${file_hash_id1}=  Set Variable  C5816964C5816964C5816964C5816964C5816964
    ${file_hash_id2}=  Set Variable  C5816964C5816964C5816964C5816964C5816965
    Create Ioc Udsomap Data  ${file_hash_id1}  C5816964  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  2
    Create Ioc Udsomap Data  ${file_hash_id2}  C5816965  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA1  2
    ${api}=  Set Variable  &{API_INFO}[query_stix_extracted_info]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5816965)Query extracting information of STIX file with unexpected request content
    [Tags]  FET
    Truncate Tables
    ${file_hash_id}=  Set Variable  C5816962C5816962C5816962C5816962C5816962
    Create Ioc Udsomap Data  ${file_hash_id}  C5816962  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  2
    ${api}=  Set Variable  &{API_INFO}[query_stix_extracted_info]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5816961)Extract STIX file with unexpected request payload
    [Tags]  FET
    Truncate Tables
    ${file_hash_id}=  Set Variable  C5816962C5816962C5816962C5816962C5816962
    Create Ioc Udsomap Data  ${file_hash_id}  C5816962  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  2
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request3.json
    Return Code Should Be  ${response}  400

(C5816960)Extract STIX file with unexpected request content
    [Tags]  FET
    Truncate Tables
    ${file_hash_id}=  Set Variable  C5816962C5816962C5816962C5816962C5816962
    Create Ioc Udsomap Data  ${file_hash_id}  C5816962  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  2
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400

(C5754368)Query all STIX in list
    [Tags]  FAST
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754369)Map STIX data by one FileHashIDs
    [Tags]  RAT
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754370)Map STIX data by multiple FileHashIDs
    [Tags]  RAT
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754371)Map STIX data by FuzzyMatchString
    [Tags]  RAT
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754372)FuzzyMatchString should be ignored if STIX FileHashIDs is set
    [Tags]  FAST
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754373)No matched STIX is found by FileHashIDs
    [Tags]  FAST
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754374)No matched STIX is found by FuzzyMatchString
    [Tags]  FAST
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754376)Limit STIX data by parameter PageSize
    [Tags]  RAT
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754377)Limit STIX data by parameter PageNumber
    [Tags]  RAT
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754380)Sort STIX data by FileName
    [Tags]  RAT
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response2.json

(C5754381)Sort STIX data by Title
    [Tags]  FAST
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response2.json

(C5754382)Sort STIX data by FileAddedDatetime
    [Tags]  FAST
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response2.json

(C5754383)Sort STIX data by UploadedFrom
    [Tags]  FAST
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response2.json

(C5754384)Sort STIX data by UploadedBy
    [Tags]  FAST
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response2.json

(C5754385)Sort STIX data by ExtractingStatus
    [Tags]  FAST
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  stix  response2.json

(C5754388)STIX query result limited by parameter PageSize
    [Tags]  TOFT1
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754389)STIX FuzzyMatchString query result limited by parameter PageNumber
    [Tags]  TOFT1
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754375)Incorrect STIX format of FileHashIDs value
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5754378)Unexpected STIX data in parameter PageSize
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5754379)Unexpected STIX data in parameter PageNumber
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5754386)Unexpected number in STIX SortingColumn parameter
    [Tags]  FET
    STIX Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Verify Query Result  ${TEST_NAME}  ${response}  stix

(C5754387)Unexpected STIX data in parameter SortingDirection
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta