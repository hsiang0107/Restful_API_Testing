*** Settings ***
Resource  ../resources/pageobjects/mdr/MDR.robot
Resource  ../resources/CM.robot

Test Setup  Begin Testing
Test Teardown  End Testing

*** Variables ***

*** Test Cases ***
Go To MDR and Register
    [Tags]  RAT
    Go To MDR Page
    Register MDR Service

Unregister
    Go To MDR Page
    Unregister MDR Service
