from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, TINYINT, UNIQUEIDENTIFIER, VARCHAR


class TbLogGeneral(Base):
    __tablename__ = 'tb_LogGeneral'
    id = Column(BIGINT, primary_key=True, nullable=False)
    CMGuid = Column(CHAR(36))
    LogReferenceID = Column(INTEGER)
    Authentication = Column(INTEGER)
    ConstraintType = Column(INTEGER)
    ComputerName = Column(NVARCHAR(128))
    DaylightSavingInMins = Column(INTEGER)
    Description = Column(VARCHAR(256))
    DetectedBy = Column(INTEGER)
    DetectionName = Column(VARCHAR(64))
    LogGenLocalDatetime = Column(DATETIME, nullable=False)
    LogGenUTCDatetime = Column(DATETIME, nullable=False)
    LogMinorVersion = Column(SMALLINT)
    LogVersion = Column(SMALLINT)
    MsgType = Column(INTEGER, nullable=False)
    PotentialRisk = Column(INTEGER)
    ProductGUID = Column(CHAR(36), nullable=False)
    ProductID = Column(INTEGER, nullable=False)
    Protocol = Column(INTEGER)
    ProtocolGroup = Column(INTEGER)
    RiskType = Column(VARCHAR(32))
    RiskTypeGroup = Column(INTEGER)
    RuleID = Column(INTEGER)
    ScanDirection = Column(INTEGER)
    TimeZoneInMins = Column(SMALLINT)
    VLANId = Column(INTEGER)
    CLF_LogReceivedTime = Column(DATETIME)
    CollaborationID = Column(UNIQUEIDENTIFIER)
    Severity = Column(INTEGER)
    SLF_InterestedIP = Column(VARCHAR(256))
    SLF_PeerIP = Column(VARCHAR(256))
    SLF_Is_CCCA_Detection = Column(INTEGER)
    SLF_CCCA_DetectionSource = Column(INTEGER)
    SLF_CCCA_Destination = Column(VARCHAR(2048))
    SLF_CCCA_RiskLevel = Column(INTEGER)
    SLF_CCCA_DestinationFormat = Column(INTEGER)
    MsgLogID = Column(CHAR(36))
    ThreatType = Column(SMALLINT)
    IsBlocked = Column(TINYINT)
    InterestedGroupName = Column(NVARCHAR(128))
    DetectionType = Column(SMALLINT)
    EventTotalCount = Column(INTEGER)
    EventAggregatedCount = Column(INTEGER)
    ECE_SeverityCode = Column(SMALLINT)
    AttackPhase = Column(SMALLINT)
    DetectedByVA = Column(TINYINT)
    LogNativeID = Column(BIGINT)
    DCEHash1 = Column(BIGINT)
    DCEHash2 = Column(BIGINT)
    Remarks = Column(NVARCHAR(2176))
    CC_Server = Column(NVARCHAR(2138))
    CC_ServerType = Column(SMALLINT)
    MalwareType = Column(VARCHAR(256))
    Event_Class = Column(SMALLINT)
    Event_SubClass = Column(SMALLINT)
    HeurFlag = Column(SMALLINT)
    CommonThreatFamily = Column(VARCHAR(256))
    SLF_URLCorrelationKey = Column(VARCHAR(64))
    VADetectionName = Column(NVARCHAR(2048))
    ThreatCharacteristics = Column(NVARCHAR(128))
    CE_FilterID = Column(VARCHAR(35))
    CLF_LogGenCMLocalTime = Column(DATETIME)
