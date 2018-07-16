*** Variables ***
# AD
${AD_SETTING_TAB}  li:nth-child(1) > a
${AD_SETTING_ON_OFF_CHECKBOX}  div.ad-connection-setting > div:nth-child(1) > div > div > div
${AD_SETTING_SERVER_ADDRESS_INPUT}  tr:nth-child(<REPLACE_ME>) > td:nth-child(2) > input[type=\"text\"]
${AD_SETTING_SERVER_USER_INPUT}  tr:nth-child(<REPLACE_ME>) > td:nth-child(3) > input[type=\"text\"]
${AD_SETTING_SERVER_PASSWORD_INPUT}  tr:nth-child(<REPLACE_ME>) > td:nth-child(4) > input[type=\"password\"]
${AD_SETTING_SYNC_FREQUENCY_DROPDOWN}  select
${AD_SETTING_SAVE_BUTTON}  .footer > div > button:nth-child(1)
${AD_SETTING_CANCEL_BUTTON}  .footer > div > button:nth-child(1)
${AD_SETTING_TESTING_BUTTON}  div.footer > div > div > button
${AD_SETTING_SYNCNOW_BUTTON}  div.footer > button:nth-child(2)
${AD_SETTING_CLEAR_DATA_BUTTON}  div.footer > button:nth-child(3)
${AD_SETTING_ADD_FIRST_BUTTON}  tr:nth-child(2) > td:nth-child(5) > span
${AD_SETTING_ADD_BUTTON}  tr:nth-child(<REPLACE_ME>) > td:nth-child(5) > span.add
${AD_SETTING_REMOVE_BUTTON}  tr:nth-child(<REPLACE_ME>) > td:nth-child(5) > span

# compliance indicator
${COMPLIANCE_TAB}  li:nth-child(2) > a
${COMPLIANCE_LOW_SCROLL}  div.handle.handle-0 > div > div.alert-level-handle-msg > div > span > div
${COMPLIANCE_HIGH_SCROLL}  div.handle.handle-1 > div > div.alert-level-handle-msg > div > span > div
${COMPLIANCE_ADD_EXCEPTION_BUTTON}  div.exception-list > div.ad-toolbar > div > a
${COMPLIANCE_ADD_EXCEPTION_LINK}  table > tbody:nth-child(1) > tr > td > div > div > a
${COMPLIANCE_ALL_ACCOUNTS_RADIO}  div.ad-toolbar > div > label:nth-child(3) > input[type=\"radio\"]
${COMPLIANCE_LOGGED_ACCOUNT_RADIO}  div.ad-toolbar > div > label:nth-child(4) > input[type=\"radio\"]
${COMPLIANCE_SAVE_BUTTON}  .setting-footer > button:nth-child(1)
${COMPLIANCE_CANCEL_BUTTON}  .setting-footer > button:nth-child(2)
${COMPLIANCE_EXCPETION_TYPE_DROPDOWN}  div.add-exception-modal.tm-modal-body > div > select
${COMPLIANCE_EXCEPTION_SEARCH_INPUT}  div.add-exception-input > input[type=\"text\"]
${COMPLIANCE_EXCEPTION_APPLY_BUTTON}  div:nth-child(2) > button.tm-btn-primary.tm-btn.tm-btn-default
${COMPLIANCE_EXCEPTION_CLOSE_BUTTON}  div:nth-child(2) > button:nth-child(2)
${COMPLIANCE_ANTI_VIRUS_TAB}  div.ad-compliance > div > ul > li:nth-child(1) > a
${COMPLIANCE_PATTERN_VERSION_SELECT_DROPDOWN}  select
${COMPLIACE_DLP_TAB}  div.ad-compliance > div > ul > li:nth-child(2) > a
${COMPLIANCE_DLP_DAY_PERIOD_DROPDOWN}  Div:nth-child(2) > div:nth-child(1) > select
${COMPLIANCE_DLP_ACCEPTABLE_DETECTION_INPUT}  div:nth-child(2) > div:nth-child(2) > input

# sites and reporting lines
${SITES_TAB}  li:nth-child(3) > a
${REPORTING_LINES_TAB}  li:nth-child(4) > a
${ADD_CUSTOM_BUTTON}  div.ad-toolbar > div:nth-child(1) > a
${DELETE_CUSTOM_BUTTON}  div.ad-toolbar > div:nth-child(2) > a
${MERGE_CUSTOM_BUTTON}  div.ad-toolbar > div:nth-child(3) > a
${SPLIT_CUSTOM_BUTTON}  div.ad-toolbar > div:nth-child(4) > a
${ADD_SITE_DISPLAY_NAME_INPUT}  td:nth-child(2) > input[type=\"text\"]
${ADD_SITE_IP_RANGES_INPUT}  td:nth-child(2) > div > textarea
${SITE_REPORTING_LINES_SAVE_BUTTON}  button.col.tm-btn.tm-btn-primary
${SITE_REPORTING_LINES_CANCEL_BUTTON}  button.col.tm-btn.tm-btn-default
${REPORTING_LINES_ADD_DiSPLAY_NAME_INPUT}  td:nth-child(2) > input[type=\"text\"]
${REPORTING_LINES_SEARCH_INPUT}  td:nth-child(1) > div:nth-child(1) > input
${REPORTING_LINES_SEARCH_BUTTON}  td:nth-child(1) > div:nth-child(1) > i