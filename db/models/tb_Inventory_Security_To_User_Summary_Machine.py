from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BINARY, CHAR, DATETIME, INTEGER, SMALLINT, VARCHAR


class TbInventorySecurityToUserSummaryMachine(Base):
    __tablename__ = 'tb_Inventory_Security_To_User_Summary_Machine'
    id = Column(BIGINT, primary_key=True, nullable=False)
    EventType = Column(SMALLINT)
    LogGenLocalDate = Column(DATETIME)
    MachineGuid = Column(CHAR(36))
    EventContentType = Column(SMALLINT)
    EventContent_MD5 = Column(BINARY(16))
    EventContentCategory = Column(SMALLINT)
    RetroScanCategory = Column(SMALLINT)
    CE_FilterID = Column(VARCHAR(35))
    Count = Column(INTEGER)
    RequireActionCount = Column(INTEGER)
    ResolvedCount = Column(INTEGER)
