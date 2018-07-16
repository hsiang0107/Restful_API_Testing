from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbFileHashDetectionByUser(Base):
    __tablename__ = 'tb_FileHashDetectionByUser'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Key = Column(VARCHAR(256), nullable=False)
    SLF_Recipient = Column(NVARCHAR(254), nullable=False)
    SLF_ActionGroup = Column(SMALLINT, nullable=False)
    SLF_SOSourceType = Column(SMALLINT, nullable=False)
    SLF_FirstSender = Column(NVARCHAR(254))
    SLF_FirstSubject = Column(NVARCHAR(254))
    SLF_FirstEntryChannel = Column(INTEGER)
    SLF_FirstProductID = Column(INTEGER)
    SLF_FirstAction = Column(SMALLINT)
    SLF_FirstMsgType = Column(INTEGER)
    SLF_FirstUTCTime = Column(DATETIME)
    SLF_FirstFileCreatedUTCTime = Column(DATETIME)
    SLF_FirstFilePathName = Column(NVARCHAR(1024))
    SLF_LatestSender = Column(NVARCHAR(254))
    SLF_LatestSubject = Column(NVARCHAR(254))
    SLF_LatestEntryChannel = Column(INTEGER)
    SLF_LatestProductID = Column(INTEGER)
    SLF_LatestAction = Column(SMALLINT)
    SLF_LatestMsgType = Column(INTEGER)
    SLF_LatestUTCTime = Column(DATETIME)
    SLF_LatestFileCreatedUTCTime = Column(DATETIME)
    SLF_LatestFilePathName = Column(NVARCHAR(1024))
    SLF_ActionResult = Column(SMALLINT)
