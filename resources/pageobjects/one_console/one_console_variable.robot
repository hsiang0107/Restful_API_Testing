*** Variables ***
${ONE_CONSOLE_PAGE_TITLE}  \#header > div > span
${ONE_CONSOLE_WIN64_RADIO}  li:nth-child(1) > label > input[type=\"radio\"]
${ONE_CONSOLE_WIN32_RADIO}  li:nth-child(2) > label > input[type=\"radio\"]
${ONE_CONSOLE_MAC_RADIO}  li:nth-child(3) > label > input[type=\"radio\"]
${ONE_CONSOLE_SERVER_SELECT}  div:nth-child(4) > div.css_td.item_content > select
${ONE_CONSOLE_DOWNLOAD_AGENT}  button.tm-btn.tm-btn-primary
${ONE_CONSOLE_GET_DOWNLOAD_LINK}  button:nth-child(2)