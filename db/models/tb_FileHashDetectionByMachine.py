from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbFileHashDetectionByMachine(Base):
    __tablename__ = 'tb_FileHashDetectionByMachine'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Key = Column(VARCHAR(256), nullable=False)
    SLF_MachineID = Column(CHAR(36), nullable=False)
    SLF_ActionGroup = Column(SMALLINT, nullable=False)
    SLF_SOSourceType = Column(SMALLINT)
    SLF_FirstProductID = Column(INTEGER)
    SLF_FirstAction = Column(SMALLINT)
    SLF_FirstMsgType = Column(INTEGER)
    SLF_FirstUTCTime = Column(DATETIME)
    SLF_FirstFileCreatedUTCTime = Column(DATETIME)
    SLF_FirstSourceEntityGUID = Column(CHAR(36))
    SLF_FirstFilePathName = Column(NVARCHAR(1024))
    SLF_LatestProductID = Column(INTEGER)
    SLF_LatestAction = Column(SMALLINT)
    SLF_LatestMsgType = Column(INTEGER)
    SLF_LatestUTCTime = Column(DATETIME)
    SLF_LatestFileCreatedUTCTime = Column(DATETIME)
    SLF_LatestSourceEntityGUID = Column(CHAR(36))
    SLF_LatestFilePathName = Column(NVARCHAR(1024))
    SLF_ActionResult = Column(SMALLINT)
