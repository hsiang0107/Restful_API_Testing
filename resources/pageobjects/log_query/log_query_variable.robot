*** Variables ***

${LOG_QUERY_SAVED_SEARCH_BUTTON}  .tmcm-btn-toolbar.flat.icon-in-button-group > div > button
${LOG_QUERY_FILTER}  section.commercial-theme.tmcm-theme.log > div > div > div.tmcm-btn-dropdown > button
${LOG_QUERY_SEARCH_BUTTON}  section.commercial-theme.tmcm-theme.log > div > div > button
${LOG_QUERY_ADVANCED_FILTER_LINK}  a.inlinelink.showhidelink
${LOG_QUERY_ADVANCED_FILTER_MATCH_RADIO}  .AdvancedFilters input[type=radio]
${LOG_QUERY_AND_RADIO}  input[Name=MatchCondition][value=true]
${LOG_QUERY_OR_RADIO}  input[Name=MatchCondition][value=false]
${LOG_QUERY_DATA_VIEW_DROPDOWN}  .logDataView > div:nth-child(1) > button:nth-child(1)
${LOG_QUERY_DATA_VIEW_DROPDOWN_OK_BUTTON}  .open > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)
${LOG_QUERY_PRODUCT_DROPDOWN}  .commercial-theme > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)
${LOG_QUERY_PRODUCT_DROPDOWN_OK_BUTTON}  div.control-panel:nth-child(4) > button:nth-child(1)
${LOG_QUERY_TIME_RANGE_DROPDOWN}  div.tm-btn-group:nth-child(3) > button:nth-child(1)
${LOG_QUERY_TIME_RANGE_DROPDOWN_ITEM}  .dp-dropdown-menu li[data-reactid*="%s"]
${LOG_QUERY_TABLE_CONTAINER}  .logQuery-table-container
${LOG_QUERY_LOG_TOTAL_COUNT_LABEL}  tfoot > tr > td:nth-child(1) > span:last-child
${LOG_QUERY_HOST_DETAILS_LINK}  td[title="Host Details"] a
${LOG_QUERY_BACK_BUTTON_HIDE}  button.btn-back.hide
${LOG_QUERY_CUSTOMIZE_COLUMNS_DROPDOWN}  .log-btn-customerize-columns
${LOG_QUERY_CUSTOMIZE_COLUMNS_DROPDOWN_ITEM}  .log-btn-customerize-columns > .tm-dropdown-container span
${LOG_QUERY_SAVE_QUERY_BUTTON}  .tm-btn-toolbar .tm-btn-group:nth-child(1)
${LOG_QUERY_SAVE_QUERY_NAME_TEXTBOX}  ${LOG_QUERY_SAVE_QUERY_BUTTON} input
${LOG_QUERY_SAVE_QUERY_SAVE_BUTTON}  ${LOG_QUERY_SAVE_QUERY_BUTTON} button:nth-child(1)
${LOG_QUERY_SAVED_QUERIES_BUTTON}  .tm-btn-toolbar .tm-btn-group:nth-child(2)
${LOG_QUERY_SAVED_QUERIES_ITEM}  ${LOG_QUERY_SAVED_QUERIES_BUTTON} li:last-child
${LOG_QUERY_SAVED_QUERIES_ITEM_DELETE_BUTTON}  ${LOG_QUERY_SAVED_QUERIES_ITEM} i[title="Delete"]
${LOG_QUERY_SAVED_QUERIES_ITEM_SHARE_BUTTON}  ${LOG_QUERY_SAVED_QUERIES_ITEM} i[title="Share"]
${LOG_QUERY_SAVED_QUERIES_ITEM_STOP_SHARING_BUTTON}  ${LOG_QUERY_SAVED_QUERIES_ITEM} i[title="Stop sharing"]
${LOG_QUERY_SAVED_QUERIES_ITEM_NAME_LABEL}  ${LOG_QUERY_SAVED_QUERIES_ITEM} .filter-name
@{LOG_QUERY_VIRUS_HOST_DETAIL_COLUMN_ITEMS}  Generated  Received  Product Entity/Endpoint  Product/Endpoint IP
...  Product  Managing Server Entity  Virus/Malware  Endpoint  User  Scan Type  File  File Path  File in Compressed File
...  Action  Result  Detections  Cloud Service Vendor
@{LOG_QUERY_MACHINE_LEARNING_COLUMN_ITEMS}  Detection Time  Received  Product Entity/Endpoint  Product/Endpoint IP
...  Product  Server  Probable Threat Type  Security Threat  Logon User  Type  File Path  File Creation Time
...  Parent Process  Process Command  Process Owner  Endpoint Infection Channel  Infection Source  Threat Probability
...  Action Result  Subject  Delivery Time  Sender  Recipients  Cloud Service Vendor
