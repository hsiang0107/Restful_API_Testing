from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbSystemEngineList(Base):
    __tablename__ = 'tb_SystemEngineList'
    SYS_EngineID = Column(INTEGER, primary_key=True)
    SYS_EngineVersion = Column(VARCHAR(19), primary_key=True)
    SYS_EngineUpdate = Column(DATETIME)
