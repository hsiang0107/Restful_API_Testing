from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR


class TbLogDataLossPreventionSetting(Base):
    __tablename__ = 'tb_LogDataLossPreventionSetting'
    event_id = Column(NVARCHAR(256), primary_key=True, nullable=False)
    instance_hourly = Column(INTEGER, nullable=False)
    instance_daily = Column(INTEGER, nullable=False)
    last_invoke_hourly = Column(DATETIME, nullable=False)
    last_invoke_daily = Column(DATETIME, nullable=False)
