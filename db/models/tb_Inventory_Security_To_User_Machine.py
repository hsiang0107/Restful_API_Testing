from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BINARY, CHAR, DATETIME, INTEGER, SMALLINT, VARCHAR


class TbInventorySecurityToUserMachine(Base):
    __tablename__ = 'tb_Inventory_Security_To_User_Machine'
    id = Column(BIGINT, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36))
    LogType = Column(INTEGER)
    EventType = Column(SMALLINT)
    ProductType = Column(INTEGER)
    LogGenLocalTime = Column(DATETIME)
    MachineGuid = Column(CHAR(36))
    EventContentType = Column(SMALLINT)
    EventContent_MD5 = Column(BINARY(16))
    EventContentCategory = Column(SMALLINT)
    RetroScanCategory = Column(SMALLINT)
    SLF_CCCA_DetectionSource = Column(SMALLINT)
    Action = Column(SMALLINT)
    RetroScanData_MD5 = Column(BINARY(16))
    Description_MD5 = Column(BINARY(16))
    CE_FilterID = Column(VARCHAR(35))
    Channel = Column(SMALLINT)
