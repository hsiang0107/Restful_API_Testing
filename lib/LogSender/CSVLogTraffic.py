import os
import zipfile
from lib.LogSender import LogGenerator
from urllib.parse import urlencode
from lib.LogSender.TrafficBase import Traffic
from lib.LogSender.MCPStreamWrapper import *
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED


class CSVLogTraffic(Traffic):
    TMP_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Log_template_Src')
    Log = "Log"

    def __init__(self, server_guid, log_type, log_name, log_count, log_tmp_root=None):
        self.__log_type = log_type
        self.__log_name = log_name+'.tmp'
        self.__log_tmp_path = self.TMP_ROOT if log_tmp_root is None else log_tmp_root
        super(CSVLogTraffic, self).__init__(server_guid, 'Log', '1.2', log_count)

    def _funcCreateLogGenerator(self):
        log_template_path = os.path.join(self.__log_tmp_path, self.__log_type, self.__log_name)
        return LogGenerator.LogGenerator(log_template_path)


class CSVRegTraffic(Traffic):
    TMP_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'REG')
    REG_Register = 'Register'
    """
    enum ActionType
    {
        AC_COMMAND_QUERY = 1,
        AC_LOG,
        AC_LOGON,
        AC_LOGOFF,
        AC_UNREGISTER,
        AC_UPLOAD_PROFILE,
        AC_COMMAND_SEND,
        AC_COMMAND_NOTIFY,
        AC_VERIFY_CONNECTION,
        AC_COMMAND_FILE_UPLOAD,
        AC_CASCADING,
    };
    """

    def __init__(self, server_guid, product_type, product_tmp_root=None):
        self.__product_type = product_type
        self.__product_name = product_type+'.tmp'
        self.__product_profile_tmp = 'UploadProfile.tmp'
        self.__product_tmp_path = self.TMP_ROOT if product_tmp_root is None else product_tmp_root
        self._entity_type = 1
        super(CSVRegTraffic, self).__init__(server_guid, self.REG_Register, '1.2', 1)

    def _funcCreateLogGenerator(self):
        log_template_path = os.path.join(self.__product_tmp_path, self.__product_type, self.__product_name)
        return LogGenerator.LogGenerator(log_template_path)

    def funcGetHeader(self):
        return urlencode({'Action': '3', 'SLF_ProductGUID': self._strServerGuid, 'MsgVer': '5.0'}) + '\r\n'

    def funcGetProfileHeader(self):
        return urlencode({'Action': '6', 'SLF_ProductGUID': self._strServerGuid, 'MsgVer': '5.0'}) + '\r\n'

    def funcGetProfileBlobMessage(self, profile_version=None, profile_file=None):
        if profile_version is None:
            profile_name = 'ProductUI'
        else:
            profile_name = 'ProductUI_{0}' % profile_version
        profile_path = os.path.join(self.__product_tmp_path, self.__product_type, profile_name)
        profile_tmp = os.path.join(self.__product_tmp_path, self.__product_profile_tmp)
        profile_generator = LogGenerator.LogGenerator(profile_tmp)
        profile_generator.funcSetRedefinedTemplate('SLF_ProductGUID', self._strServerGuid)
        profile_zip = profile_path+'.zip'
        if profile_file is not None:
            if os.path.isfile(profile_file):
                profile_zip = profile_file
            else:
                profile_path = profile_file
                profile_zip = profile_path+'.zip'
        if not os.path.isfile(profile_zip):
            profile_zip_contents = os.listdir(profile_path)
            zip_file = zipfile.ZipFile(profile_zip, mode='w')
            try:
                for zip_content in profile_zip_contents:
                    content_path = os.path.join(profile_path, zip_content)
                    zip_file.write(content_path, arcname=zip_content, compress_type=compression)
            except:
                print('Zip Product Profile failed')
            finally:
                zip_file.close()
        with open(profile_zip, 'rb') as f:
            profile_generator.funcSetRedefinedTemplate('SLF_BlobData', f.read())
        return profile_generator.funcGetOneBlob()

    def getEntityType(self):
        return self._entity_type


class CSVRegDomainTraffic(CSVRegTraffic):

    def __init__(self, server_guid, product_type, parent_guid, product_tmp_root=None):
        super(CSVRegDomainTraffic, self).__init__(server_guid, product_type, product_tmp_root)
        self.funcSetPredefinedLogTemplate('SLF_ParentGUID', parent_guid)
        self.funcSetPredefinedLogTemplate('SLF_EntityType', 3)
        self.funcSetPredefinedLogTemplate('SLF_FolderPath', '')
        self._entity_type = 3


class CSVRegClientTraffic(CSVRegTraffic):

    def __init__(self, server_guid, product_type, parent_guid, product_tmp_root=None):
        super(CSVRegClientTraffic, self).__init__(server_guid, product_type, product_tmp_root)
        self.funcSetPredefinedLogTemplate('SLF_ParentGUID', parent_guid)
        self.funcSetPredefinedLogTemplate('SLF_EntityType', 2)
        self.funcSetPredefinedLogTemplate('SLF_FolderPath', '')
        self._entity_type = 2


class CSVUnRegTraffic(Traffic):
    TMP_ROOT = 'UNREG'
    UNREG_Register = 'UnRegister'

    def __init__(self, server_guid, product_tmp_root=None):
        self.__product_type = 'UnRegister'
        self.__product_name = 'UnRegister.tmp'
        self.__product_tmp_path = self.TMP_ROOT if product_tmp_root is None else product_tmp_root
        super(CSVUnRegTraffic, self).__init__(server_guid, self.UNREG_Register, '1.2', 1)

    def _funcCreateLogGenerator(self):
        log_template_path = os.path.join(self.__product_tmp_path, 'UnRegister.tmp')
        return LogGenerator.LogGenerator(log_template_path)

    def funcGetHeader(self):
        return urlencode({'Action': '5', 'SLF_ProductGUID': self._strServerGuid, 'MsgVer': '5.0'}) + '\r\n'


class CSVQueryTraffic(Traffic):
    TMP_ROOT = 'UNREG'
    QueryProduct = 'QueryProduct'

    def __init__(self, server_guid, product_tmp_root=None):
        self.__product_type = 'QueryProduct'
        self.__product_name = 'QueryProduct.tmp'
        self.__product_tmp_path = self.TMP_ROOT if product_tmp_root is None else product_tmp_root
        super(CSVQueryTraffic, self).__init__(server_guid, self.QueryProduct, '1.2', 1)

    def _funcCreateLogGenerator(self):
        return None

    def funcGetHeader(self):
        return urlencode({'Action': '1', 'SLF_ProductGUID': self._strServerGuid, 'MsgVer': '5.0'}) + '\r\n'

    def funcGetBlobMessage(self):
        return ''


if __name__ == '__main__':
    tmp = CSVRegTraffic('asdasdsadasdasdsadsa', 'SMEX', 'SMEX')
    print(tmp.funcGetProfileHeader())
    print(tmp.funcGetProfileBlobMessage())
