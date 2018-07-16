import factory
import datetime
from db.factory_boy.cm_factory import CMFactory
from db import TbWebSecurityLog, TbEntityInfo


class TbWebSecurityLogFactory(CMFactory):
    class Meta:
        model = TbWebSecurityLog
        sqlalchemy_session_persistence = 'commit'

    CLF_MsgLogType = 1733
    CLF_LogVersion = 1
    CLF_LogMinorVersion = 1
    CLF_ComputerName = "Client01"
    CLF_ProductVersion = None
    CLF_ProductPlatformCode = None
    CLF_ProductLanguageCode = None
    CLF_ServerityCode = None
    CLF_ComponentCode = None
    CLF_LogReplicatedFlag = None
    CLF_LogGenerationTime = ""
    CLF_LogGenerationTimeZone = 0
    CLF_LogReceivedTime = datetime.datetime.now()
    CLF_LogReceivedTimeZone = 0
    CLF_IsDayLightSaving = 0
    CLF_ReasonCode = None
    CLF_ReasonCodeSource = None
    CLF_ReasonCodeSymbol = None
    CLF_ReasonCodeDescription = None
    CLF_RedAlertID = None
    SLF_ClientHostName = "Fake Host Name"
    SLF_FileName = "Fake File Name"
    SLF_BlockingType = 31
    SLF_BlockingRule = None
    SLF_Direction = 2
    SLF_Protocol = 5
    SLF_ServerIP = "10.1.1.1"
    SLF_ServerPort = "80"
    SLF_LoginUser = "Fake User"
    SLF_UserAgentType = 0
    SLF_DetectionType = 10
    SLF_SeverityLevel = 100
    SLF_CredibilityLevel = 1
    SLF_RatingThreshold = 80
    SLF_ReputationScore = 21
    SLF_PolicyName = "Internal Fake Policy"
    SLF_Action = 1
    SLF_Reason = None
    AggregatedUTCDatetime = None
    AggregatedLocalDatetime = None
    AggregatedCount = 1
    UserGroupName = None
    SLF_Is_CCCA_Detection = 1
    SLF_CCCA_DetectionSource = 1
    SLF_CCCA_RiskLevel = 1
    SLF_ProcessName = "Fake Process"
    SLF_UserMail = None
    CE_FilterID = "F"

    class Params:
        blacklist = None

    @factory.lazy_attribute_sequence
    def MsgLogID(self, n):
        return "503C31155B94-4E8B9FF2-WEBS-79A5-{:A>4}".format(n)

    @factory.lazy_attribute_sequence
    def SLF_URLCorrelationKey(self, n):
        if self.blacklist and self.blacklist.SLF_Type is '1':
            return '96aeff92ffd18acbbf0a1f0c43e9{:0>4}'.format(str(n))
        else:
            return None

    @factory.lazy_attribute
    def CLF_EntityID(self):
        return TbEntityInfo.find_by_machine_name(self.CLF_ComputerName).EI_EntityID

    @factory.lazy_attribute
    def CLF_ProductType(self):
        return TbEntityInfo.find_by_machine_name(self.CLF_ComputerName).EI_ProductType

    @factory.lazy_attribute
    def SLF_ClientIP(self):
        return TbEntityInfo.find_by_machine_name(self.CLF_ComputerName).EI_IPAddressList

    @factory.lazy_attribute
    def CLF_ManagerID(self):
        return TbEntityInfo.find_by_machine_name(self.CLF_ComputerName).EI_ManagerID

    @factory.lazy_attribute
    def SLF_ClientGuid(self):
        return self.CLF_EntityID

    @factory.lazy_attribute
    def SLF_ObjectNameURL(self):
        if self.blacklist and self.blacklist.SLF_Type is '1':
            return self.blacklist.SLF_Data

    @factory.lazy_attribute
    def SLF_CCCA_Destination(self):
        if self.blacklist and self.blacklist.SLF_Type is '1':
            return self.SLF_ObjectNameURL
        else:
            return self.blacklist.SLF_Data

    @factory.lazy_attribute
    def CLF_LogReceivedUTCTime(self):
        return self.CLF_LogReceivedTime

    @factory.lazy_attribute
    def SLF_CCCA_DestinationFormat(self):
        # {SLF_Type : destination_format}
        destination_format = {'0': '0', '1': '2', '2': None, '3': '4'}
        return destination_format[self.blacklist.SLF_Type]
