from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbInventoryCriticalEventSummaryEndpoint(Base):
    __tablename__ = 'tb_Inventory_CriticalEvent_Summary_Endpoint'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ClientGuid = Column(CHAR(36))
    CE_FilterID = Column(VARCHAR(35))
    LastDetectionTime = Column(DATETIME)
