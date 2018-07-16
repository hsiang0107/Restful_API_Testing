*** Settings ***
Resource  SO_distribution_variable.robot

*** Keywords ***
Go To Managed Server Tab
    Click Element  id=${DIRTRIBUTION_MANAGED_PRODUCTS_TAB}

Go To Tipping Point Tab
    Click Element  id=${DIRTRIBUTION_TP_TAB}

Go To Hub CM Tab
    Click Element  id=${DIRTRIBUTION_HUB_CM_TAB}
