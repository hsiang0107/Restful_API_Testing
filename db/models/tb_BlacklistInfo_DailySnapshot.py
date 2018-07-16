from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, INTEGER


class TbBlacklistInfoDailySnapshot(Base):
    __tablename__ = 'tb_BlacklistInfo_DailySnapshot'
    id = Column(BIGINT, primary_key=True, nullable=False)
    Date = Column(DATETIME, nullable=False)
    Count = Column(INTEGER, nullable=False)
