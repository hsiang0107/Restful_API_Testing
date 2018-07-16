from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbServerDetailStatusInfo(Base):
    __tablename__ = 'tb_ServerDetailStatusInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ServerID = Column(VARCHAR(36), nullable=False)
    DiskUsage = Column(VARCHAR(10))
    DiskTotal = Column(VARCHAR(10))
    DiskUnit = Column(VARCHAR(10))
    DiskPercent = Column(VARCHAR(10))
    DiskLevel = Column(INTEGER)
    CPUPercent = Column(VARCHAR(10))
    CPULevel = Column(INTEGER)
    MemoryUsage = Column(VARCHAR(10))
    MemoryTotal = Column(VARCHAR(10))
    MemoryUnit = Column(VARCHAR(10))
    MemoryPercent = Column(VARCHAR(10))
    MemoryLevel = Column(INTEGER)
    Samples = Column(INTEGER)
    SamplesLevel = Column(INTEGER)
    LastUpdateUTCTime = Column(DATETIME)
    ServerStatus = Column(INTEGER)
