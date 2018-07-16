import factory
from lib.extend_datetime import ExtendDateTime
from datetime import datetime, timedelta
from db.factory_boy.cm_factory import CMFactory
from db import TbNetworkContentInspectionEngineLog, TbSystemInfo, TbEntityInfo


class TbNetworkContentInspectionEngineLogFactory(CMFactory):
    class Meta:
        model = TbNetworkContentInspectionEngineLog
        sqlalchemy_session_persistence = 'commit'

    CMGuid = TbSystemInfo.get_CM_guid()
    SLF_MsgType = 1756
    SLF_LogVersion = 1
    SLF_LogMinorVersion = 0
    SLF_LogGenLocalDatetime = ExtendDateTime.current_time()
    SLF_TimeZoneInMins = -480
    SLF_DaylightSavingInMins = 0
    LogReceivedTime = ExtendDateTime.current_time()
    LogReceivedTimeZone = -480
    SLF_ComputerName = None
    SLF_ProcessName = "Factory.exe"
    SLF_SourceIP = '10.1.1.1'
    SLF_SourcePort = 80
    SLF_DestinationIP = None
    SLF_DestinationPort = 80
    SLF_Action = 1
    SLF_Direction = 1
    SLF_PatternType = 1
    SLF_Is_CCCA_Detection = 1
    SLF_CCCA_DetectionSource = 1
    SLF_CCCA_RiskLevel = 1
    NCIE_ThreatName = None
    CE_FilterID = 'F'
    SLF_DestinationDomain = None

    @factory.lazy_attribute_sequence
    def MsgLogID(self, n):
        return "503C31155B94-4E8B9FF2-NCIE-79A5-{:B>4}".format(n)

    @factory.lazy_attribute
    def LogReceivedUTCTime(self):
        return ExtendDateTime.get_date_by_offset(timedelta(minutes=int(self.LogReceivedTimeZone)),
                                                 self.LogReceivedTime)

    @factory.lazy_attribute
    def SLF_LogGenUTCDatetime(self):
        return ExtendDateTime.get_date_by_offset(timedelta(minutes=int(self.SLF_TimeZoneInMins)),
                                                 self.SLF_LogGenLocalDatetime)

    @factory.lazy_attribute
    def SLF_ProductGUID(self):
        return TbEntityInfo.find_by_machine_name(self.SLF_ComputerName).EI_AgentID

    @factory.lazy_attribute
    def SLF_ClientGUID(self):
        return TbEntityInfo.find_by_machine_name(self.SLF_ComputerName).EI_EntityID

    @factory.lazy_attribute
    def SLF_ProductID(self):
        return TbEntityInfo.find_by_machine_name(self.SLF_ComputerName).EI_ProductType
