import factory
from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import *


class TbFileHashDetectionLogFactory(CMFactory):
    class Meta:
        model = TbFileHashDetectionLog
        sqlalchemy_session_persistence = 'commit'

    CMGuid = TbSystemInfo.get_CM_guid()
    SLF_LogType = 1766
    SLF_ProductGUID = None
    SLF_ProductID = None
    SLF_LogVersion = 1
    SLF_LogMinorVersion = 0
    SLF_ComputerName = 'OSCE01'
    SLF_ProductVersion = 13
    SLF_LogGenerationTime = ExtendDateTime.current_time()
    SLF_LogGenerationTimeZone = 8
    SLF_IsDayLightSaving = 0
    SLF_Sender = None
    SLF_Recipient = None
    SLF_Subject = None
    SLF_EntryChannel = None
    SLF_ClientGUID = None
    SLF_ClientIP = None
    SLF_HostName = None
    SLF_TrueFileType = "EXE"
    SLF_FileSHA1 = None
    SLF_FileSource = "Factory.exe"
    SLF_SourceType = 0
    SLF_Action = 1
    SLF_ActionResult = 1
    SLF_ScanType = 2
    SLF_LogReceivedUTCTime = ExtendDateTime.current_time()
    SLF_FileCreatedUTCTime = ExtendDateTime.current_time()
    SLF_FileModifiedUTCTime = ExtendDateTime.current_time()
    CE_FilterID = None
    CLF_LogGenCMLocalTime = ExtendDateTime.current_time()

    class Params:
        affected_client = None
        day_offset = '+0'

    @factory.lazy_attribute_sequence
    def MsgLogID(self, n):
        return "503C31155B94-4E8B9FF2-FILE-HASH-{:A>4}".format(n)

    @factory.lazy_attribute
    def SLF_ProductGUID(self):
        return TbEntityInfo.find_by_machine_name(self.affected_client).EI_AgentID

    @factory.lazy_attribute
    def SLF_ProductID(self):
        return TbEntityInfo.find_by_machine_name(self.affected_client).EI_ProductType

    @factory.lazy_attribute
    def SLF_ProductVersion(self):
        return TbEntityInfo.find_by_machine_name(self.affected_client).EI_ProductVersion

    @factory.lazy_attribute
    def SLF_ClientGUID(self):
        return TbEntityInfo.find_by_machine_name(self.affected_client).EI_EntityID

    @factory.lazy_attribute
    def SLF_ClientIP(self):
        return TbEntityInfo.find_by_machine_name(self.affected_client).EI_IPAddressList

    @factory.lazy_attribute
    def SLF_HostName(self):
        return self.affected_client

    @factory.lazy_attribute
    def SLF_LogGenerationTime(self):
        return ExtendDateTime.get_date_by_offset(self.day_offset)

    @factory.lazy_attribute
    def CLF_LogGenCMLocalTime(self):
        return ExtendDateTime.get_date_by_offset(self.day_offset)
