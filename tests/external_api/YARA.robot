*** Settings ***
Resource  ../../resources/CM.robot
Resource  ../../resources/automation_api.robot
Library  ../../resources/backend_objects/external_api.py
Variables  ../../resources/backend_objects/external_api_variables.py

Suite Setup  External Api Suite Setup
Test Setup
#Suite Teardown  External Api Suite Tear Down

*** Variables ***
${upload_yara_description_pattern}  Upload\\sYARA.*
${delete_yara_description_pattern}  Delete\\sYARA.*
${upload_yara_incorrect_parameter_pattern}  Upload\\sYARA.*Incorrect\\sParameter
${delete_yara_incorrect_parameter_pattern}  Delete\\sYARA.*Incorrect\\sParameter

*** Test Cases ***

(C5816966)Upload a valid YARA file
    [Tags]  RAT
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  yara  1
    Audit Should Be  12001  1  ${upload_yara_description_pattern}
    Uploaded Data Should Be  ${response}  yara

(C5816967)Upload two valid YARA file
    [Tags]  FAST
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  yara  2
    Audit Should Be  12001  1  ${upload_yara_description_pattern}
    Uploaded Data Should Be  ${response}  yara

(C5816968)Upload one valid, one invalid YARA file
    [Tags]  FAST
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  206
    Table Count Should Be  yara  1
    Audit Should Be  12004  1  ${upload_yara_description_pattern}
    Uploaded Data Should Be  ${response}  yara

(C5816976)Upload with unexpected YARA request payload
    [Tags]  FET
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  yara  0
    Audit Should Be  12001  1  ${upload_yara_incorrect_parameter_pattern}  0

    Truncate Tables
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  yara  0
    Audit Should Be  12001  1  ${upload_yara_incorrect_parameter_pattern}  0

(C5816969)Upload with unexpected YARA request content
    [Tags]  FET
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  yara  0
    Audit Should Be  12001  1  ${upload_yara_incorrect_parameter_pattern}  0

    Truncate Tables
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  yara  0
    Audit Should Be  12001  1  ${upload_yara_incorrect_parameter_pattern}  0

(C5816977)Download a valid YARA file
    [Tags]  RAT
    Truncate Tables
    Create Yara Data  C5816977  C5816977C5816977C5816977C5816977C5816977
    ${api}=  Set Variable  &{API_INFO}[download_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5816978)Download a non-existing YARA file
    [Tags]  FAST
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[download_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200

(C5816980)Download with unexpected YARA FileHashID
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[download_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request3.json
    Return Code Should Be  ${response}  400

(C5816979)Download with unexpected YARA request content
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[download_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5816981)Delete a valid YARA file
    [Tags]  RAT
    Truncate Tables
    Create Yara Data  C5816981  C5816981C5816981C5816981C5816981C5816981
    ${api}=  Set Variable  &{API_INFO}[delete_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  yara  0
    Audit Should Be  12003  1  ${delete_yara_description_pattern}

(C5816982)Delete two valid YARA files
    [Tags]  FAST
    Truncate Tables
    Create Yara Data  C5816982  C5816982C5816982C5816982C5816982C5816982
    Create Yara Data  C5816983  C5816982C5816982C5816982C5816982C5816983
    ${api}=  Set Variable  &{API_INFO}[delete_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  yara  0
    Audit Should Be  12003  1  ${delete_yara_description_pattern}

(C5816983)Delete one valid, one invalid files
    [Tags]  FAST
    Truncate Tables
    Create Yara Data  C5816983  C5816983C5816983C5816983C5816983C5816983
    Create Yara Data  C5816984  C5816983C5816983C5816983C5816983C5816984
    ${api}=  Set Variable  &{API_INFO}[delete_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Response  ${TEST_NAME}  ${response}  200
    Table Count Should Be  yara  1
    Audit Should Be  12003  1  ${delete_yara_description_pattern}

(C5816985)Delete YARA file with unexpected FileHashID
    [Tags]  FET
    Truncate Tables
    Create Yara Data  C5816981  C5816981C5816981C5816981C5816981C5816981
    ${api}=  Set Variable  &{API_INFO}[delete_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request1.json
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  yara  1
    Audit Should Be  12003  1  ${delete_yara_incorrect_parameter_pattern}  0

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  yara  1
    Audit Should Be  12003  2  ${delete_yara_incorrect_parameter_pattern}  0

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  request_data=request2.json
    Return Code Should Be  ${response}  400
    Table Count Should Be  yara  1
    Audit Should Be  12003  3  ${delete_yara_incorrect_parameter_pattern}  0

(C5816984)Delete YARA file with unexpected request content
    [Tags]  FET
    Truncate Tables
    Create Yara Data  C5816981  C5816981C5816981C5816981C5816981C5816981
    ${api}=  Set Variable  &{API_INFO}[delete_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta
    Table Count Should Be  yara  1
    Audit Should Be  12003  1  ${delete_yara_incorrect_parameter_pattern}  0

(C5754393)Map YARA data by one FileHashIDs
    [Tags]  RAT
    Truncate Tables
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754394)Map YARA data by multiple FileHashIDs
    [Tags]  RAT
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754395)Map YARA data by FuzzyMatchString
    [Tags]  RAT
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754396)FuzzyMatchString should be ignored if YARA FileHashIDs is set
    [Tags]  FAST
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754392)Query all YARA in list
    [Tags]  FAST
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754397)When no matched YARA is found by FileHashIDs
    [Tags]  FAST
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754398)When no matched YARA is found by FuzzyMatchString
    [Tags]  FAST
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754400)Limit YARA data by parameter PageSize
    [Tags]  RAT
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754401)Limit YARA data by parameter PageNumber
    [Tags]  RAT
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754404)Sort YARA data by FileName
    [Tags]  RAT
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  yara  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  yara  response2.json

(C5754406)Sort YARA data by FileAddedDatetime
    [Tags]  FAST
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  yara  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  yara  response2.json

(C5754407)Sort YARA data by UploadedFrom
    [Tags]  FAST
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  yara  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  yara  response2.json

(C5754408)Sort YARA data by UploadedBy
    [Tags]  FAST
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request1.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  yara  response1.json

    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  2  request2.json
    Return Code Should Be  ${response}  200
    Verify Response Data Without Datetime  ${TEST_NAME}  ${response}  yara  response2.json

(C5754412)YARA query result limited by parameter PageSize
    [Tags]  TOFT1
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754413)YARA FuzzyMatchString query result limited by parameter PageNumber
    [Tags]  TOFT1
    YARA Query Initialization
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754399)Incorrect YARA format of FileHashIDs value
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5754402)Unexpected YARA data in parameter PageSize
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5754403)Unexpected YARA data in parameter PageNumber
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5754410)Unexpected number in YARA SortingColumn parameter
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Verify Query Result  ${TEST_NAME}  ${response}  yara

(C5754411)Unexpected YARA data in parameter SortingDirection
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[query_yara]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  400
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta