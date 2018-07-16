from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbBlacklistRESTRegisterProductList(Base):
    __tablename__ = 'tb_BlacklistRESTRegisterProductList'
    id = Column(BIGINT, primary_key=True, nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    ProductName = Column(NVARCHAR(256), nullable=False)
    HostName = Column(NVARCHAR(256), nullable=False)
    lutontmcm = Column(DATETIME, nullable=False)
    LatestQueryID = Column(INTEGER)
    LatestQueryUTCTime = Column(DATETIME)
    SourceID = Column(VARCHAR(16))
