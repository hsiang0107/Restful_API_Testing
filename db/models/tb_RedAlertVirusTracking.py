from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbRedAlertVirusTracking(Base):
    __tablename__ = 'tb_RedAlertVirusTracking'
    RAVT_ID = Column(CHAR(36), primary_key=True, nullable=False)
    RAVT_RedAlertID = Column(CHAR(36), nullable=False)
    RAVT_ProductType = Column(INTEGER)
    RAVT_VirusCount = Column(INTEGER)
    RAVT_CreateTime = Column(DATETIME)
