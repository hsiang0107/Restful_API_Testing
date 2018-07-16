from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbTopTenSource(Base):
    __tablename__ = 'tb_TopTenSource'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_ProductType = Column(INTEGER, nullable=False)
    VLF_InfectionSource = Column(NVARCHAR(254))
    TTS_Total = Column(INTEGER, nullable=False)
    TTS_SummaryTime = Column(DATETIME)
    TTS_YEAR = Column(INTEGER, nullable=False)
    TTS_MONTH = Column(INTEGER, nullable=False)
    TTS_DAY = Column(INTEGER, nullable=False)
