from db.models.tb_IOCFileList import TbIOCFileList
from lib import http_helper
from lib.ConfigHelper import ConfigHelper
from resources.backend_objects import external_api
from db.factory_boy.tb_IOCFileList_factory import TbIOCFileListFactory
from resources.backend_objects import external_api
from resources.backend_objects import external_api_variables


external_api.truncate_tables()
external_api.initialize_ioc_test_data()
# external_api.initialize_stix_test_data()
# external_api.initialize_yara_test_data()
# config = ConfigHelper()
#
api = external_api_variables.API_INFO['GetReportingLineMap']
# res = external_api.send_external_api_request('(C5752128)Internal call with no InvokePermission set', api)
res = external_api.send_internal_api_request('(C5752128)Internal call with no InvokePermission set', api)
print(res.json())
external_api.validate_response_by_key('(C5752128)Internal call with no InvokePermission set', res, 'Data', 'Meta', 'PermissionCtrl', 'FeatureCtrl')
# external_api.verify_query_data('(C5734168)Limit the number of query data by parameter PageSize', res)
# body = external_api.parse_test_data_json('(C5721603)External invoke API - InvokePermission Both', 'request.json')

# server = config.get_data_from_config('CM', 'protocol') + config.get_data_from_config('CM', 'ip')
# res = http_helper.internally_request_api(server, api)
# print(res.json())
# res = TbIOCFileListFactory()
# # external_api.external_api_suite_setup()



# api = {
#     'method': 'POST',
#     'path': '/WebApp/IOCBackend/OpenIOCResource/File'
#     }



# config = ConfigHelper()
# body = external_api.parse_test_data_json('(C5721603)External invoke API - InvokePermission Both', 'request.json')
# token = http_helper.get_jwt(api['method'], api['path'], '', body)
# res = http_helper.send_jwt_request(token, config.get_data_from_config('CM', 'protocol') + config.get_data_from_config('CM', 'ip'),
#                                    api, body if body else None)
# hashid = res.json()['Data']['UploadedResultInfoList'][0]['FileHashID']
# print(res.json())


# ioc = TbIOCFileList.find_by_hashid('fcce66ad8b3a6242b2f35f6bc103683aaf5f3f48')
# print(ioc.UploadedFrom, ioc.UploadedBy)

