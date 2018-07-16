*** Variables ***
${LOGIN_ACCOUNT_INPUT}  //*[@id="txtUserName"]
${LOGIN_PASSWORD_INPUT}  txtPassword
${LOGIN_BUTTON}  loginLink

# what's new close button
${WHATS_NEW_CLOSE_BUTTON}  button

# Account menu at the top right
${ACCOUNT_MENU_BUTTON}  \#option
${ACCOUNT_MENU_LOG_OFF_BUTTON}  \#account_menu > li > a.logout

# Menu xpath

${MENU_DASHBOARD_NAVIGATION}  ul:nth-child(3) > li > a

${MENU_DIRECTORIES_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[4]/li/a
${MENU_USER_ENDPOINTS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[4]/li/ul/li[1]/a
${MENU_PRODUCTS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[4]/li/ul/li[2]/a

${MENU_POLICIES_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[5]/li/a
${MENU_POLICY_MANAGEMENT_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[5]/li/ul/li[1]/a
${MENU_POLICY_RESOURCES_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[5]/li/ul/li[2]/a
${MENU_POLICY_TEMPLATE_SETTINGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[5]/li/ul/li[2]/ul/li[1]/a
${MENU_DLP_DATA_IDENTIFIERS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[5]/li/ul/li[2]/ul/li[2]/a
${MENU_DLP_TEMPLATES_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[5]/li/ul/li[2]/ul/li[3]/a

${MENU_LOGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[6]/li/a
${MENU_LOG_QUERY_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[6]/li/ul/li[1]/a
${MENU_LOG_AGGREGATION_SETTINGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[6]/li/ul/li[2]/a
${MENU_LOG_MAINTENANCE_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[6]/li/ul/li[3]/a

${MENU_NOTIFICATIONS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[7]/li/a
${MENU_EVENT_NOTIFICATIONS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[7]/li/ul/li[1]/a
${MENU_NOTIFICAITON_METHOD_SETTINGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[7]/li/ul/li[3]/a
${MENU_OCNTACT_GROUPS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[7]/li/ul/li[4]/a

${MENU_REPORTS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[8]/li/a
${MENU_MY_REPORTS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[8]/li/ul/li[1]/a
${MENU_ONE_TIME_REPORTS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[8]/li/ul/li[2]/a
${MENU_SCHEDULED_REPORTS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[8]/li/ul/li[3]/a
${MENU_CUSTOM_TEMPLATES_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[8]/li/ul/li[5]/a
${MENU_REPORT_MAINTENANCE_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[8]/li/ul/li[6]/a

${MENU_UPDATES_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[9]/li/a
${MENU_SCHEDULED_UPDATE_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[9]/li/ul/li[1]/a
${MENU_MANUAL_UPDATE_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[9]/li/ul/li[2]/a

${MENU_CONNECTED_THREAT_DEFENSE_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[10]/li/a
${MENU_THREAT_INTELLIGENCE_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[10]/li/ul/li[1]/a
${MENU_VASO_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[10]/li/ul/li[1]/ul/li[1]/a
${MENU_CUSTOM_INTELLIGENCE_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[10]/li/ul/li[1]/ul/li[2]/a
${MENU_DISTRIBUTION_SETTINGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[10]/li/ul/li[1]/ul/li[3]/a
${MENU_MDR_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[10]/li/ul/li[3]/a

${MENU_ADMINISTRATION_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/a
${MENU_ACCOUNT_MANAGEMENT_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[1]/a
${MENU_MY_ACCOUNT_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[1]/ul/li[1]/a
${MENU_USER_ACCOUNTS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[1]/ul/li[2]/a
${MENU_USER_ROLES_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[1]/ul/li[3]/a
${MENU_MANAGED_SERVERS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[2]/a
${MENU_SERVER_REGISTRATION_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[2]/ul/li[1]/a
${MENU_AGENT_COMMUNICATION_SCHEDULE_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[2]/ul/li[2]/a
${MENU_COMMUNICATION_TIME_OUT_SETTINGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[2]/ul/li[3]/a
${MENU_SECURITY_AGENT_DOWNLOAD_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[3]/a
${MENU_COMMAND_TRACKING_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[4]/a
${MENU_LICENSE_MANAGEMENT_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[5]/a
${MENU_CONTROL_MANAGER_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[5]/ul/li[1]/a
${MENU_MANAGED_PRODUCTS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[5]/ul/li[2]/a
${MENU_SETTINGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[6]/a
${MENU_PROXY_SETTINGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[6]/ul/li[1]/a
${MENU_WEB_CONSOLE_SETTINGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[6]/ul/li[2]/a
${MENU_SMART_PROTECTION_NETWORK_SETTINGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[6]/ul/li[3]/a
${MENU_AD_COMPLIANCE_SETTINGS_NAVIGATION}  //*[@id="trendMenu"]/div[2]/div/ul[11]/li/ul/li[6]/ul/li[4]/a

${FRAME_TMCM}  mainTMCM
