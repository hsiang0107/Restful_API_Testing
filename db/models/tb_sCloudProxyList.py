from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbsCloudProxyList(Base):
    __tablename__ = 'tb_sCloudProxyList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ProxyID = Column(CHAR(36), nullable=False)
    DisplayName = Column(NVARCHAR(64), nullable=False)
    Protocol = Column(VARCHAR(12), nullable=False)
    ServerName = Column(VARCHAR(2048), nullable=False)
    Port = Column(INTEGER, nullable=False)
    UserID = Column(VARCHAR(256))
    Password = Column(VARCHAR(256))
    LastUpdateTime = Column(DATETIME, nullable=False)
    CreatedUserID = Column(VARCHAR(256), nullable=False)
