from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR


class TbRedAlertCmdHistory(Base):
    __tablename__ = 'tb_RedAlertCmdHistory'
    RACH_RedAlertID = Column(CHAR(36), nullable=False)
    RACH_TamID = Column(CHAR(36))
    RACH_PolicyVersion = Column(INTEGER)
    RACH_CreationOrder = Column(INTEGER, primary_key=True, nullable=False)
    RACH_CreationTime = Column(DATETIME, nullable=False)
    RACH_FA_LUT = Column(DATETIME)
    RACH_FirstAidCmd = Column(IMAGE)
    RACH_NOTIF_LUT = Column(DATETIME)
    RACH_NotificationCmd = Column(IMAGE)
    RACH_RTS_LUT = Column(DATETIME)
    RACH_RealTimeScanConfigCmd = Column(IMAGE)
    RACH_UPDATE_LUT = Column(DATETIME)
    RACH_UpdateCmd = Column(IMAGE)
    RACH_SNC_LUT = Column(DATETIME)
    RACH_ScanNowConfigCmd = Column(IMAGE)
    RACH_SSN_LUT = Column(DATETIME)
    RACH_StartScanNowCmd = Column(IMAGE)
    RACH_CreatorName = Column(NVARCHAR(256))
