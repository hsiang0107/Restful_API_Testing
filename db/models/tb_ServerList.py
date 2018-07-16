from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbServerList(Base):
    __tablename__ = 'tb_ServerList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ServerID = Column(CHAR(36))
    ServerName = Column(VARCHAR(2048))
    DisplayName = Column(NVARCHAR(64))
    ProductID = Column(VARCHAR(12))
    ProductVersion = Column(VARCHAR(19))
    Type = Column(SMALLINT, nullable=False)
    Protocol = Column(VARCHAR(12))
    Host = Column(NVARCHAR(256), nullable=False)
    Port = Column(INTEGER, nullable=False)
    Username = Column(NVARCHAR(256))
    Password = Column(NVARCHAR(256))
    Others = Column(NVARCHAR(512))
    Status = Column(INTEGER)
    IsEnableDelete = Column(SMALLINT)
    IsEnableProxy = Column(SMALLINT)
    ProxyID = Column(CHAR(36))
    LastUpdateTime = Column(DATETIME)
    CreatedUserID = Column(VARCHAR(256))
    GlobalRetroScanAggregated = Column(BIT)
    GlobalRetroScanSubscribed = Column(BIT)
    APIKey = Column(CHAR(36))
    DeployedDDAnID = Column(INTEGER)

    @classmethod
    def find_by_serverid(cls, serverid):
        return cm_session.query(cls).filter(cls.ServerID == serverid).first()

    @classmethod
    def find_by_displayname(cls, displayname):
        return cm_session.query(cls).filter(cls.DisplayName == displayname).first()

    def __str__(self):
        return "tb_ServerList DisplayName is %s" % self.DisplayName
