from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbGlobalRetroScanTask(Base):
    __tablename__ = 'tb_GlobalRetroScanTask'
    id = Column(INTEGER, primary_key=True, nullable=False)
    RetroScanContent = Column(NVARCHAR(2048), nullable=False)
    EventContentMD5 = Column(BINARY(16), nullable=False)
    RetroScanCategory = Column(SMALLINT, nullable=False)
    ProgressState = Column(SMALLINT, nullable=False)
    LatestHttpResponseCode = Column(INTEGER)
    ReportID = Column(VARCHAR(64))
    ResultCode = Column(SMALLINT)
    InitiateTime = Column(DATETIME)
    ReportSubmitTime = Column(DATETIME)
    ReportReceiveTime = Column(DATETIME)
