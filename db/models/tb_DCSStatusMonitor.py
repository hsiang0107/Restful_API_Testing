from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbDCSStatusMonitor(Base):
    __tablename__ = 'tb_DCSStatusMonitor'
    StatusMonitorID = Column(INTEGER, primary_key=True, nullable=False)
    DomainName = Column(NVARCHAR(16), nullable=False)
    MachineName = Column(NVARCHAR(16), nullable=False)
    IPAddress = Column(VARCHAR(256), nullable=False)
    Status = Column(INTEGER, nullable=False)
    StartTime = Column(DATETIME, nullable=False)
    EndTime = Column(DATETIME, nullable=False)
    Malware = Column(VARCHAR(64))
