*** Settings ***
Resource  inventory_view_variable.robot

*** Variable ***


*** Keywords ***
Click Advanced Link
    Click Element  css=${INVENTORY_VIEW_ADVANCED_LINK}

Click Criteria Dropdown
    Click Element  css=${INVENTORY_VIEW_CRITERIA_DROPDOWN}

Switch to Endpoints
    Click Criteria Dropdown
    Click Element   css=${INVENTORY_VIEW_ENDPOINTS_OPTION}

Select Compliance
    Switch to Endpoints
    Click Element   xpath=${INVENTORY_VIEW_COMPLIANCE_OPTION}

Go To Threat View of ${Threat}
    Sort Table by THREAT
    Click Element  css=${INVENTORY_VIEW_TABLE_FIRST_THREAT_RECORD_LINK}
    Wait Until Page Contains Element  xpath=//a[contains(.,"${Threat}")]
    Click Element  xpath=//a[contains(.,"${Threat}")]

Sort Table by ${Header}
    Wait Until Page Contains Element  css=${INVENTORY_VIEW_TABLE_${Header}_HEADER}
    Click Element  css=${INVENTORY_VIEW_TABLE_${Header}_HEADER}
    Wait Until Page Contains Element  css=${INVENTORY_VIEW_TABLE_FIRST_THREAT_RECORD_LINK}

Start Assess Impact
    Wait Until Page Contains Element  css=${INVENTORY_VIEW_ASSESS_IMPACT_BUTTON}
    Click Element  css=${INVENTORY_VIEW_ASSESS_IMPACT_BUTTON}

Check UI After Clicking Assess Impact
    Element Text Should Be  css=${INVENTORY_VIEW_PREVIOUSLY_UNDETECTED_LABEL}  Previously undetected (Assessing impact...)

Check Threat View Dots
    [Arguments]  @{colors}
    ${color_schema}=  Create dictionary  red=#ff000a  orange=#ff9900
    ${i}=  set variable  ${1}
    :FOR  ${color}  IN  @{colors}
    \  ${css}=  set variable  svg > g.highcharts-series-group > g:nth-child(2) > path:nth-child(${i})
    \  Page Should Contain Element  css=${css}
    \  ${actual_color_schema}=  Get Element Attribute  css=${css}  fill
    \  ${expect_color_schema}=  Evaluate  ${color_schema}.get('${color}')
    \  Should Be Equal  ${actual_color_schema}  ${expect_color_schema}  color schema does not match
    \  ${i}=  Evaluate  ${i}+${1}
