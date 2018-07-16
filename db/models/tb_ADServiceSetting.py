from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbADServiceSetting(Base):
    __tablename__ = 'tb_ADServiceSetting'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ServerName = Column(NVARCHAR(256), nullable=False)
    ServerURL = Column(VARCHAR(2048), nullable=False)
    Port = Column(INTEGER, nullable=False)
    IsHTTPS = Column(BIT)
    Username = Column(VARCHAR(32))
    Password = Column(VARCHAR(256))
    ServerType = Column(SMALLINT, nullable=False)
    ServerVersion = Column(VARCHAR(16))
    IntervalInHours = Column(SMALLINT)
    LastUpdateTime = Column(DATETIME)
    IsEnable = Column(BIT)
    FailType = Column(SMALLINT)
    RootDomains = Column(NVARCHAR)
