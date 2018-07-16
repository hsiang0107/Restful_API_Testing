*** Settings ***
Resource  ../resources/CM.robot
Resource  ../resources/pageobjects/inventory_view/inventory_view.robot
Library  ../resources/pageobjects/inventory_view/ies_backend_integration.py
Library  ../lib/log_creator.py

Suite Setup  Prepare for iES Backend Testing
Suite Teardown  End Testing
Test Teardown  Ies Backend Case Teardown

*** Keywords ***
Prepare for iES Backend Testing
    Ies Backend Suite Setup
    Begin Testing


*** Variable ***
${Ruleid_VASO_file}  708


*** Test Cases ***
(C4918541)Trigger sha1 quick inv and no matched result from iES
    [Tags]  FAST
    Change Testing Data  C4918541
    Create CAV Log  SLF_InterestedIP=100.1.1.1  RuleID=${Ruleid_VASO_file}  SLF_CCCA_Destination=27EF11C24A1D336F46C69762B655A1495656820F
    ...  SHA1=27EF11C24A1D336F46C69762B655A1495656820F
    Sleep  10
    Go To Inventory View
    Go To Threat View of 27EF11C24A1D336F46C69762B655A1495656820F
    Start Assess Impact
    Check UI After Clicking Assess Impact
    Sleep  5
    Go To Inventory View
    Go To Threat View of 27EF11C24A1D336F46C69762B655A1495656820F
    Check Threat View Dots  red
    Check Quick Inv Result  criteria=27EF11C24A1D336F46C69762B655A1495656820F  criteria_type=5  no_match=${True}


(C4918542)Trigger IP quick inv and iES return matched result
    [Tags]  RAT
    Change Testing Data  case_id=C4918542
    Create NCIE Log  SLF_ComputerName=Client11  SLF_DestinationIP=202.80.1.1
    Sleep  10
    Go To Inventory View
    Go To Threat View of 202.80.1.1
    Start Assess Impact
    Check UI After Clicking Assess Impact
    Sleep  5
    Go To Inventory View
    Go To Threat View of 202.80.1.1
    Check Threat View Dots  red  orange  orange
    Check Quick Inv Result  criteria=202.80.1.1  criteria_type=2  agents=Client12,Client13
    Check Init RCA Result  criteria=202.80.1.1  criteria_type=2  agents=Client12,Client13


(C4918543)Trigger Domain quick inv and iES return invalid result
    [Tags]  FET
    Change Testing Data  case_id=C4918543
    Create NCIE Log  SLF_ComputerName=Client11  SLF_DestinationDomain=TEST.IES.COM
    Sleep  10
    Go To Inventory View
    Go To Threat View of TEST.IES.COM
    Start Assess Impact
    Check UI After Clicking Assess Impact
    Sleep  5
    Check Quick Inv Result  criteria=TEST.IES.COM  criteria_type=1  fet=${True}  no_match=${True}


(C4918592)CM should should not create multiple record into match object table if there are duplicate agent ID and criteria in journal table
    [Tags]  FAST
    Change Testing Data  case_id=C4918592
    Create Virus Log  CLF_ComputerName=Client11  SLF_FileSHA1=CAED1FB5039A8F0CDDD6A23C4DDDBF7285531569  VLF_VirusName=OMG_SO_Horrify
    Sleep  10
    Go To Inventory View
    Go To Threat View of OMG_SO_Horrify
    Start Assess Impact
    Check UI After Clicking Assess Impact
    Sleep  5
    Go To Inventory View
    Go To Threat View of OMG_SO_Horrify
    Check Threat View Dots  orange  orange  orange  orange  orange
    Check Quick Inv Result  criteria=CAED1FB5039A8F0CDDD6A23C4DDDBF7285531569  criteria_type=5  agents=Client11,Client12,Client13,Client14,Client15
    Check Init RCA Result  criteria=CAED1FB5039A8F0CDDD6A23C4DDDBF7285531569  criteria_type=5  agents=Client11,Client12,Client13,Client14,Client15


(C4918672)Trigger one quick inv containing multiple SHA1 value
    [Tags]  FAST
    Change Testing Data  case_id=C4918672
    Create Virus Log  CLF_ComputerName=Client11  SLF_FileSHA1=CAED1FB5039A8F0CDDD6A23C4DDDBF7285531569  VLF_VirusName=OMG_SO_Horrify
    Create Virus Log  CLF_ComputerName=Client11  SLF_FileSHA1=C3E4DDCA70ED53C3BB6678B4DDC398C474A65BDB  VLF_VirusName=OMG_SO_Horrify
    Create Virus Log  CLF_ComputerName=Client11  SLF_FileSHA1=443DDF9616EA43F8898FFCF7A5BA7E43CBDCA874  VLF_VirusName=OMG_SO_Horrify
    Sleep  10
    Go To Inventory View
    Go To Threat View of OMG_SO_Horrify
    Start Assess Impact
    Check UI After Clicking Assess Impact
    Sleep  5
    Go To Inventory View
    Go To Threat View of OMG_SO_Horrify
    Check Case Result C4918672


(C5019997)CM timeout task
    [Tags]  FAST
    Create Test Data For C5019997
    Sleep  5
    Check Task Should Be Timeout


(C4918545)submit sha1 RCA task and iES return affected
    [Tags]  FAST
    Change Testing Data  case_id=C4918545
    Create RCA Test Data  match_agent=Client11  criteria=B9B76DCB9EACE405028811E7F4E23E0B33643710  criteria_type=5
    Sleep  5
    Check Finished RCA Result  criteria=B9B76DCB9EACE405028811E7F4E23E0B33643710  agent=Client11


(C4944292)submit IP, Domain and SHA1 RCA task and iES return not affected for IP, affected for SHA1, Domain
    [Tags]  FAST
    Change Testing Data  case_id=C4944292
    Create RCA Test Data  match_agent=Client11  criteria=DCB63A930713A07525AE07A149F1A2DF911925E0  criteria_type=5
    ...  slf_key=0x5fa3ac39560cb7f8a1e794840
    Create RCA Test Data  match_agent=Client11  criteria=aa.bb.com  criteria_type=1  slf_key=0x4fa3ac39560cb7f8a1e794840
    Create RCA Test Data  match_agent=Client11  criteria=100.1.1.1  criteria_type=2  slf_key=0x8a3ac3955960cb7f81e794840
    Sleep  5
    Check Finished RCA Result  criteria=DCB63A930713A07525AE07A149F1A2DF911925E0  agent=Client11
    Check Finished RCA Result  criteria=aa.bb.com  agent=Client11  status=4  sync=1
    Check Finished RCA Result  criteria=100.1.1.1  agent=Client11  status=4  affected=0  sync=0


(C4918594)CM should aggregate RCA agent into one request if they have same criteria
    [Tags]  FAST
    Change Testing Data  case_id=C4918594
    Create RCA Test Data  match_agent=Client11  criteria=aa.bb.com  criteria_type=1  slf_key=0x4fa3ac39560cb7f8a1e794840
    Create RCA Test Data  match_agent=Client12  criteria=aa.bb.com  criteria_type=1  slf_key=0x4fa3ac39560cb7f8a1e794840
    Create RCA Test Data  match_agent=Client13  criteria=aa.bb.com  criteria_type=1  slf_key=0x4fa3ac39560cb7f8a1e794840
    Create RCA Test Data  match_agent=Client14  criteria=aa.bb.com  criteria_type=1  slf_key=0x4fa3ac39560cb7f8a1e794840
    Create RCA Test Data  match_agent=Client15  criteria=aa.bb.com  criteria_type=1  slf_key=0x4fa3ac39560cb7f8a1e794840

    Create RCA Test Data  match_agent=Client11  criteria=100.1.1.1  criteria_type=2  slf_key=0x8a3ac3955960cb7f81e794840
    Create RCA Test Data  match_agent=Client12  criteria=100.1.1.1  criteria_type=2  slf_key=0x8a3ac3955960cb7f81e794840
    Create RCA Test Data  match_agent=Client13  criteria=100.1.1.1  criteria_type=2  slf_key=0x8a3ac3955960cb7f81e794840
    Create RCA Test Data  match_agent=Client14  criteria=100.1.1.1  criteria_type=2  slf_key=0x8a3ac3955960cb7f81e794840
    Create RCA Test Data  match_agent=Client15  criteria=100.1.1.1  criteria_type=2  slf_key=0x8a3ac3955960cb7f81e794840
    Sleep  5
    Check Case Result C4918594


(C4918657)iES return timeout for one RCA result
    [Tags]  FAST
    Change Testing Data  case_id=C4918657
    Create RCA Test Data  match_agent=Client11  criteria=aa.bb.com  criteria_type=1  slf_key=0x4fa3ac39560cb7f8a1e794840
    Sleep  5
    Check Finished RCA Result  criteria=aa.bb.com  agent=Client11  status=5  affected=0  sync=0


(C4918653)CM Should periodically send request for querying ongoing task even if there is no task
    [Tags]  FAST
    Change Testing Data  case_id=C4918653
    Create Test Data For C4918653
    Sleep  10
    Check Quick Inv Result  criteria=factory.com.tw  criteria_type=1  no_match=${True}
    Check Quick Inv Result  criteria=factory.com.nz  criteria_type=1  no_match=${True}
    Check Finished RCA Result  criteria=factory.com.tw  agent=Client11  status=4  affected=0  sync=0  skip_match_obj=${True}
    Check Finished RCA Result  criteria=factory.com.nz  agent=Client11  status=4  affected=0  sync=0  skip_match_obj=${True}


(C4918670)can only handle 100000 hit records per scheduler
    [Tags]  FAST
    Change Testing Data  case_id=C4918670
    Create File Hash Detection Log  affected_client=Client11  SLF_FileSHA1=BDDA7ED0A22A4CD37241CD33DD20B5FBD061CF56
    Sleep  10
    Go To Inventory View
    Go To Threat View of BDDA7ED0A22A4CD37241CD33DD20B5FBD061CF56
    Start Assess Impact
    Sleep  5
    Check Case Result C4918670


(C4918674)Trigger SHA1 Retro scan and RCA return affected
    [Tags]  FAST
    Change Testing Data  case_id=C4918674
    Create File Hash Detection Log  affected_client=Client11  SLF_FileSHA1=ADDA7ED0A22A4CD37241CD33DD20B5FBD061CF56
    Sleep  10
    Go To Inventory View
    Go To Threat View of ADDA7ED0A22A4CD37241CD33DD20B5FBD061CF56
    Start Assess Impact
    Sleep  5
    Go To Inventory View
    Go To Threat View of ADDA7ED0A22A4CD37241CD33DD20B5FBD061CF56
    Check Quick Inv Result  criteria=ADDA7ED0A22A4CD37241CD33DD20B5FBD061CF56  criteria_type=5  agents=Client24,Client25  no_rca=${False}
    Check Finished RCA Result  criteria=ADDA7ED0A22A4CD37241CD33DD20B5FBD061CF56  agent=Client24  status=4  affected=1  sync=1
    Check Finished RCA Result  criteria=ADDA7ED0A22A4CD37241CD33DD20B5FBD061CF56  agent=Client25  status=4  affected=0  sync=0
