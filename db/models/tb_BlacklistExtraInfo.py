from sqlalchemy import Column, desc
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbBlacklistExtraInfo(Base):
    __tablename__ = 'tb_BlacklistExtraInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Key = Column(VARCHAR(256), nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    SubmitTime = Column(DATETIME)
    AnalyzeTime = Column(DATETIME)
    SubmitterProductName = Column(NVARCHAR(64))
    SubmitterHostName = Column(NVARCHAR(64))
    SubmitterIPAddress = Column(VARCHAR(128))
    FileName = Column(NVARCHAR)
    TrueFileType = Column(NVARCHAR(64))
    DetectionName = Column(NVARCHAR(1024))
    ThreatCharacteristics = Column(NVARCHAR(128))
    SampleIdentity = Column(NVARCHAR)
    AnalyzeReportID = Column(VARCHAR(128))
    Protocol = Column(INTEGER)
    Source = Column(NVARCHAR(1024))
    Destination = Column(NVARCHAR(1024))

    @classmethod
    def find_last_record_by_slf_key(cls, key):
        return cm_session.query(cls).filter(cls.SLF_Key == key).order_by(desc(cls.id)).first()
