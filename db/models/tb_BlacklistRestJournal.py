from sqlalchemy import Column, desc
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbBlacklistRestJournal(Base):
    __tablename__ = 'tb_BlacklistRestJournal'
    id = Column(BIGINT, primary_key=True, nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    SLF_Key = Column(VARCHAR(256))
    SLF_Action = Column(SMALLINT, nullable=False)
    SLF_Type = Column(INTEGER, nullable=False)
    SLF_Data = Column(NVARCHAR, nullable=False)
    SLF_RiskLevel = Column(INTEGER, nullable=False)
    SLF_ExpireDateTimeStamp = Column(BIGINT, nullable=False)
    SLF_ExpiredUTCDate = Column(DATETIME, nullable=False)
    ViolatedDTASPolicy = Column(VARCHAR(256))
    SourceFileSHA1 = Column(VARCHAR(64))
    Detectable = Column(SMALLINT)
    SourceType = Column(SMALLINT, nullable=False)
    ScanAction = Column(SMALLINT)
    FilterCRC = Column(VARCHAR(64))
    RootFileSHA1 = Column(VARCHAR(128))
    DataMD5 = Column(VARCHAR(256))
    Status = Column(SMALLINT)
    FromTmcm = Column(SMALLINT)

    @classmethod
    def find_last_record_by_slf_key(cls, key):
        return cm_session.query(cls).filter(cls.SLF_Key == key).order_by(desc(cls.id)).first()
