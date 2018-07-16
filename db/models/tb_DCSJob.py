from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, IMAGE, INTEGER, NVARCHAR, VARCHAR


class TbDCSJob(Base):
    __tablename__ = 'tb_DCSJob'
    JobID = Column(INTEGER, primary_key=True, nullable=False)
    TaskID = Column(INTEGER, nullable=False)
    TaskName = Column(NVARCHAR(64))
    StartTime = Column(DATETIME)
    EndTime = Column(DATETIME)
    IssuedBy = Column(NVARCHAR(32))
    MA_MachineList = Column(IMAGE, nullable=False)
    UnsupportMachineList = Column(IMAGE)
    DamageCleanupEngine = Column(VARCHAR(19))
    DamageCleanupPattern = Column(VARCHAR(19))
    Properties = Column(INTEGER)
    DeployMissed = Column(INTEGER)
    DamageMachines = Column(INTEGER)
    DamageFree = Column(INTEGER)
    CleanMissed = Column(INTEGER)
    InProgress = Column(INTEGER)
    UnsupportMachines = Column(INTEGER)
    Total = Column(INTEGER)
