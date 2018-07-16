from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbVASStatusMonitor(Base):
    __tablename__ = 'tb_VASStatusMonitor'
    VAS_MonitorID = Column(INTEGER, primary_key=True, nullable=False)
    VAS_DomainName = Column(NVARCHAR(16), nullable=False)
    VAS_HostName = Column(NVARCHAR(64), nullable=False)
    VAS_IPAddress = Column(VARCHAR(256), nullable=False)
    VAS_StartTime = Column(DATETIME, nullable=False)
    VAS_EndTime = Column(DATETIME, nullable=False)
    VAS_Restricted = Column(INTEGER, nullable=False)
    VAS_Status = Column(INTEGER, nullable=False)
    VAS_Description = Column(INTEGER, nullable=False)
