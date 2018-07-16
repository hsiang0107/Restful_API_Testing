from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbTopTenVirus(Base):
    __tablename__ = 'tb_TopTenVirus'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_ProductType = Column(INTEGER, nullable=False)
    VLF_VirusName = Column(VARCHAR(64))
    TTV_Total = Column(INTEGER, nullable=False)
    TTV_SummaryTime = Column(DATETIME)
    TTV_YEAR = Column(INTEGER, nullable=False)
    TTV_MONTH = Column(INTEGER, nullable=False)
    TTV_DAY = Column(INTEGER, nullable=False)
