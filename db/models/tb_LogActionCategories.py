from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, SMALLINT


class TbLogActionCategories(Base):
    __tablename__ = 'tb_LogActionCategories'
    LogType = Column(INTEGER, primary_key=True, nullable=False)
    Action = Column(SMALLINT, primary_key=True, nullable=False)
    ActionCategory = Column(SMALLINT, nullable=False)
