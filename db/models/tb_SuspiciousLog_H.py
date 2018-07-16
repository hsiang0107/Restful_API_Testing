from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, TINYINT, VARCHAR


class TbSuspiciousLogH(Base):
    __tablename__ = 'tb_SuspiciousLog_H'
    id = Column(BIGINT, primary_key=True, nullable=False)
    LogNativeID = Column(BIGINT)
    LogType = Column(SMALLINT)
    LogGenUTCDatetime = Column(DATETIME)
    ProductGUID = Column(CHAR(36))
    DetectionName = Column(VARCHAR(64))
    ThreatType = Column(SMALLINT)
    SourceIP = Column(VARCHAR(15))
    DestIP = Column(VARCHAR(15))
    Protocol = Column(INTEGER)
    FileName = Column(NVARCHAR(512))
    RuleID = Column(INTEGER)
    InterestedIP = Column(VARCHAR(15))
    HostName = Column(VARCHAR(256))
    Group = Column(NVARCHAR(128))
    ECE_SeverityCode = Column(SMALLINT)
    Remarks = Column(NVARCHAR(2176))
    CC_Server = Column(NVARCHAR(2138))
    CC_ServerType = Column(SMALLINT)
    SLF_CCCA_DetectionSource = Column(INTEGER)
    SLF_PeerIP = Column(VARCHAR(256))
    Description = Column(VARCHAR(256))
    SHA1 = Column(VARCHAR(40))
    MalwareType = Column(VARCHAR(256))
    DetectedByVA = Column(TINYINT)
    HeurFlag = Column(SMALLINT)
    AttackPhase = Column(SMALLINT)
