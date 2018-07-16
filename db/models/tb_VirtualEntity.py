from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbVirtualEntity(Base):
    __tablename__ = 'tb_VirtualEntity'
    id = Column(INTEGER, primary_key=True, nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    Owner = Column(INTEGER)
    Certificate = Column(VARCHAR(49))
    RegisterTime = Column(DATETIME)
    ProductType = Column(VARCHAR(9), nullable=False)
    SiteName = Column(VARCHAR(39), nullable=False)
    GroupName = Column(VARCHAR(39), nullable=False)
    ServerName = Column(VARCHAR(39), nullable=False)
    InformationServerName = Column(VARCHAR(39))
    ServerIPAddress = Column(VARCHAR(256))
    SerialNumber = Column(VARCHAR(39))
    FullSerialNumber = Column(VARCHAR(39))
    PatternVer = Column(VARCHAR(19))
    EngineVer = Column(VARCHAR(19))
    ProgramVer = Column(VARCHAR(19))
    TimeZone = Column(VARCHAR(9))
    AuthID = Column(VARCHAR(128))
    AuthPassword = Column(VARCHAR(128))
    GetStatusURL = Column(VARCHAR(509))
    ConfigurationURL = Column(VARCHAR(509))
    ScanNowURL = Column(VARCHAR(509))
    CommandURL = Column(VARCHAR(509))
    AgentIPList = Column(VARCHAR(1024))
    AgentVer = Column(VARCHAR(39))
