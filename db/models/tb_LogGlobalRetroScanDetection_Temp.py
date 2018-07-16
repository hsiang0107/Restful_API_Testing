from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbLogGlobalRetroScanDetectionTemp(Base):
    __tablename__ = 'tb_LogGlobalRetroScanDetection_Temp'
    id = Column(INTEGER, primary_key=True, nullable=False)
    RetroScanContent = Column(NVARCHAR(2048), nullable=False)
    SLF_URLCorrelationKey = Column(VARCHAR(64))
    ClientIP = Column(VARCHAR(256))
    CallbackTime = Column(DATETIME, nullable=False)
    ServerGUID = Column(VARCHAR(64))
    ReportID = Column(VARCHAR(64), nullable=False)
