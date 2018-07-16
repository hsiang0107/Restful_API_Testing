from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbCTDNotMitigatedRankTmp(Base):
    __tablename__ = 'tb_CTD_NotMitigatedRank_Tmp'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Rank = Column(INTEGER)
    MaxEndpointID = Column(INTEGER)
    MaxMachineID = Column(INTEGER)
    RetroScanMD5 = Column(BINARY(16))
    RetroScanCategory = Column(SMALLINT)
    SuspiciousObject = Column(NVARCHAR(2048))
    SLF_Key = Column(VARCHAR(256))
    SLF_RiskLevel = Column(SMALLINT)
    SampleData = Column(NVARCHAR)
    Submitter = Column(NVARCHAR(64))
    ImportantRequiredActionEndpointCounts = Column(INTEGER)
    OtherRequiredActionEndpointCounts = Column(INTEGER)
    ImportantSuccessActionEndpointCounts = Column(INTEGER)
    OtherSuccessActionEndpointCounts = Column(INTEGER)
