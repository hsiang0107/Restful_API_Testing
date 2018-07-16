import os
import re
import json
import urllib.parse
from robot.utils.asserts import assert_equal, assert_not_equal
from lib import DBHelper, http_helper, csv_handler
from db.factory_boy import TbExternalWebServiceConsumersFactory, TbIOCFileListFactory, TbIOCsSTIXFileListFactory,\
    TbIOCsYARAFileListFactory, TbBlacklistInfoFactory, TbBlacklistSourceInfoFactory, TbIOCsUDSOMapFactory
from lib.ConfigHelper import ConfigHelper
from db import TbExternalWebServiceConsumers, TbIOCFileList, TbIOCsSTIXFileList, TbIOCsYARAFileList, TbUserAccessLog,\
    TbBlacklistInfo, TbBlacklistSourceInfo, TbIOCsUDSOMap
from lib.extend_datetime import ExtendDateTime

test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              r'..\..\tests\testdata\external_api')


def external_api_suite_setup():
    initialize_api_key()


def external_api_suite_tear_down():
    clear_api_key()


def truncate_tables():
    DBHelper.clear_ioc_stix_yara_table()
    TbUserAccessLog.truncate()


def initialize_api_key(app_name=None, is_enabled=1, latency_second=120):
    config = ConfigHelper()
    app_id = config.get_data_from_config('CM', 'application_id')
    if not TbExternalWebServiceConsumers.check_if_key_is_duplicated(app_id):
        api_key = config.get_data_from_config('CM', 'api_key_crypted')
        if not app_name:
            app_name = config.get_data_from_config('CM', 'app_name')
        res = TbExternalWebServiceConsumersFactory(ApplicationID=app_id, APIKey=api_key, IsEnabled=is_enabled,
                                                   AllowedLatencyInSeconds=latency_second, ApplicationName=app_name)


def initialize_ioc_test_data():
    ioc_test_data = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 r'..\..\tests\external_api\initial_data\ioc.csv')
    test_data_list = csv_handler.parse_csv(ioc_test_data)
    dict_list = []
    for sub_list in test_data_list[1:]:
        tmp_dict = {}
        for key, data in zip(test_data_list[0], sub_list):
            tmp_dict.update({key: data})
        dict_list.append(tmp_dict)
    time_offset = -1
    for ioc in dict_list:
        TbIOCFileListFactory(FileHashID=ioc['FileHashID'], FileName=ioc['FileName'], ShortDesc=ioc['ShortDesc_Title'],
                             UploadedFrom=int(ioc['UploadedFrom']), UploadedBy=ioc['UploadedBy'],
                             ExtractingStatus=int(ioc['ExtractingStatus']),
                             UploadedTime=ExtendDateTime.get_date_by_offset(str(time_offset)))
        time_offset -= 1


def initialize_stix_test_data():
    stix_test_data = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 r'..\..\tests\external_api\initial_data\stix.csv')
    test_data_list = csv_handler.parse_csv(stix_test_data)
    dict_list = []
    for sub_list in test_data_list[1:]:
        tmp_dict = {}
        for key, data in zip(test_data_list[0], sub_list):
            tmp_dict.update({key: data})
        dict_list.append(tmp_dict)
    time_offset = -1
    for stix in dict_list:
        TbIOCsSTIXFileListFactory(FileHashID=stix['FileHashID'], FileName=stix['FileName'], Title=stix['ShortDesc_Title'],
                             UploadedFrom=int(stix['UploadedFrom']), UploadedBy=stix['UploadedBy'],
                             ExtractingStatus=int(stix['ExtractingStatus']),
                             UploadedTime=ExtendDateTime.get_date_by_offset(str(time_offset)))
        time_offset -= 1


def initialize_yara_test_data():
    yara_test_data = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  r'..\..\tests\external_api\initial_data\yara.csv')
    test_data_list = csv_handler.parse_csv(yara_test_data)
    dict_list = []
    for sub_list in test_data_list[1:]:
        tmp_dict = {}
        for key, data in zip(test_data_list[0], sub_list):
            tmp_dict.update({key: data})
        dict_list.append(tmp_dict)
    time_offset = -1
    for yara in dict_list:
        TbIOCsYARAFileListFactory(FileHashID=yara['FileHashID'], FileName=yara['FileName'],
                                  UploadedFrom=int(yara['UploadedFrom']), UploadedBy=yara['UploadedBy'],
                                  UploadedTime=ExtendDateTime.get_date_by_offset(str(time_offset)))
        time_offset -= 1


def clear_api_key():
    DBHelper.clear_tb_ExternalWebServiceConsumers()


def parse_test_data_json(test_case_name, file_name):
    test_case_id = test_case_name[test_case_name.find('(') + 1:test_case_name.find(')')]
    request_path = os.path.join(test_data_path, test_case_id, file_name)
    body = ''
    if os.path.isfile(request_path):
        with open(request_path, 'r') as f:
            body = json.load(f)
    return body


# interface:
#   1: internal
#   2: external
def send_api_request(test_case_name, api, interface=2, request_data='request.json', credential=None):
    config = ConfigHelper()
    body = {}
    params = {}
    if api['method'] == 'GET' or api['method'] == 'DELETE':
        params = parse_test_data_json(test_case_name, request_data)
    else:
        body = parse_test_data_json(test_case_name, request_data)
    query_url = api['path']
    if params:
        query_url += '?' + urllib.parse.urlencode(params)
    token = None
    if int(interface) == 2:
        token = http_helper.get_jwt(api['method'], query_url, '', json.dumps(body) if body else '')
    return http_helper.send_request(
        config.get_data_from_config('CM', 'protocol') +
        config.get_data_from_config('CM', 'ip') + ':' +
        str(config.get_data_from_config('CM', 'port')),
        api, interface, credential, params=params if params else None, body=json.dumps(body) if body else None,
        jwt_token=token)


def return_code_should_be(response, expected):
    if response.status_code != int(expected):
        raise AssertionError('Return code should be %d, instead of %d.' % (int(expected), response.status_code))


def response_body_should_be(test_case_name, response, expected_data='response.json'):
    expected = parse_test_data_json(test_case_name, expected_data)
    current = response.json()
    if 'Data' in current:
        current = current['Data']
    if expected != current:
        raise AssertionError('Response is not matched to expected.')


def full_response_body_should_be(test_case_name, response):
    expected = parse_test_data_json(test_case_name, 'response.json')
    if expected != response.json():
        raise AssertionError('Response is not matched with expected.')


def verify_response_by_key(test_case_name, response, *keys):
    expected = parse_test_data_json(test_case_name, 'response.json')
    response = response.json()
    for key in keys:
        if expected[key] != response[key]:
            raise AssertionError(key, ' is not matched with expected')


def verify_response_data_without_datetime(test_case_name, response, filetype, expected_data='response.json'):
    expected = parse_test_data_json(test_case_name, expected_data)
    expected = expected['Data']
    response = response.json()['Data']
    if expected['TotalIOCCount'] != response['TotalIOCCount']:
        raise AssertionError('TotalIOCCount does not match expected')
    for exp_dic, res_dic in zip(expected.get('FilingCabinet'), response.get('FilingCabinet')):
        if 'FileAddedDatetime' not in res_dic.keys():
            raise AssertionError('FileAddedDatetime does not exist')
        if exp_dic['FileHashID'] != res_dic['FileHashID']:
            raise AssertionError('FileHashID does not match expected')
        if exp_dic['FileName'] != res_dic['FileName']:
            raise AssertionError('FileName does not match expected')
        if exp_dic['UploadedFrom'] != res_dic['UploadedFrom']:
            raise AssertionError('UploadedFrom does not match expected')
        if exp_dic['UploadedBy'] != res_dic['UploadedBy']:
            raise AssertionError('UploadedBy does not match expected')
        if filetype != 'yara':
            if exp_dic['ExtractingStatus'] != res_dic['ExtractingStatus']:
                raise AssertionError('ExtractingStatus does not match expected')
        if filetype == 'ioc':
            if exp_dic['ShortDesc'] != res_dic['ShortDesc']:
                raise AssertionError('ShortDesc does not match expected')
        if filetype == 'stix':
            if exp_dic['Title'] != res_dic['Title']:
                raise AssertionError('Title does not match expected')


def create_openioc_data(file_name, file_hash_id):
    TbIOCFileListFactory(FileName=file_name, FileHashID=file_hash_id)


def create_stix_data(file_name, file_hash_id):
    TbIOCsSTIXFileListFactory(FileName=file_name, FileHashID=file_hash_id)


def create_yara_data(file_name, file_hash_id):
    TbIOCsYARAFileListFactory(FileName=file_name, FileHashID=file_hash_id)


def create_blacklistinfo_data(slf_key):
    TbBlacklistInfoFactory(SLF_Key=slf_key)


def create_blacklistsourceinfo_data(slf_key, file_hash_id):
    TbBlacklistSourceInfoFactory(SLF_Key=slf_key, FileHashID=file_hash_id)


# file_type
#   1: ioc, 2: stix
# source
#   1: api, 2: web, 3: stix, 4: ioc, 5: hub, 6: node
def create_ioc_udsomap_data(file_hash_id, slf_key, udso_id, file_type='1'):
    if file_type == '1':
        source = 4
        t = TbIOCFileListFactory
    elif file_type == '2':
        source = 3
        t = TbIOCsSTIXFileListFactory
    else:
        raise AssertionError('file_type = %s is not valid' % file_type)
    TbBlacklistInfoFactory(SLF_Key=slf_key, EntityID=udso_id, UserDefinedTime='06/13/2018 00:00:00')
    TbBlacklistSourceInfoFactory(SLF_Key=slf_key, FileHashID=file_hash_id, FileName=slf_key, Source=source)
    t(FileName=slf_key, FileHashID=file_hash_id)
    TbIOCsUDSOMapFactory(FileHashID=file_hash_id, UDSOID=slf_key, FileType=int(file_type))


def ioc_membership_validation(res, expected):
    config = ConfigHelper()
    from db.models.tb_IOCFileList import TbIOCFileList
    hashid = res.json()['Data']['UploadedResultInfoList'][0]['FileHashID']
    if expected['UploadedFrom'] == 1:
        uploadedby = config.get_data_from_config('CM', 'app_name')
    if expected['UploadedFrom'] == 2:
        uploadedby = config.get_data_from_config('CM', 'admin', 'account')
    record = TbIOCFileList.find_by_file_hash_id(hashid)
    if record.UploadedFrom != expected['UploadedFrom']:
        raise AssertionError('UploadedFrom value is not correct')
    if record.UploadedBy != uploadedby:
        raise AssertionError('UploadedBy value is not correct')


def table_count_should_be(table_type, expected):
    def verify_count(table, expected):
        if table.count() != expected:
            raise AssertionError(
                'Data count of %s should be %d, instead of %d.' %
                (table.__tablename__, expected, table.count())
            )
    t = {
        'ioc': TbIOCFileList,
        'stix': TbIOCsSTIXFileList,
        'yara': TbIOCsYARAFileList,
        'blacklist': [TbBlacklistInfo, TbBlacklistSourceInfo]
    }.get(table_type)
    expected = int(expected)
    if t:
        if type(t) is list:
            for i in t:
                verify_count(i, expected)
        else:
            verify_count(t, expected)
    else:
        raise AssertionError('Table type is not correct: %s' % table_type)


def audit_should_be(event_type_id, expected_count, expected_description, expected_result=1):
    config = ConfigHelper()
    records = TbUserAccessLog.find_records_by_event_type(event_type_id)
    assert_equal(len(records), int(expected_count))
    for r in records:
        assert_equal(r.UserID, config.get_data_from_config('CM', 'app_name'))
        assert_equal(r.Result, int(expected_result))
        assert_not_equal(re.match(expected_description, r.Description), None)


def uploaded_data_should_be(request, type):
    {
        'ioc': lambda: uploaded_ioc_tables_should_be(request, TbIOCFileList),
        'stix': lambda: uploaded_ioc_tables_should_be(request, TbIOCsSTIXFileList),
        'yara': lambda: uploaded_ioc_tables_should_be(request, TbIOCsYARAFileList),
    }.get(type)()


def uploaded_ioc_tables_should_be(request, table):
    config = ConfigHelper()
    data = request.json()['Data']
    for i in data['UploadedResultInfoList']:
        if i['UploadedStatus'] != 1:
            continue
        record = table.find_by_file_hash_id(i['FileHashID'])
        assert_equal(record.FileName, i['FileName'])
        assert_equal(record.UploadedFrom, 1)
        assert_equal(record.UploadedBy, config.get_data_from_config('CM', 'app_name'))


def uploaded_so_tables_should_be(test_case_name, expected_data='request.json'):
    config = ConfigHelper()
    scan_action = {'LOG': 1, 'BLOCK': 2, 'QUARANTINE': 3}
    expected = parse_test_data_json(test_case_name, expected_data)
    record = TbBlacklistInfo.find_by_note(expected.get('note'))
    assert_equal(record.SLF_Type, 2)
    assert_equal(record.SourceType, 1)
    assert_equal(record.ScanAction, scan_action.get(expected.get('file_scan_action')))
    source_record = TbBlacklistSourceInfo.find_by_key(record.SLF_Key)
    assert_equal(source_record.Source, 1)
    assert_equal(source_record.UploadedBy, config.get_data_from_config('CM', 'app_name'))


def read_test_data_base64(test_case_name, file_name):
    test_case_id = test_case_name[test_case_name.find('(') + 1:test_case_name.find(')')]
    request_path = os.path.join(test_data_path, test_case_id, file_name)
    base64 = ''
    if os.path.isfile(request_path):
        with open(request_path, 'r') as f:
            base64 = f.readline()
    return base64


def create_openioc_data_with_base64(test_case_name, file_hash_id):
    base64 = read_test_data_base64(test_case_name, 'base64')
    TbIOCFileListFactory(FileName=test_case_name, FileHashID=file_hash_id, FileContent_BASE64=base64)


def create_stix_data_with_base64(test_case_name, file_hash_id):
    base64 = read_test_data_base64(test_case_name, 'base64')
    TbIOCsSTIXFileListFactory(FileName=test_case_name, FileHashID=file_hash_id, FileContent_BASE64=base64)


def create_specified_stix_data_with_base64(test_case_name, file_hash_id, teat_data_name):
    base64 = read_test_data_base64(test_case_name, teat_data_name)
    TbIOCsSTIXFileListFactory(FileName=test_case_name+teat_data_name, FileHashID=file_hash_id, FileContent_BASE64=base64)


def extract_blacklist_table_should_be(test_case_name):
    expected = parse_test_data_json(test_case_name, 'expected_tbblacklistinfo.json')
    if TbBlacklistInfo.get_count() != len(expected):
        raise AssertionError('SO count in DB('+str(TbBlacklistInfo.get_count())+') does not match expected count('+str(len(expected))+')')
    for i in expected:
        record = TbBlacklistInfo.find_by_slf_data(i['SLF_Data'])
        if record is None:
            raise AssertionError('Missing SO('+i['SLF_Data']+')')
        assert_equal(record.ScanAction, i['ScanAction'])
        assert_equal(record.SLF_Type, i['SLF_Type'])

