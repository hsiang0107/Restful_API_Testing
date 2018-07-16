*** Settings ***
Resource  ../../resources/CM.robot
Resource  ../../resources/automation_api.robot
Library  ../../resources/backend_objects/external_api.py
Variables  ../../resources/backend_objects/external_api_variables.py

Suite Setup  External Api Suite Setup
Test Setup
#Suite Teardown  External Api Suite Tear Down

*** Variables ***
${upload_ioc_description_pattern}  Upload\\sOpenIOC.*
${delete_ioc_description_pattern}  Delete\\sOpenIOC.*
${upload_ioc_incorrect_parameter_pattern}  Upload\\sOpenIOC.*Incorrect\\sParameter
${delete_ioc_incorrect_parameter_pattern}  Delete\\sOpenIOC.*Incorrect\\sParameter

*** Test Cases ***

(C5816929)Upload a valid OpenIoC file
    [Tags]  RAT
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  ioc  1
    Audit Should Be  12001  1  ${upload_ioc_description_pattern}
    Uploaded Data Should Be  ${response}  ioc

(C5816930)Upload two valid OpenIoC file
    [Tags]  FAST
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  ioc  2
    Audit Should Be  12001  1  ${upload_ioc_description_pattern}
    Uploaded Data Should Be  ${response}  ioc

(C5816931)Upload one valid, one invalid OpenIoC file
    [Tags]  FAST
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  206
    Table Count Should Be  ioc  1
    Audit Should Be  12004  1  ${upload_ioc_description_pattern}
    Uploaded Data Should Be  ${response}  ioc

(C5816939)Upload with unexpected IOC request payload
    [Tags]  FET
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  ioc  0
    Audit Should Be  12001  1  ${upload_ioc_incorrect_parameter_pattern}  0

    Truncate Tables
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  ioc  0
    Audit Should Be  12001  1  ${upload_ioc_incorrect_parameter_pattern}  0

(C5816932)Upload with unexpected IOC request content
    [Tags]  FET
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  ioc  0
    Audit Should Be  12001  1  ${upload_ioc_incorrect_parameter_pattern}  0

    Truncate Tables
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  ioc  0
    Audit Should Be  12001  1  ${upload_ioc_incorrect_parameter_pattern}  0

(C5721592)Download a valid OpenIoC file
    [Tags]  RAT
    Truncate Tables
    Create Openioc Data  C5721592  C5721592C5721592C5721592C5721592C5721592
    ${api}=  Set Variable  &{API_INFO}[download_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5721600)Download a non-existing OpenIoC file
    [Tags]  FAST
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[download_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5743943)Download with unexpected IOC FileHashID
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[download_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request3.json
    Return Code Should Be  ${response}  400

(C5721619)Download with unexpected IOC request content
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[download_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5721622)Delete a valid OpenIoC file
    [Tags]  RAT
    Truncate Tables
    Create Openioc Data  C5721622  C5721622C5721622C5721622C5721622C5721622
    ${api}=  Set Variable  &{API_INFO}[delete_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  ioc  0
    Audit Should Be  12003  1  ${delete_ioc_description_pattern}

(C5721625)Delete two valid OpenIoC files
    [Tags]  FAST
    Truncate Tables
    Create Openioc Data  C5721625  C5721625C5721625C5721625C5721625C5721625
    Create Openioc Data  C5721626  C5721625C5721625C5721625C5721625C5721626
    ${api}=  Set Variable  &{API_INFO}[delete_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  ioc  0
    Audit Should Be  12003  1  ${delete_ioc_description_pattern}

(C5721626)Delete one valid, one invalid files
    [Tags]  FAST
    Truncate Tables
    Create Openioc Data  C5721626  C5721626C5721626C5721626C5721626C5721626
    Create Openioc Data  C5721627  C5721625C5721625C5721625C5721625C5721627
    ${api}=  Set Variable  &{API_INFO}[delete_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  ioc  1
    Audit Should Be  12003  1  ${delete_ioc_description_pattern}

(C5744019)Delete IOC with unexpected FileHashID
    [Tags]  FET
    Truncate Tables
    Create Openioc Data  C5721622  C5721622C5721622C5721622C5721622C5721622
    ${api}=  Set Variable  &{API_INFO}[delete_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  ioc  1
    Audit Should Be  12003  1  ${delete_ioc_incorrect_parameter_pattern}  0

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  ioc  1
    Audit Should Be  12003  2  ${delete_ioc_incorrect_parameter_pattern}  0

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request3.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  ioc  1
    Audit Should Be  12003  3  ${delete_ioc_incorrect_parameter_pattern}  0

(C5721627)Delete IOC with unexpected request content
    [Tags]  FET
    Truncate Tables
    Create Openioc Data  C5721622  C5721622C5721622C5721622C5721622C5721622
    ${api}=  Set Variable  &{API_INFO}[delete_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  ioc  1
    Audit Should Be  12003  1  ${delete_ioc_incorrect_parameter_pattern}  0

(C5734251)Query a valid of extracting information of OpenIOC file
    [Tags]  RAT
    Truncate Tables
    ${file_hash_id}=  Set Variable  C5734251C5734251C5734251C5734251C5734251
    Create Openioc Data  C5734251  ${file_hash_id}
    Create Ioc Udsomap Data  ${file_hash_id}  0xC5734251  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  1
    ${api}=  Set Variable  &{API_INFO}[query_openioc_extracted_info]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5743896)Query two valid of extracting information of OpenIOC files
    [Tags]  FAST
    Truncate Tables
    ${file_hash_id1}=  Set Variable  C5743896C5743896C5743896C5743896C5743896
    ${file_hash_id2}=  Set Variable  C5743896C5743896C5743896C5743896C5743897
    Create Openioc Data  C5743896  ${file_hash_id1}
    Create Openioc Data  C5743897  ${file_hash_id2}
    Create Ioc Udsomap Data  ${file_hash_id1}  0xC5743896  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  1
    Create Ioc Udsomap Data  ${file_hash_id2}  0xC5743897  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA1  1
    ${api}=  Set Variable  &{API_INFO}[query_openioc_extracted_info]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5743897)Query one valid, one invalid of extracting information of OpenIOC files
    [Tags]  FAST
    Truncate Tables
    ${file_hash_id1}=  Set Variable  C5743897C5743897C5743897C5743897C5743897
    ${file_hash_id2}=  Set Variable  C5743897C5743897C5743897C5743897C5743898
    Create Openioc Data  C5743897  ${file_hash_id1}
    Create Openioc Data  C5743898  ${file_hash_id2}
    Create Ioc Udsomap Data  ${file_hash_id1}  0xC5743897  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  1
    Create Ioc Udsomap Data  ${file_hash_id2}  0xC5743898  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA1  1
    ${api}=  Set Variable  &{API_INFO}[query_openioc_extracted_info]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5743898)Query extracting information of OpenIOC file with unexpected request content
    [Tags]  FET
    Truncate Tables
    ${file_hash_id}=  Set Variable  C5734251C5734251C5734251C5734251C5734251
    Create Openioc Data  C5734251  ${file_hash_id}
    Create Ioc Udsomap Data  ${file_hash_id}  0xC5734251  11111111-AAAA-BBBB-CCCC-DDDDDDDDAAA0  1
    ${api}=  Set Variable  &{API_INFO}[query_openioc_extracted_info]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5816436)Extract Open IoC to UDSO with unexpected request payload
    [Tags]  FET
    Truncate Tables
    ${file_hash_id}=  Set Variable  C5734251C5734251C5734251C5734251C5734251
    Create Openioc Data  C5734251  ${file_hash_id}
    ${api}=  Set Variable  &{API_INFO}[extract_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request3.json
    Return Code Should Be  ${response}  400

(C5816435)Extract Open IoC to UDSO with unexpected request content
    [Tags]  FET
    Truncate Tables
    ${file_hash_id}=  Set Variable  C5734251C5734251C5734251C5734251C5734251
    Create Openioc Data  C5734251  ${file_hash_id}
    ${api}=  Set Variable  &{API_INFO}[extract_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400

(C5734143)Map OPenIOC data by FileHashIDs
    [Tags]  RAT
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5721998)Query all IOC in list
    [Tags]  FAST
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5734144)Map IOC data by multiple FileHashIDs
    [Tags]  FAST
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5734145)Map OPenIOC data by FuzzyMatchString
    [Tags]  RAT
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response2.json

(C5734146)FuzzyMatchString should be ignored if IOC FileHashIDs is set
    [Tags]  FAST
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5734153)No matched IOC is found by FileHashIDs
    [Tags]  FAST
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5734155)No matched IOC is found by FuzzyMatchString
    [Tags]  FAST
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5734168)Limit IOC data by parameter PageSize
    [Tags]  RAT
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5734186)Limit IOC data by parameter PageNumber
    [Tags]  RAT
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5734204)Sort IOC data by FileName
    [Tags]  RAT
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response2.json

(C5734208)Sort IOC data by ShortDescription
    [Tags]  FAST
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response2.json

(C5734211)Sort IOC data by FileAddedDatetime
    [Tags]  FAST
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response2.json

(C5734213)Sort IOC data by UploadedFrom
    [Tags]  FAST
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response2.json

(C5734222)Sort IOC data by UploadedBy
    [Tags]  FAST
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response2.json

(C5734226)Sort IOC data by ExtractingStatus
    [Tags]  FAST
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  ioc  response2.json

(C5734193)IOC query result limited by parameter PageSize
    [Tags]  TOFT1
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5734195)IOC FuzzyMatchString query result limited by parameter PageNumber
    [Tags]  TOFT1
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5754050)Incorrect IOC format of FileHashIDs value
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5752138)Unexpected IOC data in parameter PageSize
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5752139)Unexpected IOC data in parameter PageNumber
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5752140)Unexpected number in IOC SortingColumn parameter
    [Tags]  FET
    IOC Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Verify Query Result  ${TEST_NAME}  ${response}  ioc

(C5752141)Unexpected IOC data in parameter SortingDirection
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta