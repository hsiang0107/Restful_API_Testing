*** Variables ***
${UDSO_IMPORT}  li.btn_import > div
${UDSO_EXPORT}  li.btn_export_all > div
${UDSO_DELETE}  li.btn_delete > div
${UDSO_DELETE_DISABLE}  li.btn_delete.disable > div
${UDSO_SELECT_ALL}  th.checkAllTH > input
${UDSO_SELECT_TYPE}  \#userDefinedSO > div > div.view > select
${UDSO_SEARCH_INPUT}  \#userDefinedSO > div > div.view > span.searchBar > input
${UDSO_SEARCH}  \#userDefinedSO > div > div.view > span.searchBar > span.search

# Add UDSO
${UDSO_ADD}  li.btn_add.first > div
${UDSO_ADD_TABLE}  \#modalAdd > table > tbody > tr > td
${UDSO_ADD_TYPE}  tr:nth-child(1) > td:nth-child(2) > select
${UDSO_ADD_FILE_BROWSE}  \#browsebtn > div.mid
${UDSO_ADD_INPUT}  tr:nth-child(3) > td:nth-child(2) > input
${UDSO_ADD_EDIT_SCANACTION}  tr.scanAction > td:nth-child(2) > select
${UDSO_ADD_EDIT_NOTE_INPUT}  tr:nth-child(7) > td:nth-child(2) > textarea
${UDSO_ADD_EDIT_SAVE}  \#save_layout > div.mid
${UDSO_ADD_EDIT_CANCEL}  \#cancel_layout > div.mid

# Edit UDSO
${UDSO_EDIT}  li.btn_edit > div
${UDSO_EDIT_DISABLE}  li.btn_edit.disable > div

# STIX
${STIX_TAB}  .tm-nav-tabs > li:nth-child(2)
${STIX_ADD_BUTTON}  .ioc-table-button-area > button:nth-child(1)
${STIX_DELETE_BUTTON}  .ioc-table-button-area > button:nth-child(2)
${STIX_ADD_MODAL_ADD_BUTTON}  .ioc-modal-footer > button:nth-child(1)

# OpenIOC
${OPENIOC_TAB}  .tm-nav-tabs > li:nth-child(3)
${OPENIOC_ADD_BUTTON}  .ioc-table-button-area > button:nth-child(1)
${OPENIOC_DELETE_BUTTON}  .ioc-table-button-area > button:nth-child(2)
${OPENIOC_INVESTIGATE_BUTTON}  .ioc-table-button-area > div > button
${OPENIOC_EXTRACT_BUTTON}  .ioc-table-button-area > button:nth-child(4)

${FRAME_UDSO}  iframe[title="udsoIframe"]
