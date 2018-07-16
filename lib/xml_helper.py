import os
from lib.ConfigHelper import ConfigHelper
from lib.xml_parser import get_attribute_value, update_attribute


def remove_hiding_pages_from_system_configuration():
    xpath = './/P[@Name="m_MenuIdHideList"]'
    cm_root_path = ConfigHelper().get_data_from_config('CM', 'folder')
    page_numbers = ConfigHelper().get_data_from_config('CM', 'remove_hiding')
    sys_conf_path = os.path.join(cm_root_path, 'SystemConfiguration.xml')
    hide_pages = get_attribute_value(sys_conf_path, xpath, 'Value').split(';')
    for n in page_numbers:
        if n in hide_pages:
            hide_pages.remove(n)
    update_attribute(sys_conf_path, xpath, 'Value', ';'.join(hide_pages))


def update_system_configuration(key, value):
    xpath = './/P[@Name="%s"]' % key
    cm_root_path = ConfigHelper().get_data_from_config('CM', 'folder')
    sys_conf_path = os.path.join(cm_root_path, 'SystemConfiguration.xml')
    update_attribute(sys_conf_path, xpath, 'Value', value)


def update_schedule_job_time(job_id, time):
    xpath = './/Job[@id="%s"]/Schedule' % job_id
    cm_root_path = ConfigHelper().get_data_from_config('CM', 'folder')
    sys_conf_path = os.path.join(cm_root_path, 'ScheduleJobSetting.xml')
    update_attribute(sys_conf_path, xpath, 'interval', time)
