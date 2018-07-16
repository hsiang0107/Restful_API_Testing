*** Variables ***
${VASO_TYPE_DROP_DOWN}  select.dataGroupFilter
${VASO_SEARCH_INPUT}  input.keyword
${VASO_TAB}  a.feedbackSO
${VASO_EXPORT_ALL}  div.export_all
${VASO_ADD_TO_EXCEPTION}  div.add_to_exception
${VASO_NEVER_EXPIRE}  div.never_expire
${VASO_EXPIRE_NOW}  div.expire_now
${VASO_CONFIGURE_ACTION}  div.configure_scan_action
${VASO_ASSESS_IMPACT}  div.assess_impact
${VASO_SELECT_ALL}  input.checkAll
${VASO_SMAPLE_SUBMISSION}  \#tabContainer > li:nth-child(1) > span
${VASO_ANALYSIS}  \#tabContainer > li:nth-child(2) > span
${VASO_DISTRIBUTION}  \#tabContainer > li:nth-child(3) > span
${VASO_IMPACT_ASSESS_MITIGATION}  \#tabContainer > li:nth-child(3) > span
${VASO_HANDLING_PROCESS_BACK}  \#header > div > span > a > i
${VASO_LATEST_ACTION_RESULT}  \#VAFE_atRiskEndpointGrid > div.headerScrollerWrap > div > div.column.column-ellipsis.actionResult_col > span

${VASO_EXCEPTION_TAB}  a.exceptionSO
${VASO_EXCEPTION_ADD}  div.add
${VASO_EXCPETION_IMPORT}  div.import
${VASO_EXCEPTION_EXPORT_ALL}  div.export_all
${VASO_EXCEPTION_DELETE}  div.delete
${VASO_EXCEPTION_ADD_TYPE}  select.typeOptions
${VASO_EXCEPTION_ADD_DATA}  input.newSuspiciousObject
${VASO_EXCEPTION_ADD_NOTE}  textarea.newNote
${VASO_EXCEPTION_ADD_CONFIRM}  \#save_layout > div.mid
${VASO_EXCEPTION_ADD_CANCEL}  \#cancel_layout > div.mid

${CONFIG_SCANACTION_TABLE}  \#modalConfigureScanAction > table > tbody > tr > td
${CONFIG_SCANACTION_CUSTOMIZE_CHECKBOX}  .button.customizeByRiskLevelCheckBox
${CONFIG_SCANACTION_FOR_ALL_FILES_DROPDOWN}  .forAllRiskLevelFiles .scanActionOptions
${CONFIG_SCANACTION_FOR_ALL_IPS_DROPDOWN}  .forAllRiskLevelIPs .scanActionOptions
${CONFIG_SCANACTION_FOR_ALL_URLS_DROPDOWN}  .forAllRiskLevelURLs .scanActionOptions
${CONFIG_SCANACTION_FOR_ALL_DOMAINS_DROPDOWN}  .forAllRiskLevelDomains .scanActionOptions
${CONFIG_SCANACTION_FOR_ALL_APPLTO_DROPDOWN}  .forAllRiskLevels.applyToScope .applyToScopeOptions
${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_HIGH_RISK_ACTION_DROPDOWN}  .forDomains.riskLevelHigh .scanActionOptions
${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_HIGH_RISK_APPLYTO_DROPDOWN}  .forDomains.riskLevelHigh .applyToScopeOptions
${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_MEDIUM_RISK_ACTION_DROPDOWN}  .forDomains.riskLevelMedium .scanActionOptions
${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_MEDIUM_RISK_APPLYTO_DROPDOWN}  .forDomains.riskLevelMedium .applyToScopeOptions
${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_LOW_RISK_ACTION_DROPDOWN}  .forDomains.riskLevelLow .scanActionOptions
${CONFIG_SCANACTION_FOR_DETAIL_DOMAIN_LOW_RISK_APPLYTO_DROPDOWN}  .forDomains.riskLevelLow .applyToScopeOptions
