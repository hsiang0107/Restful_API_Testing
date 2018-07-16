import factory
from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import TbAVVirusLog, TbEntityInfo


class TbAvviruslogFactory(CMFactory):
    class Meta:
        model = TbAVVirusLog
        sqlalchemy_session_persistence = 'commit'

    CLF_MsgLogType = 1703
    CLF_LogMinorVersion = 1
    CLF_EntityID = '111111111111-AAAAAAAA-1111-0000-0001'
    CLF_ManagerID = '000C2934ADB2-5AEBD810-05D5-C191-5B5E'
    CLF_LogVersion = 1
    CLF_ProductType = '15'
    CLF_ProductVersion = '13.5'
    CLF_ProductLanguageCode = 0
    CLF_LogGenerationTime = ExtendDateTime.get_date_by_offset('-1')
    CLF_LogGenerationTimeZone = 0
    CLF_LogReceivedTime = ExtendDateTime.current_time()
    CLF_LogReceivedUTCTime = ExtendDateTime.current_time()
    CLF_LogReceivedTimeZone = 0
    CLF_ServerityCode = 2
    CLF_ComponentCode = 9
    CLF_LogReplicatedFlag = None
    CLF_ComputerName = 'Client11'
    CLF_ProductPlatformCode = 4
    CLF_IsDayLightSaving = 0
    CLF_ReasonCode = 'virus log'
    CLF_ReasonCodeSource = 20
    VLF_VirusLogType = 1
    VLF_VirusName = 'Factory_make_virus'
    VLF_IsMoreThanOneVirus = 0
    VLF_FunctionCode = 11
    VLF_FirstAction = 2
    VLF_SecondAction = 4
    VLF_FirstActionResult = 32
    VLF_SecondActionResult = 25
    VLF_FileName = 'Factory_make'
    VLF_FilePath = 'C:\\factory\\make'
    VLF_FileNameInCompressedFile = 'win32'
    VLF_InfectionSource = 'Factory Make'
    VLF_InfectionDestination = 'Factory.Make@test.mail.com'
    VLF_EngineType = 4096
    VLF_EngineVersion = '1.83.5566'
    VLF_PatternType = None
    VLF_PatternNumber = 55688
    SIC_RuleName = None
    MVL_Protocol = None
    MVL_DeliverTime = None
    MVL_StorageGroup = None
    MVL_DataBaseName = None
    MVL_FolderName = None
    MVL_MessageID = None
    DVL_ClientIPAddress = None
    DVL_ResultCode = None
    FVL_InfectTarget = None
    FVL_LoginUser = None
    MVL_Subject = None
    DCS_JobID = None
    DCS_TaskID = None
    VLF_MajorVirusType = 1
    VLF_SubVirusType = 0
    VLF_PrivateAttribute = None
    VLF_ClientGUID = '112E85840114-694DBF9D-44CC-65D3-0003'
    AggregatedCount = 1
    AggregatedLocalToTime = None
    AggregatedUTCToTime = None
    SourceIP = None
    DestIP = None
    UserGroupName = None
    SLF_FileSHA1 = None
    SLF_CloudStorage = None
    CE_FilterID = None
    SLF_Channel = None
    CLF_LogGenCMLocalTime = ExtendDateTime.current_time()

    @factory.lazy_attribute_sequence
    def MsgLogID(self, n):
        return "503C31155B94-4E8B9FF2-VIRU-SLOG-{:A>4}".format(n)

    @factory.lazy_attribute
    def VLF_ClientGUID(self):
        return TbEntityInfo.find_by_machine_name(self.CLF_ComputerName).EI_EntityID

    @factory.lazy_attribute
    def CLF_ProductVersion(self):
        return TbEntityInfo.find_by_machine_name(self.CLF_ComputerName).EI_ProductVersion

    @factory.lazy_attribute
    def CLF_ProductType(self):
        return TbEntityInfo.find_by_machine_name(self.CLF_ComputerName).EI_ProductType

    @factory.lazy_attribute
    def CLF_ManagerID(self):
        return TbEntityInfo.find_by_machine_name(self.CLF_ComputerName).EI_ManagerID

    @factory.lazy_attribute
    def CLF_EntityID(self):
        return TbEntityInfo.find_by_machine_name(self.CLF_ComputerName).EI_AgentID
