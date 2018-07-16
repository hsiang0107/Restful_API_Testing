from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import VARCHAR


class TbScheduleTaskCheckPoint(Base):
    __tablename__ = 'tb_ScheduleTaskCheckPoint'
    Name = Column(VARCHAR(64), primary_key=True, nullable=False)
    Value = Column(VARCHAR(256), nullable=False)
