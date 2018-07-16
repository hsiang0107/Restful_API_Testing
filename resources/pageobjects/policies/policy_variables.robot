*** Variables ***
# Product Types Drop-Down List
${PRODUCT_ID_DROPDOWN}  select.product_id_select

# How to Create Policy Dialog
${HOW_TO_DIALOG_CLOSE_BUTTON}  \#modalHowCreatePolicy div.mid

# Policy Menus
${POLICY_CREATE_BUTTON}  .btn_create.first

# Policy Options
${POLICY_TYPE_DRAFT_RADIO}  \#lockFlag_1

# Filter By Criteria
${POLICY_TYPE_FILTER_RADIO}  \#lockFlag_2
${POLICY_SET_FILTER_BUTTON}  .configure_rule
${POLICY_DIRECTORIES_CHECKBOX}  .criteria_policy_rule_checked_folder
${POLICY_DIRECTORIES_DROPDOWN}  .criteria_policy_rule_directories_selection
${POLICY_PRODUCT_DIRECTORY_AREA}  \#ProductDirectory
${POLICY_AD_DIRECTORY_AREA}  \#ADResource
${POLICY_OFFICESCAN_DOMAIN_HIERARCHY_AREA}  \#TreePath

# Specify Targets
${POLICY_TYPE_TARGETS_RADIO}  \#lockFlag_3
