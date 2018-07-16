from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR


class TbADAllUserTmpB(Base):
    __tablename__ = 'tb_AD_AllUserTmp_B'
    DN = Column(NVARCHAR, nullable=False)
    ObjGUID = Column(CHAR(36), primary_key=True, nullable=False)
    Domain = Column(NVARCHAR(256), nullable=False)
    SAMAccountName = Column(NVARCHAR(32), nullable=False)
    Type = Column(INTEGER, nullable=False)
    ManagerDN = Column(NVARCHAR)
    OuDN = Column(NVARCHAR)
    DisplayName = Column(NVARCHAR(256))
    AccountControl = Column(INTEGER)
    Sid = Column(NVARCHAR(256))
    RootDomain = Column(NVARCHAR(256))
