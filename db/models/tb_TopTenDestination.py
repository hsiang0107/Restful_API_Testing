from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbTopTenDestination(Base):
    __tablename__ = 'tb_TopTenDestination'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_ProductType = Column(INTEGER, nullable=False)
    VLF_InfectionDestination = Column(NVARCHAR(254))
    TTD_Total = Column(INTEGER, nullable=False)
    TTD_SummaryTime = Column(DATETIME)
    TTD_YEAR = Column(INTEGER, nullable=False)
    TTD_MONTH = Column(INTEGER, nullable=False)
    TTD_DAY = Column(INTEGER, nullable=False)
