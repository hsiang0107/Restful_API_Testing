*** Variables ***
${MDR_PAGE_TITLE}  \#header > div > span

${MDR_PENDING_TAB}  div.tm-tabbable > ul > li:nth-child(1) > a
${MDR_HISTORY_TAB}  div.tm-tabbable > ul > li:nth-child(2) > a
${MDR_PTE_TAB}  div.tm-tabbable > ul > li:nth-child(3) > a
${MDR_SETTING_TAB}  div.tm-tabbable > ul > li:nth-child(4) > a

${MDR_APPROVE_BUTTON}  div.process-buttons > button:nth-child(1)
${MDR_REJECT_BUTTON}  div.process-buttons > button:nth-child(2)

# Setting tab
${MDR_SERVER_ADDRESS}  tr:nth-child(1) > td:nth-child(2) > input[type=\"text\"]
${MDR_SERVICE_TOKEN}  tr:nth-child(2) > td:nth-child(2) > input[type=\"text\"]
${MDR_REGISTER_BUTTON}  div.mdr-setting > div.footer > button
${MDR_SAVE_BUTTON}  div.footer > button.tm-btn.tm-btn-primary
${MDR_CANCEL_BUTTON}  div.footer > button:nth-child(2)
${MDR_UNREGISTER_BUTTON}  div.mdr-setting > div.footer > button:nth-child(3)
${MDR_CONFIRM_UNREGISTER}  div.tm-modal-footer > button.tm-btn.tm-btn-primary
${MDR_CANCEL_UNREGISTER}  div.tm-modal-footer > button.tm-btn.tm-btn-default
${MDR_PAUSE_MDR}  div.footer > button:nth-child(4)
${MDR_AUTO_APPROVE}  td:nth-child(2) > div > div
