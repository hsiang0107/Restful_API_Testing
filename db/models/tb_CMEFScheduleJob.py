from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, VARCHAR


class TbCMEFScheduleJob(Base):
    __tablename__ = 'tb_CMEFScheduleJob'
    id = Column(BIGINT, primary_key=True, nullable=False)
    JobGUID = Column(CHAR(36), nullable=False)
    Creator = Column(CHAR(36), nullable=False)
    JobDescription = Column(VARCHAR(64), nullable=False)
    DllName = Column(VARCHAR(64), nullable=False)
    CommandText = Column(VARCHAR(1024), nullable=False)
    CronExpression = Column(VARCHAR(64), nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
