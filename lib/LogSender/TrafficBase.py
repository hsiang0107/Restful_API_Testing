import os
import threading
from urllib.parse import urlencode
import lib.LogSender.LogGenerator as LogGenerator


class Traffic(object):
    REG_Register = "Register"
    Log_Status = "Status"
    Log_Status_Partial = "Status_Partial"
    Log_Virus = "Virus"
    Log_Spyware = "Spyware"
    Log_Security = "Security"
    Log_WebSecurity = "WebSecurity"
    Log_DLP = "DLP"
    Log_CAV = "CAV"
    Log_TDATMufe = "TDATmufe"
    Log_BM = "BM"
    Log_DAE = "DAE"
    Log_COR = "COR"
    Log_CVW = "CVW"
    Log_URL = "URL"
    Log_PerfM = "PerfM"
    Log_PCK = "PCK"
    Log_VAS = "VAS"
    Log_ESV = "ESV"
    Log_ESC = "ESC"
    Log_ESVS = "ESVS"
    Log_NRS = "NRS"
    Log_WebS = "WebS"
    Log_PFW = "PFW"
    Log_MRS = "MRS"
    Log_NCIE = "NCIE"
    Log_Susobj = "SuspiciousObject"
    Log_VAF = "VAFeedback"
    Log_INT = "Intrusion"
    Log_BigTable = "BIGTABLE"   # A specialString indicate 3 Big Table
    Log_DD = "DD"

    HTTP = "http"
    HTTPS = "https"

    def __init__(self, str_server_guid, str_traffic_type, str_version, str_amount, str_method=HTTP):
        self._strServerGuid = str_server_guid
        self._strTrafficType = str_traffic_type
        self._strVersion = str_version
        self._intAmount = int(str_amount)
        self._strMethod = str_method
        self._intTotalAmount = 0
        self.__strTemplateRoot = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Template")
        self.__objLogGenerator = self._funcCreateLogGenerator()
        self.__strHeader = self.__funcCreateHeader()
        self.__StatisticLock = threading.Lock()

    def _funcCreateLogGenerator(self):
        """
        Create Log Generator according to the Traffic Type
        """

        # Define the Template Path
        dict_template_folder_map = {self.REG_Register: "REG",
                                    self.Log_Status: "Status",
                                    self.Log_Status_Partial: "Status_Partial",
                                    self.Log_Virus: "Virus",
                                    self.Log_Spyware: "Spyware",
                                    self.Log_Security: "Security",
                                    self.Log_WebSecurity: "WebSec",
                                    self.Log_DLP: "DLP",
                                    self.Log_CAV: "CAV",
                                    self.Log_BM: "BM",
                                    self.Log_TDATMufe: "TDA",
                                    self.Log_DAE: "DAE",
                                    self.Log_COR: "COR",
                                    self.Log_CVW: "CVW",
                                    self.Log_URL: "URL",
                                    self.Log_PerfM: "PerfM",
                                    self.Log_PCK: "PCK",
                                    self.Log_VAS: "VAS",
                                    self.Log_ESV: "ESV",
                                    self.Log_ESC: "ESC",
                                    self.Log_ESVS: "ESVS",
                                    self.Log_NRS: "NRS",
                                    self.Log_WebS: "WebS",
                                    self.Log_PFW: "PFW",
                                    self.Log_MRS: "MRS",
                                    self.Log_NCIE: "NCIE",
                                    self.Log_VAF: "VAF",
                                    self.Log_INT: "Int",
                                    self.Log_Susobj: "SusObj",
                                    self.Log_DD: "DD"}

        str_template_folder = os.path.join(self.__strTemplateRoot, dict_template_folder_map[self._strTrafficType])
        str_template_path = os.path.join(str_template_folder, os.listdir(str_template_folder)[-1])

        return LogGenerator.LogGenerator(str_template_path)

    def __funcCreateHeader(self):
        str_action = "0"
        for strKey, strValue in list(self.__class__.__dict__.items()):
            if strValue == self._strTrafficType:
                if strKey.startswith("REG"):
                    str_action = 3
                elif strKey.startswith("Log"):
                    str_action = 2
                elif strKey.startswith("UNREG"):
                    str_action = 5

        str_header = urlencode({'Action': str_action,
                                'SLF_ProductGUID': self._strServerGuid,
                                'MsgVer': '5.0'})
        return str_header + '\r\n'

    def funcGetBlobMessage(self, network_order=True):
        """
        @Return: [One String] Based on required amount, all generated MCP Blobs in one String
        """
        list_pack_blob = []
        with self.__StatisticLock:
            for i in range(self._intAmount):
                list_pack_blob.append(self.__objLogGenerator.funcGetOneBlob(network_order))

            self._intTotalAmount += len(list_pack_blob)

        return b"".join(list_pack_blob)

    def funcGetBlobList(self, max_blob_count=4000):
        """
        @Return: [One String] Based on required amount, all generated MCP Blobs in one String
        """
        list_pack_blob = []
        with self.__StatisticLock:
            n = min(self._intAmount, max_blob_count)
            left_count = self._intAmount
            tmp_pack_blob = list()
            repeatable_blob = None
            while left_count > 0:
                n = min(n, left_count)
                for i in range(n):
                    if self.__objLogGenerator.funcIsRepeatable():
                        if repeatable_blob is None:
                            repeatable_blob = self.__objLogGenerator.funcGetOneBlob()
                        tmp_blob_obj = repeatable_blob
                    else:
                        tmp_blob_obj = self.__objLogGenerator.funcGetOneBlob()

                    tmp_pack_blob.append(tmp_blob_obj)

                self._intTotalAmount += len(tmp_pack_blob)
                list_pack_blob.append(tmp_pack_blob)
                tmp_pack_blob = list()
                left_count -= n

        return list_pack_blob

    def funcRollbackAmount(self):
        """
        Used to Rollback the Send Log Amount due to something error.
        """
        with self.__StatisticLock:
            self._intTotalAmount -= self._intAmount

    def funcGetHeader(self):
        return self.__strHeader

    def funcSetAmount(self, int_amount):

        if isinstance(int_amount, int):
            self._intAmount = int_amount

    def funcSetPredefinedLogTemplate(self, str_field_name, obj_content):
        """
        Pass the predefined value into Log Generator
        """
        self.__objLogGenerator.funcSetRedefinedTemplate(str_field_name, obj_content)

    def funcGetTemplateValue(self, str_field_name):
        """
        Pass the predefined value into Log Generator
        """
        return self.__objLogGenerator.funcGetTemplateValue(str_field_name)

    def funcGetTotalAmount(self):
        return self._intTotalAmount

    def funcGetTrafficType(self):
        return self._strTrafficType

    def funcGetUid(self):
        return self._strServerGuid


if __name__ == "__main__":
    objTraffic_A = Traffic("800000000000-00000000-0000-0000-0001", Traffic.REG_Register, "1.2", 1)
    print(objTraffic_A.funcGetBlobMessage())
