from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbProductRoleBaseAuditLog(Base):
    __tablename__ = 'tb_ProductRoleBaseAuditLog'
    CMGuid = Column(CHAR(36))
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    MsgLogType = Column(INTEGER)
    ProductGUID = Column(CHAR(36))
    ProductID = Column(INTEGER)
    LogVersion = Column(INTEGER)
    LogMinorVersion = Column(INTEGER)
    ComputerName = Column(NVARCHAR(128))
    LogGenUTCDatetime = Column(DATETIME)
    LogGenLocalDatetime = Column(DATETIME)
    TimeZoneInMins = Column(INTEGER)
    DaylightSavingInMins = Column(INTEGER)
    LogReceivedTime = Column(DATETIME)
    EventCategory = Column(INTEGER)
    EventLevel = Column(INTEGER)
    UserName = Column(NVARCHAR(64))
    EventDescription = Column(NVARCHAR(2048))
