from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BINARY, CHAR, DATETIME, INTEGER, SMALLINT, VARCHAR


class TbInventorySecurityToUserSummaryEndpoint(Base):
    __tablename__ = 'tb_Inventory_Security_To_User_Summary_Endpoint'
    id = Column(BIGINT, primary_key=True, nullable=False)
    EventType = Column(SMALLINT)
    LogGenLocalDate = Column(DATETIME)
    ClientGuid = Column(CHAR(36))
    EventContentType = Column(SMALLINT)
    EventContent_MD5 = Column(BINARY(16))
    RetroScanCategory = Column(SMALLINT)
    EventContentCategory = Column(SMALLINT)
    CE_FilterID = Column(VARCHAR(35))
    Count = Column(INTEGER)
    RequireActionCount = Column(INTEGER)
    ResolvedCount = Column(INTEGER)
