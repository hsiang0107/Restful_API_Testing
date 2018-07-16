from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbADCustomSiteInfo(Base):
    __tablename__ = 'tb_AD_CustomSiteInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    SiteID = Column(CHAR(36), nullable=False)
    SiteName = Column(NVARCHAR(1024))
    Type = Column(SMALLINT, nullable=False)
    Color = Column(NVARCHAR(10))
    MergedSiteID = Column(CHAR(36))
    Location = Column(NVARCHAR(1024))
    Subnet = Column(VARCHAR(43))
    LastModificationTime = Column(DATETIME)
    CreatorGuid = Column(CHAR(36))
    IPv6Start = Column(BINARY(16))
    IPv6End = Column(BINARY(16))
