from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, IMAGE, INTEGER, NVARCHAR, VARCHAR


class TbDCSTask(Base):
    __tablename__ = 'tb_DCSTask'
    TaskID = Column(INTEGER, primary_key=True, nullable=False)
    TaskName = Column(NVARCHAR(64), nullable=False)
    CreateTime = Column(DATETIME, nullable=False)
    MachineList = Column(IMAGE, nullable=False)
    ScheduleTime = Column(VARCHAR(32))
    CompleteTime = Column(DATETIME)
    Properties = Column(INTEGER, nullable=False)
    VAS_TaskRelationID = Column(VARCHAR(36))
    VAS_Properties = Column(INTEGER)
