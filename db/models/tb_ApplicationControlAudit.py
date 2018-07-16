from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbApplicationControlAudit(Base):
    __tablename__ = 'tb_ApplicationControlAudit'
    id = Column(INTEGER, primary_key=True, nullable=False)
    SLF_MsgType = Column(INTEGER)
    SLF_ProductID = Column(SMALLINT)
    SLF_LogVersion = Column(SMALLINT)
    SLF_LogMinorVersion = Column(SMALLINT)
    SLF_LogGenUTCDatetime = Column(DATETIME)
    SLF_LogGenLocalDatetime = Column(DATETIME)
    SLF_TimeZoneInMins = Column(SMALLINT)
    SLF_DaylightSavingInMins = Column(SMALLINT)
    SLF_ClientGUID = Column(CHAR(36))
    SLF_ClientUserGUID = Column(CHAR(36))
    SLF_ClientUserName = Column(NVARCHAR(128))
    SLF_ClientUserDomain = Column(NVARCHAR(256))
    SLF_ClientUserDepartment = Column(NVARCHAR(256))
    SLF_ClientMachineArchitecture = Column(VARCHAR(64))
    SLF_ApplicationFileHash = Column(VARCHAR(40))
    SLF_ApplicationFileName = Column(NVARCHAR(256))
    SLF_ApplicationFileOwner = Column(NVARCHAR(256))
    SLF_ApplicationPath = Column(NVARCHAR(512))
    SLF_ApplicationDriveType = Column(SMALLINT)
    SLF_ApplicationFileCreatedUTCDatetime = Column(DATETIME)
    SLF_ApplicationFileModifiedUTCDatetime = Column(DATETIME)
    SLF_ApplicationFileDeletedUTCDatetime = Column(DATETIME)
