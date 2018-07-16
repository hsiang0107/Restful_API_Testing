from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, SMALLINT, VARCHAR


class TbAVStatusEngineInfo(Base):
    __tablename__ = 'tb_AVStatusEngineInfo'
    SEI_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    SEI_EngineType = Column(INTEGER, primary_key=True)
    SEI_EngineVersion = Column(VARCHAR(19))
    SEI_EngineLastUpdateTime = Column(DATETIME)
    SEI_IsInUse = Column(SMALLINT)
    LUTonTMCM = Column(DATETIME)
    SEI_EngineLastUpdateUTCTime = Column(DATETIME)
