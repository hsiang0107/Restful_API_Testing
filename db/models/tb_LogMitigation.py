from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, UNIQUEIDENTIFIER, VARCHAR


class TbLogMitigation(Base):
    __tablename__ = 'tb_LogMitigation'
    CMGuid = Column(CHAR(36))
    CollaborationID = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    ProductGUID = Column(CHAR(36))
    LogGenLocalDatetime = Column(DATETIME, nullable=False)
    LogGenUTCDatetime = Column(DATETIME, nullable=False)
    ThreatDescription = Column(NVARCHAR(256))
    InfectedHostName = Column(NVARCHAR(64))
    InfectedHostIP = Column(VARCHAR(256))
    MitigationStatus = Column(INTEGER)
    MitigationResult = Column(NVARCHAR(2048))
    LogReceivedTime = Column(DATETIME, nullable=False)
