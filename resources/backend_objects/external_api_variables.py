API_INFO = {
    'upload_openioc': {
        'method': 'POST',
        'path': '/WebApp/IOCBackend/OpenIOCResource/File',
    },
    'download_openioc': {
        'method': 'GET',
        'path': '/WebApp/IOCBackend/OpenIOCResource/File',
    },
    'delete_openioc': {
        'method': 'DELETE',
        'path': '/WebApp/IOCBackend/OpenIOCResource/File',
    },
    'query_openioc_extracted_info': {
        'method': 'GET',
        'path': '/WebApp/IOCBackend/OpenIOCResource/ExtractingInfo',
    },
    'query_openioc': {
        'method': 'GET',
        'path': '/WebApp/IOCBackend/OpenIOCResource/FilingCabinet',
    },
    'upload_stix': {
        'method': 'POST',
        'path': '/WebApp/IOCBackend/STIXResource/File',
    },
    'download_stix': {
        'method': 'GET',
        'path': '/WebApp/IOCBackend/STIXResource/File',
    },
    'delete_stix': {
        'method': 'DELETE',
        'path': '/WebApp/IOCBackend/STIXResource/File',
    },
    'query_stix_extracted_info': {
        'method': 'GET',
        'path': '/WebApp/IOCBackend/STIXResource/ExtractingInfo',
    },
    'query_stix': {
        'method': 'GET',
        'path': '/WebApp/IOCBackend/STIXResource/FilingCabinet',
    },
    'extract_openioc': {
        'method': 'PUT',
        'path': '/WebApp/SuspiciousObjectsBackend/UserDefinedSOResource/OpenIOCExtraction',
    },
    'extract_stix': {
        'method': 'PUT',
        'path': '/WebApp/SuspiciousObjectsBackend/UserDefinedSOResource/STIXExtraction',
    },
    'upload_yara': {
        'method': 'POST',
        'path': '/WebApp/IOCBackend/YARAResource/File',
    },
    'download_yara': {
        'method': 'GET',
        'path': '/WebApp/IOCBackend/YARAResource/File',
    },
    'delete_yara': {
        'method': 'DELETE',
        'path': '/WebApp/IOCBackend/YARAResource/File',
    },
    'query_yara': {
        'method': 'GET',
        'path': '/WebApp/IOCBackend/YARAResource/FilingCabinet',
    },
    'GetReportingLineMap': {
        'method': 'GET',
        'path': '/webapp/ExeDashboardBackend/ExeDashboardResource/GetReportingLineMap',
    },
    'getdetections': {
        'method': 'GET',
        'path': '/webapp/ExeDashboardBackend/ExeDashboardResource/getdetections',
    },
    'upload_file_udso_from_external': {
        'method': 'PUT',
        'path': '/WebApp/API/SuspiciousObjectResource/FileUDSO',
    },
    'query_udso_from_extration': {
        'method': 'POST',
        'path': '/WebApp/SuspiciousObjectsBackend/UserDefinedSOResource/ListByScope',
    },
    'mdr': {
        'method': 'GET',
        'path': '/WebApp/MDRBackend/MDRResource/PendingTaskList?Page=1&PageSize=1',
    },
    'query_server': {
        'method': 'GET',
        'path': '/WebApp/XWS/V1/ServerResource/ProductServers',
    },
    'query_agent': {
        'method': 'GET',
        'path': '/WebApp/XWS/V1/AgentResource/ProductAgents',
    },
}
Membership = {
    'API': {
        'UploadedFrom': 1
    },
    'Manual': {
        'UploadedFrom': 2
    }
}
