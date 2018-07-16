import os
import time
import requests
from lib.DBHelper import *
from lib.ConfigHelper import ConfigHelper
from lib import DBHelper, xml_helper, process_helper
from lib.LogSender.LogSender import LogSender
from robot.utils.asserts import assert_equal, assert_not_none, assert_none
from db.factory_boy import *


def ies_backend_suite_setup():
    test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  '..', '..', '..', 'tests', 'testdata', 'iES_backend_integration', 'Initialize')
    LogSender().register_with_csv_file('Init', test_data_path, with_status=False)
    LogSender().send_log(test_data_path + '\status.csv')
    time.sleep(5)
    DBHelper.execute_store_procedure('sp_SyncEntityIPAddress')
    xml_helper.update_system_configuration('m_iES_TaskForceExecuteTimeIntervalInSec', '5')
    xml_helper.update_schedule_job_time('12', '5')
    process_helper.kill_log_processor()


def ies_backend_case_teardown():
    clear_iES_backend_logs()
    clear_inventory_logs()
    clear_ncie_logs()
    clear_tda_logs()
    clear_virus_logs()
    clear_file_hash_detection_logs()
    clear_global_retroscan_task()
    reset_watermark()


def change_testing_data(case_id):
    mock_server = ConfigHelper().get_data_from_config('Mock Server', 'address')
    uri = '/testing/ies_backend/response/%s' % case_id
    r = requests.put(mock_server + uri, verify=False)
    if r.json() != 'OK':
        raise EnvironmentError


def check_quick_inv_result(criteria, criteria_type, no_match=False, agents=None, fet=False, no_rca=True):
    if isinstance(agents, str):
        agents = agents.split(',')

    quick_inv_task = TbQuickInvTask.find_by_criteria(criteria)
    quick_inv_mapping = TbInventoryQuickInvScanMapping.find_by_retroscandata_md5(quick_inv_task.RetroScanData_MD5)

    assert_equal(quick_inv_mapping.RetroScanData_MD5, quick_inv_task.RetroScanData_MD5,
                 "RetroScanData_MD5 should be the same")
    assert_equal(quick_inv_mapping.RetroScanCategory, quick_inv_task.RetroScanCategory,
                 "RetroScanCategory should be the same")
    assert_equal(quick_inv_task.CriteriaType, int(criteria_type), "CriteriaType should be the same")
    has_more = True if fet else False
    assert_equal(quick_inv_task.HasMore, has_more, "HasMore should be %s" % has_more)

    if no_match:
        assert_equal(TbQuickInvMatchObjectInfo.count(), 0, "if no quick inv result, match object should be empty")
    else:
        for index in range(0, len(agents)):
            check_quick_inv_match_obj_from_quick_inv_task(quick_inv_task, agents[index], no_rca)


def check_quick_inv_match_obj_from_quick_inv_task(quick_inv_task, agent, no_rca):
    match_agent = TbQuickInvMatchObjectInfo.find_by_slf_key_and_agent(quick_inv_task.SLF_Key, agent)
    assert_not_none(match_agent, "agent %s should exist" % agent)
    assert_equal(match_agent.RetroScanData_MD5, quick_inv_task.RetroScanData_MD5, "RetroScanData_MD5 should be the same")
    assert_equal(match_agent.RetroScanCategory, quick_inv_task.RetroScanCategory, "RetroScanCategory should be the same")
    if no_rca:
        assert_none(match_agent.RCAScanID, "RCAScanID should be NULL when RCA return no affected or yet to run RCA")


def check_init_rca_result(criteria, criteria_type, agents):
    agents = agents.split(',')
    for index in range(0, len(agents)):
        rca_agent = TbRCATask.find_by_criteria_and_agent(criteria, agents[index])
        assert_not_none(rca_agent, "RCA record for agent %s should exist" % agents[index])
        assert_equal(rca_agent.CriteriaType, int(criteria_type), "RCA criteriaType should be %s" % criteria_type)
        assert_none(rca_agent.TaskID, "RCA TaskID should not be NULL")
        assert_none(rca_agent.ScanSummaryID, "RCA ScanSummaryID should not be NULL")
        assert_equal(rca_agent.Status, 0, "RCA status should be 0 for init value")
        assert_equal(rca_agent.IsAffected, 0, "RCA IsAffected should be 0 for init value")
        assert_equal(rca_agent.IsSync, 0, "RCA IsSync should be 0 for init value")


def check_finished_rca_result(criteria, agent, status=4, affected=1, sync=1, skip_match_obj=False):
    rca_agent = TbRCATask.find_by_criteria_and_agent(criteria, agent)
    assert_not_none(rca_agent.TaskID, "TaskID should not be Null")
    assert_not_none(rca_agent.ScanSummaryID, "ScanSummaryID should not be Null")
    assert_equal(rca_agent.Status, int(status), "status should be %s" % status)
    assert_equal(rca_agent.IsAffected, int(affected), "IsAffected should be %s" % affected)
    assert_equal(rca_agent.IsSync, int(sync), "IsSync should be %s" % sync)
    if not skip_match_obj:
        check_quick_inv_match_obj_from_rca_task(rca_agent, agent)


def check_quick_inv_match_obj_from_rca_task(rca, agent):

    match_obj = TbQuickInvMatchObjectInfo.find_by_slf_key_and_agent(rca.SLF_Key, agent)
    if rca.IsAffected == 1:
        assert_equal(match_obj.RCAScanID, rca.ScanSummaryID,
                     "RCAScanID should be equal to ScanSummaryID for agent %s" % agent)
    else:
        assert_equal(match_obj.RCAScanID, None, "RCAScanID should be NULL when isaffected is 0")


def create_rca_test_data(match_agent, criteria, criteria_type, slf_key='0x4fa3ac39560cb7f8a1e794840'):
    # criteria_type : retroscan_type
    criteria_retroscan_mapping = {'1': '5', '2': '3', '5': '2'}
    match_agent = match_agent.split(',')

    for index in range(0, len(match_agent)):
        quick_inv_match = TbQuickInvMatchObjectInfoFactory(RetroScanCategory=criteria_retroscan_mapping[criteria_type],
                                                           agent=match_agent[index], SLF_Key=slf_key)
        TbRCATaskFactory(Criteria=criteria, CriteriaType=criteria_type, agent=match_agent[index],
                         SLF_Key=quick_inv_match.SLF_Key)


def check_task_should_be_timeout():
    quick_inv_task = TbQuickInvTask.all()
    for index in range(0, len(quick_inv_task)):
        assert_equal(True, quick_inv_task[index].IsTimeout, "quick inv task should be timeout")
        assert_equal(True, quick_inv_task[index].HasMore, "HasMore should be True for timeout task")

    rca_task = TbRCATask.all()
    for index in range(0, len(rca_task)):
        assert_equal(True, rca_task[index].IsTimeout, "rca task should be timeout")


def create_test_data_for_c5019997():
    TbQuickInvTaskFactory(day_offset='-3')
    TbQuickInvTaskFactory(day_offset='-3', init=False)
    TbRCATaskFactory(day_offset='-3')
    TbRCATaskFactory(day_offset='-3', init=False)


def create_test_data_for_c4918653():
    quick_inv = TbQuickInvTaskFactory(init=True, Criteria='factory.com.tw')
    TbInventoryQuickInvScanMappingFactory(RetroScanData_MD5=quick_inv.RetroScanData_MD5,
                                          RetroScanCategory=quick_inv.RetroScanCategory)

    quick_inv = TbQuickInvTaskFactory(init=False, Criteria='factory.com.nz')
    TbInventoryQuickInvScanMappingFactory(RetroScanData_MD5=quick_inv.RetroScanData_MD5,
                                          RetroScanCategory=quick_inv.RetroScanCategory)

    TbRCATaskFactory(init=True, Criteria='factory.com.tw')
    TbRCATaskFactory(init=False, Criteria='factory.com.nz')


def check_case_result_c4918672():
    criteria = ['CAED1FB5039A8F0CDDD6A23C4DDDBF7285531569', 'C3E4DDCA70ED53C3BB6678B4DDC398C474A65BDB',
                '443DDF9616EA43F8898FFCF7A5BA7E43CBDCA874']
    criteria_type = 5
    for index in range(0, len(criteria)):
        check_quick_inv_result(criteria[index], criteria_type, agents='Client24')
    assert_equal(3, TbQuickInvTask.get_distinct_taskid(), "distinct taskID should be 3")


def check_case_result_c4918594():
    argument = {'aa.bb.com': ['Client11', 'Client12', 'Client13', 'Client14', 'Client15'],
                '100.1.1.1': ['Client11', 'Client12', 'Client13', 'Client14', 'Client15']}
    for criteria, agents in argument.items():
        for index in range(0, len(agents)):
            check_finished_rca_result(criteria, agents[index], status=4, affected=False, sync=0)
        rcas = TbRCATask.find_by_criteria(criteria)
        task_scan_id = list(map(lambda x: (x.TaskID, x.ScanSummaryID), rcas))
        assert_equal(len(list(set(task_scan_id))), 1, "for one criteria, taskID and ScanSummaryID should be the same")


def check_case_result_c4918670():
    assert_equal(10000, TbQuickInvMatchObjectInfo.count(), "TbQuickInvMatchObjectInfo count should be 10000")
    assert_equal(10000, TbRCATask.count(), "TbRCATask count should be 10000")
