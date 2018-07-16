*** Settings ***
Resource  ../../resources/CM.robot
Resource  ../../resources/automation_api.robot
Library  ../../resources/pageobjects/log_query/log_query.py
Library  ../../resources/backend_objects/external_api.py
Library  ../../lib/http_helper.py
Variables  ../../resources/backend_objects/external_api_variables.py
Variables  ../../config/settings.yaml

Suite Setup  External Api Suite Setup
Test Setup
#Suite Teardown  External Api Suite Tear Down

*** Test Cases ***

(C5721603)External invoke API - InvokePermission Both
    [Tags]  RAT
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    ${membership}=  Set Variable  &{Membership}[API]
    Ioc Membership Validation  ${response}  ${membership}

(C5721580)Internal invoke API - InvokePermission Both
    [Tags]  RAT
    Truncate Tables
    ${api}=  Set Variable  &{API_INFO}[upload_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  1
    Return Code Should Be  ${response}  200
    ${membership}=  Set Variable  &{Membership}[Manual]
    Ioc Membership Validation  ${response}  ${membership}

(C5752128)Internal call with no InvokePermission set
    [Tags]  RAT
    ${api}=  Set Variable  &{API_INFO}[GetReportingLineMap]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  1
    Return Code Should Be  ${response}  200
    Verify Response By Key  ${TEST_NAME}  ${response}  Data  Meta  PermissionCtrl  FeatureCtrl

(C5752132)Internal call with InvokePermission to Internal Only
    [Tags]  FAST
    ${api}=  Set Variable  &{API_INFO}[getdetections]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  1
    Return Code Should Be  ${response}  200
    Verify Response By Key  ${TEST_NAME}  ${response}  Data  Meta

(C5721649)Legacy API - Query product server list
    [Tags]  TOFT
    Log Query Suite Setup
    ${api}=  Set Variable  &{API_INFO}[query_server]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Full Response Body Should Be  ${TEST_NAME}  ${response}

(C5752116)Legacy API - Query product agent list
    [Tags]  TOFT
    Log Query Suite Setup
    ${api}=  Set Variable  &{API_INFO}[query_agent]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Verify Response By Key  ${TEST_NAME}  ${response}  result_code  result_description  result_content

(C5752134)External call with InvokePermission set to Internal Only
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[getdetections]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  403

(C5752133)External call with no InvokePermission set
    [Tags]  FET
    ${api}=  Set Variable  &{API_INFO}[GetReportingLineMap]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  403

(C5754366)No permission if invoking internal API by read only account
    [Tags]  FET
    &{credential}=  Create Dictionary  user=${CM.read_only.account}  pwd=${CM.read_only.password}
    ${api}=  Set Variable  &{API_INFO}[upload_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  1  credential=${credential}
    Return Code Should Be  ${response}  403
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5752135)Invoke internal API without login
    [Tags]  FET
    &{credential}=  Create Dictionary  user=guest  pwd=1234
    ${api}=  Set Variable  &{API_INFO}[GetReportingLineMap]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  1  credential=${credential}
    Return Code Should Be  ${response}  401

(C5752118)Invoke external API without login
    [Tags]  FET
    &{credential}=  Create Dictionary  user=guest  pwd=1234
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}  1  credential=${credential}
    Return Code Should Be  ${response}  401
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5752119)Authentication fail - AuthenticationFailureTokenNotProvided
    [Tags]  FET
    ${host}=  Catenate  SEPARATOR=  ${CM.protocol}  ${CM.ip}
    ${server}=  Catenate  SEPARATOR=:  ${host}  ${CM.port}
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${params}=  Parse Test Data Json  ${TEST_NAME}  request.json
    ${response}=  Send Request  ${server}  ${api}  2  params=${params}
    Return Code Should Be  ${response}  401
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5752120)Authentication fail - AuthenticationFailureMalformedToken
    [Tags]  FET
    ${host}=  Catenate  SEPARATOR=  ${CM.protocol}  ${CM.ip}
    ${server}=  Catenate  SEPARATOR=:  ${host}  ${CM.port}
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${params}=  Parse Test Data Json  ${TEST_NAME}  request.json
    ${response}=  Send Request  ${server}  ${api}  2  params=${params}  jwt_token=aaaa.bbbb
    Return Code Should Be  ${response}  401
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5752122)Authentication fail - AuthenticationFailureInvalidTokenSignature
    [Tags]  FET
    ${host}=  Catenate  SEPARATOR=  ${CM.protocol}  ${CM.ip}
    ${server}=  Catenate  SEPARATOR=:  ${host}  ${CM.port}
    ${private_key}=  Set Variable  1D44452A-1390-483B-AFA8-000000000000
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${params}=  Parse Test Data Json  ${TEST_NAME}  request.json
    ${token}=  get_jwt  &{api}[method]  &{api}[path]  header=  request_body=  private_key=${private_key}
    ${response}=  Send Request  ${server}  ${api}  2  params=${params}  jwt_token=${token}
    Return Code Should Be  ${response}  401
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5752124)Authentication fail - AuthenticationFailureInvalidRequestCheckSum
    [Tags]  FET
    ${host}=  Catenate  SEPARATOR=  ${CM.protocol}  ${CM.ip}
    ${server}=  Catenate  SEPARATOR=:  ${host}  ${CM.port}
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${params}=  Parse Test Data Json  ${TEST_NAME}  request.json
    ${token}=  get_jwt  POST  &{api}[path]  header=  request_body=
    ${response}=  Send Request  ${server}  ${api}  2  params=${params}  jwt_token=${token}
    Return Code Should Be  ${response}  401
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta

(C5721633)Authentication fail - Invalid application ID
    [Tags]  FET
    ${host}=  Catenate  SEPARATOR=  ${CM.protocol}  ${CM.ip}
    ${server}=  Catenate  SEPARATOR=:  ${host}  ${CM.port}
    ${app_id}=  Set Variable  7ACE92AE-FFD3-4E07-AF35-000000000000
    ${api}=  Set Variable  &{API_INFO}[query_openioc]
    ${params}=  Parse Test Data Json  ${TEST_NAME}  request.json
    ${token}=  get_jwt  &{api}[method]  &{api}[path]  header=  request_body=  app_id=${app_id}
    ${response}=  Send Request  ${server}  ${api}  2  params=${params}  jwt_token=${token}
    Return Code Should Be  ${response}  401
    Verify Response By Key  ${TEST_NAME}  ${response}  Meta