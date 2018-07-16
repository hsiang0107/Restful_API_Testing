from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbInventoryCriticalEventSummaryUser(Base):
    __tablename__ = 'tb_Inventory_CriticalEvent_Summary_User'
    id = Column(INTEGER, primary_key=True, nullable=False)
    UserObjectGuid = Column(CHAR(36))
    CE_FilterID = Column(VARCHAR(35))
    LastDetectionTime = Column(DATETIME)
