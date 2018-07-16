from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, SMALLINT, VARCHAR


class TbBIFWeeklySoInfo(Base):
    __tablename__ = 'tb_BIFWeeklySoInfo'
    SOType = Column(SMALLINT, primary_key=True, nullable=False)
    ProductID = Column(VARCHAR(36), primary_key=True, nullable=False)
    Count = Column(INTEGER)
    LastUpdateTime = Column(DATETIME)
