from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbScheduleTask(Base):
    __tablename__ = 'tb_ScheduleTask'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ScheduleName = Column(VARCHAR(1024))
    ScheduleID = Column(UNIQUEIDENTIFIER, nullable=False)
    Parameters = Column(NVARCHAR)
    Context = Column(NVARCHAR)
    FrequencyType = Column(SMALLINT, nullable=False)
    FrequencyRange = Column(INTEGER, nullable=False)
    RetryTimes = Column(INTEGER, nullable=False)
    Target = Column(VARCHAR(1024))
    Enable = Column(SMALLINT, nullable=False)
    LastUpdateUTCTime = Column(DATETIME)
    SpecificTime = Column(VARCHAR(32))

    @classmethod
    def update_schedule_time(cls, target, freq):
        cm_session.query(cls).filter(cls.Target == target).update({cls.FrequencyRange: freq})
        cm_session.commit()
