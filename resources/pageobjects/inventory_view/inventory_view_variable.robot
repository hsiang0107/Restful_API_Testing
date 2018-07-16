*** Variables ***
${INVENTORY_VIEW_ADVANCED_LINK}                 div.block.block2 > a
${INVENTORY_VIEW_TYPE_DROPDOWN}                 div.leftSide > span > div > span:nth-child(2) > select
${INVENTORY_VIEW_CRITERIA_DROPDOWN}             div.section.section1.interval > select
${INVENTORY_VIEW_ENDPOINTS_OPTION}              div.leftSide > span > div > span:nth-child(2) > select > option:nth-child(2)
${INVENTORY_VIEW_THREATTYPE_OPTION}             //select[@name="criteria"]//option[@value="AdvU_ThreatType"]
${INVENTORY_VIEW_SECURITYTHREAT_OPTION}         //select[@name="criteria"]//option[@value="AdvU_SecurityThreat"]
${INVENTORY_VIEW_IMPORTANCE_OPTION}             //select[@name="criteria"]//option[@value="AdvU_Importance"]
${INVENTORY_VIEW_THREATSTATUS_OPTION}           //select[@name="criteria"]//option[@value="AdvE_ActionStatus"]
${INVENTORY_VIEW_ACTIVEDIRECTORYSITE_OPTION}    //select[@name="criteria"]//option[@value="AdvE_ADSite"]
${INVENTORY_VIEW_REPORTINGLINE_OPTION}          //select[@name="criteria"]//option[@value="AdvE_ReportLine"]
${INVENTORY_VIEW_COMPLIANCE_OPTION}             //select[@name="criteria"]//option[@value="AdvE_Compliance"]
${INVENTORY_VIEW_ANTIVIRUSPATTERN_OPTION}       //select[@name="AdvE_Compliance_Category_Key"]//option[@value="malware"]
${INVENTORY_VIEW_DATALOSSPREVENTION_OPTION}     //select[@name="AdvE_Compliance_Category_Key"]//option[@value="idlp"]
${INVENTORY_VIEW_FULLYCOMPLIANT_OPTION}         //select[@name="AdvE_Compliance_Key"]//option[@value="0"]
${INVENTORY_VIEW_NONCOMPLICANT_OPTION}          //select[@name="AdvE_Compliance_Key"]//option[@value="1"]
${INVENTORY_VIEW_UNREACHABLE_OPTION}            //select[@name="AdvE_Compliance_Key"]//option[@value="2"]
${INVENTORY_VIEW_TABULARVIEW_OPTION}            //select[@name="viewMode"]//option[@value="grid"]
${INVENTORY_VIEW_TIMELINEVIEW_OPTION}           //select[@name="viewMode"]//option[@value="timeline"]
${INVENTORY_VIEW_TABLE_THREAT_HEADER}    th:nth-child(7) > div.sort-indicator.th-text.fixed-row-height
${INVENTORY_VIEW_TABLE_FIRST_THREAT_RECORD_LINK}  td > table > tbody > tr:nth-child(1) > td:nth-child(7) > a
${INVENTORY_VIEW_ASSESS_IMPACT_BUTTON}  \#retroScanBtn
${INVENTORY_VIEW_PREVIOUSLY_UNDETECTED_LABEL}  div.highcharts-legend > div > div > div:nth-child(2) > span > span
