from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR


class TbRedAlertVirusTrackingDetail(Base):
    __tablename__ = 'tb_RedAlertVirusTrackingDetail'
    RAVTD_VirusLogID = Column(CHAR(36), primary_key=True, nullable=False)
    RAVTD_RedAlertID = Column(CHAR(36), nullable=False)
    RAVTD_RedAlertVirusTrackingID = Column(CHAR(36), nullable=False)
