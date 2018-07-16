from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbLogGlobalRetroScanDetection(Base):
    __tablename__ = 'tb_LogGlobalRetroScanDetection'
    id = Column(INTEGER, primary_key=True, nullable=False)
    DetectionKey = Column(VARCHAR(64), nullable=False)
    RetroScanContent = Column(NVARCHAR(2048), nullable=False)
    EventContentMD5 = Column(BINARY(16), nullable=False)
    RetroScanCategory = Column(SMALLINT, nullable=False)
    SLF_URLCorrelationKey = Column(VARCHAR(64))
    ClientIP = Column(VARCHAR(256))
    CallbackTime = Column(DATETIME, nullable=False)
    ServerGUID = Column(VARCHAR(64))
    LastUpdateTime = Column(DATETIME, nullable=False)
    ReportID = Column(VARCHAR(64), nullable=False)
