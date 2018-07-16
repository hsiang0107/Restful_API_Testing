from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR


class TbADProxyMailB(Base):
    __tablename__ = 'tb_AD_ProxyMail_B'
    id = Column(INTEGER, primary_key=True, nullable=False)
    GUID = Column(CHAR(36), nullable=False)
    Type = Column(INTEGER, nullable=False)
    Mail = Column(NVARCHAR(450))
    RootDomain = Column(NVARCHAR(256))
