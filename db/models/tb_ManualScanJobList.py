from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbManualScanJobList(Base):
    __tablename__ = 'tb_ManualScanJobList'
    MS_JobID = Column(CHAR(36), primary_key=True, nullable=False)
    MS_RcvDateTime = Column(DATETIME(32))
    MS_EntityID = Column(CHAR(36))
    MS_DstType = Column(INTEGER)
    MS_WaitTime = Column(INTEGER)
    MS_Status = Column(INTEGER)
    MS_Token = Column(VARCHAR(255), nullable=False)
    MS_ScanType = Column(INTEGER, nullable=False)
