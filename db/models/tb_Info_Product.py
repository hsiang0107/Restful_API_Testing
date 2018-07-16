from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, SMALLINT, VARCHAR


class TbInfoProduct(Base):
    __tablename__ = 'tb_Info_Product'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Guid = Column(CHAR(36), nullable=False)
    AgentGuid = Column(CHAR(36), nullable=False)
    ParentGuid = Column(CHAR(36), nullable=False)
    CMGuid = Column(CHAR(36), nullable=False)
    ProductType = Column(INTEGER)
    ProductVersion = Column(VARCHAR(19))
    MenuVersion = Column(VARCHAR(8))
    ProductLanguage = Column(INTEGER)
    BuildNumber = Column(VARCHAR(24))
    Status = Column(INTEGER)
    ProductStatusMask = Column(SMALLINT)
    ConfigureURL = Column(VARCHAR(509))
    LastRegistrationTime = Column(DATETIME)
    LastLogonTime = Column(DATETIME)
    ServicePack = Column(VARCHAR(32))
    EntityType = Column(INTEGER)
