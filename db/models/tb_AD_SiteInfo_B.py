from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, CHAR, INTEGER, NVARCHAR, VARCHAR


class TbADSiteInfoB(Base):
    __tablename__ = 'tb_AD_SiteInfo_B'
    id = Column(INTEGER, primary_key=True, nullable=False)
    SiteID = Column(CHAR(36))
    SiteDefaultName = Column(NVARCHAR(1024))
    SiteName = Column(NVARCHAR(1024))
    Color = Column(NVARCHAR(10))
    MergedSiteID = Column(CHAR(36))
    Location = Column(NVARCHAR(1024))
    Subnet = Column(VARCHAR(43), nullable=False)
    IPv6Start = Column(BINARY(16))
    IPv6End = Column(BINARY(16))
    RootDomain = Column(NVARCHAR(256))
