*** Settings ***
Resource  ../../resources/CM.robot
Resource  ../../resources/automation_api.robot
Library  ../../resources/backend_objects/external_api.py
Variables  ../../resources/backend_objects/external_api_variables.py

Suite Setup  External Api Suite Setup
Test Setup
#Suite Teardown  External Api Suite Tear Down

*** Test Cases ***

(C5721586) Indicator type - IP Watchlist
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721587) Indicator type - Domain Watchlist
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721588) Indicator type - URL Watchlist
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721589) Indicator type - File Watchlist
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721597) Cybox object property type - cyboxCommon:Simple_Hash_Value
    [Tags]  FAST
    Truncate Tables
    Create Specified Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9  base64_1
    Create Specified Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e8  base64_2
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721598) Cybox object property type - URIObject:Value
    [Tags]  FAST
    Truncate Tables
    Create Specified Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9  base64_1
    Create Specified Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e8  base64_2
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721599) Cybox object property type - DomainNameObj:Value
    [Tags]  FAST
    Truncate Tables
    Create Specified Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9  base64_1
    Create Specified Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e8  base64_2
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721601) Cybox object property type - HostnameObject:Hostname_Value
    [Tags]  FAST
    Truncate Tables
    Create Specified Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9  base64_1
    Create Specified Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e8  base64_2
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721602) Cybox object property type - AddressObject:Address_Value
    [Tags]  FAST
    Truncate Tables
    Create Specified Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9  base64_1
    Create Specified Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e8  base64_2
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721604) Single Observable with Single Property containing multiple values separated by comma
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721606) Single Observable with Multiple Properties
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721608) Composite Observable - Multiple Observable with operator = O1 AND O2 AND O3 under <stix:Indicators>
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721609) Composite Observable - Multiple Observable with operator = O1 OR O2 OR O3 under <stix:Indicators>
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5817217) Composite Observable - Multiple Observable under <stix:Observables>
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721621) Composite Observable - Multiple Observable and Composite Observable with operator = O1 OR (O2 AND (O3 OR O4)) under <stix:Indicators>
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721623) Composite Indicators - Multiple Indicators with operator = I1 AND I2 AND I3
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721624) Composite Indicators - Multiple Indicators with operator = I1 OR I2 OR I3
    [Tags]  FAST
    Truncate Tables
    Create Stix Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e9
    ${api}=  Set Variable  &{API_INFO}[extract_stix]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5721640) Extract IOC file with supported OpenIOC IndicatorItem Type - SHA1 and supported conditions "is"
    [Tags]  RAT
    Truncate Tables
    Create Openioc Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e0
    ${api}=  Set Variable  &{API_INFO}[extract_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5751993) Extract IOC file with supported OpenIOC IndicatorItem Type - URL and supported conditions "is"
    [Tags]  FAST
    Truncate Tables
    Create Openioc Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e0
    ${api}=  Set Variable  &{API_INFO}[extract_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5751994) Extract IOC file with supported OpenIOC IndicatorItem Type - DNS and supported conditions "Contains"
    [Tags]  FAST
    Truncate Tables
    Create Openioc Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e0
    ${api}=  Set Variable  &{API_INFO}[extract_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5751996) Extract IOC file with supported OpenIOC IndicatorItem Type - IP and supported conditions "is"
    [Tags]  FAST
    Truncate Tables
    Create Openioc Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e0
    ${api}=  Set Variable  &{API_INFO}[extract_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5734150) Extract IOC file with all "OR" operation
    [Tags]  FAST
    Truncate Tables
    Create Openioc Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e0
    ${api}=  Set Variable  &{API_INFO}[extract_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5734151) Extract IOC file with combination I1 or I2 or I3 or (G1) or (G2) or (G3) or (G4).
    [Tags]  FAST
    Truncate Tables
    Create Openioc Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e0
    ${api}=  Set Variable  &{API_INFO}[extract_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}

(C5734157) Extract IOC file with combination - Item1 or {Item2 and [Item3 or (Item4 and Item5)]}
    [Tags]  FAST
    Truncate Tables
    Create Openioc Data With Base64  ${TEST_NAME}  cfefc424fc95ce74ec7a8232de7d14ec659071e0
    ${api}=  Set Variable  &{API_INFO}[extract_openioc]
    ${response}=  Send Api Request  ${TEST_NAME}  ${api}
    Return Code Should Be  ${response}  200
    Response Body Should Be  ${TEST_NAME}  ${response}
    Extract Blacklist Table Should Be  ${TEST_NAME}
