from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, IMAGE, INTEGER, VARCHAR


class TbRedAlertTamDefaultSettings(Base):
    __tablename__ = 'tb_RedAlertTamDefaultSettings'
    RATDS_ID = Column(CHAR(36), primary_key=True, nullable=False)
    RATDS_FirstAidEManFilters = Column(VARCHAR(64))
    RATDS_FirstAidDefaultSetting = Column(IMAGE)
    RATDS_RTScanDefaultSetting = Column(IMAGE)
    RATDS_ScanNowDefaultSetting = Column(IMAGE)
    RATDS_PolicyVersion = Column(INTEGER)
    RATDS_DefaultSettingsStatus = Column(VARCHAR(64))
    RATDS_VulnIDs = Column(IMAGE)
