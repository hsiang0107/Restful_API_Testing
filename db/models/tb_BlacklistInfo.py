from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BIT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbBlacklistInfo(Base):
    __tablename__ = 'tb_BlacklistInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Key = Column(VARCHAR(256), nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    SLF_Action = Column(SMALLINT, nullable=False)
    SLF_Type = Column(INTEGER, nullable=False)
    SLF_Data = Column(NVARCHAR, nullable=False)
    SLF_RiskLevel = Column(INTEGER, nullable=False)
    SLF_ExpireDateTimeStamp = Column(BIGINT, nullable=False)
    SLF_ExpiredUTCDate = Column(DATETIME, nullable=False)
    SLF_URLCorrelationKey = Column(VARCHAR(64))
    ViolatedDTASPolicy = Column(VARCHAR(256))
    SourceFileSHA1 = Column(VARCHAR(64))
    Detectable = Column(SMALLINT)
    SourceType = Column(SMALLINT, nullable=False)
    ScanAction = Column(SMALLINT)
    Status = Column(SMALLINT)
    FilterCRC = Column(VARCHAR(64))
    HasAssessed = Column(BIT)
    LastAssessedTime = Column(DATETIME)
    LastUpdateTime = Column(DATETIME)
    LatestAnalyzeReportID = Column(VARCHAR(128))
    UserDefinedTime = Column(DATETIME)
    UserDefinedNotes = Column(NVARCHAR)
    RootFileSHA1 = Column(VARCHAR(128))
    DataMD5 = Column(VARCHAR(256))
    IsWildcardException = Column(BIT)
    IsExceptionDueToWildcard = Column(BIT)

    @classmethod
    def find_by_key(cls, slf_key):
        return cm_session.query(cls).filter(cls.SLF_Key == slf_key).first()

    @classmethod
    def find_by_slf_data(cls, slf_data):
        return cm_session.query(cls).filter(cls.SLF_Data == slf_data).first()

    @classmethod
    def find_by_note(cls, note):
        return cm_session.query(cls).filter(cls.UserDefinedNotes == note).first()

    @classmethod
    def get_count(cls):
        return cm_session.query(cls).count()