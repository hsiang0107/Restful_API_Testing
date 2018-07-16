from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbRedAlertCommandTracking(Base):
    __tablename__ = 'tb_RedAlertCommandTracking'
    RACT_ID = Column(CHAR(36), primary_key=True, nullable=False)
    RACT_RedAlertID = Column(CHAR(36), nullable=False)
    RACT_CommandTrackingID = Column(CHAR(36), nullable=False)
    RACT_Command = Column(INTEGER)
    RACT_CreateTime = Column(DATETIME)
    RACT_NodeInfo = Column(VARCHAR(2048))
