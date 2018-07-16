from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbRedAlertAutoSetting(Base):
    __tablename__ = 'tb_RedAlertAutoSetting'
    id = Column(CHAR(36), primary_key=True, nullable=False)
    RAS_Status = Column(INTEGER, nullable=False)
    RAS_NotifySvcs = Column(INTEGER)
    RAS_Duration = Column(INTEGER, nullable=False)
    RAS_PlanID = Column(CHAR(36))
    RAS_ExcludedPdt = Column(VARCHAR(1024))
    RAS_IsAutoStop = Column(INTEGER)
