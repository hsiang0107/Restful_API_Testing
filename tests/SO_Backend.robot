*** Settings ***
Resource  ../resources/CM.robot
Library  ../resources/backend_objects/so_backend.py
Library  ../lib/DBHelper.py
Library  ../lib/log_creator.py


Suite Setup  SO Backend Suite Setup
Test Setup
Test Teardown  Clear SO Logs
Suite Teardown

*** Variable ***


*** Test Cases ***
(RAT-0001)Blacklist log - 1 record for each type
    [Tags]  RAT
    ${ip_so}=  Create SO Log  server_name=DDI01  SLF_RiskLevel=1  SLF_Type=0  SLF_Data=168.95.1.1
    ${url_so}=  Create SO Log  server_name=DDI02  SLF_RiskLevel=2  SLF_Type=1
    ...  SLF_Data=http://www.virus8.com:88/index.php?virus=8
    ${file_so}=  Create SO Log  server_name=DDI01  SLF_RiskLevel=3  SLF_Type=2
    ...  SLF_Data=2EF7BDE608CE5404E97D5F042F95F89F1C232871
    ${domain_so}=  Create SO Log  server_name=DDI02  SLF_RiskLevel=2  SLF_Type=3
    ...  SLF_Data=www.virus.com

    Execute Store Procedure  sp_UpdateBlacklist
    Big Watermark Should be Correct  tb_logblacklistinfojournal=4

    Check Blacklist Table From LogBlacklistInfoJournal  ${ip_so}  ScanAction=1  HasAssessed=0  Status=1
    ...  SLF_Key=0x574876b4fb5b2e40d044452abe7996d5
    Check Blacklist Table From LogBlacklistInfoJournal  ${url_so}  ScanAction=1  HasAssessed=0  Status=1
    Check Blacklist Table From LogBlacklistInfoJournal  ${file_so}  ScanAction=1  HasAssessed=0  Status=1
    ...  SLF_Key=0x68a72673a42856a1c11c1b1d6e40e326
    Check Blacklist Table From LogBlacklistInfoJournal  ${domain_so}  ScanAction=1  HasAssessed=0  Status=1
    ...  SLF_Key=0xd704acd89cd6c9e93c4526ba3164895c
