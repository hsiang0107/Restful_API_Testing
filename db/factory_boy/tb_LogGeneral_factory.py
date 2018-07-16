import factory
import datetime
from db.factory_boy.cm_factory import CMFactory
from db import TbLogGeneral, TbSystemInfo, TbEntityInfo
from lib.extend_datetime import ExtendDateTime


class TbLogGeneralFactory(CMFactory):
    class Meta:
        model = TbLogGeneral
        sqlalchemy_session_persistence = 'commit'

    CMGuid = TbSystemInfo.get_CM_guid()
    LogReferenceID = None
    Authentication = 1
    ConstraintType = 0
    ComputerName = 'DDI01'
    DaylightSavingInMins = 0
    Description = 'Factory Make'
    DetectedBy = 42
    DetectionName = 'Factory Made Virus'
    LogGenLocalDatetime = ExtendDateTime.get_date_by_offset('-1')
    LogGenUTCDatetime = ExtendDateTime.get_date_by_offset('-1')
    LogMinorVersion = 4
    LogVersion = 1
    MsgType = 1723
    PotentialRisk = 0
    Protocol = 5
    ProtocolGroup = 8
    RiskType = 'AV'
    RiskTypeGroup = 1
    RuleID = 709
    ScanDirection = 4
    TimeZoneInMins = 0
    VLANId = 5
    CLF_LogReceivedTime = datetime.datetime.now()
    CollaborationID = '73599893-97B1-4678-B964-4D9B3FEDAAE4'
    Severity = 1
    SLF_InterestedIP = None
    SLF_PeerIP = '5.5.6.6'
    SLF_Is_CCCA_Detection = 1
    SLF_CCCA_DetectionSource = 1
    SLF_CCCA_Destination = None
    SLF_CCCA_RiskLevel = 0
    SLF_CCCA_DestinationFormat = None
    ThreatType = 1
    IsBlocked = 0
    InterestedGroupName = 'Fake Group'
    DetectionType = 1
    EventTotalCount = 1
    EventAggregatedCount = 1
    ECE_SeverityCode = 1
    AttackPhase = 1
    DetectedByVA = 1
    LogNativeID = 9223372036854775807
    DCEHash1 = 9223372036854775807
    DCEHash2 = 9223372036854775807
    Remarks = 'Fake Remark'
    CC_Server = 'Fake Server'
    CC_ServerType = 1
    MalwareType = 'Fake Malware Type'
    Event_Class = 4
    Event_SubClass = 2
    HeurFlag = 3
    CommonThreatFamily = 'Fake Common Threat Family'
    SLF_URLCorrelationKey = None
    VADetectionName = None
    ThreatCharacteristics = None
    CE_FilterID = None

    @factory.lazy_attribute_sequence
    def MsgLogID(self, n):
        return "503C31155B94-4E8B9FF2-LOGE-79A5-{:B>4}".format(n)

    @factory.lazy_attribute
    def ProductGUID(self):
        return TbEntityInfo.find_by_machine_name(self.ComputerName).EI_EntityID

    @factory.lazy_attribute
    def ProductID(self):
        return TbEntityInfo.find_by_machine_name(self.ComputerName).EI_ProductType
