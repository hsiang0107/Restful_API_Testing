from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, SMALLINT, VARCHAR


class TbAVStatusPatternInfo(Base):
    __tablename__ = 'tb_AVStatusPatternInfo'
    SPI_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    SPI_PatternType = Column(INTEGER, primary_key=True)
    SPI_PatternVersion = Column(VARCHAR(19))
    SPI_PatternLastUpdateTime = Column(DATETIME)
    SPI_IsInUse = Column(SMALLINT)
    LUTonTMCM = Column(DATETIME)
    SPI_PatternLastUpdateUTCTime = Column(DATETIME)
