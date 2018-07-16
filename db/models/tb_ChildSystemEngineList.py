from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbChildSystemEngineList(Base):
    __tablename__ = 'tb_ChildSystemEngineList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    CSEL_SystemID = Column(CHAR(36), nullable=False)
    CSEL_EngineID = Column(INTEGER, nullable=False)
    CSEL_EngineVersion = Column(VARCHAR(19), nullable=False)
    CSEL_EngineUpdate = Column(DATETIME, nullable=False)
