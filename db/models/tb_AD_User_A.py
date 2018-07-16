from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbADUserA(Base):
    __tablename__ = 'tb_AD_User_A'
    GUID = Column(CHAR(36), primary_key=True, nullable=False)
    SAMAccountName = Column(NVARCHAR(32), nullable=False)
    Domain = Column(NVARCHAR(256), nullable=False)
    DomainAccount = Column(NVARCHAR(256), nullable=False)
    Type = Column(INTEGER, nullable=False)
    ManagerGUID = Column(CHAR(36))
    OuGUID = Column(CHAR(36))
    DisplayName = Column(NVARCHAR(256))
    AccountControl = Column(INTEGER)
    RootDomain = Column(NVARCHAR(256))
    CMLoginFailedTimes = Column(INTEGER)
    CMLoginBlockedTime = Column(DATETIME)
    CMLastLogonTime = Column(DATETIME)
    CM2FASecretToken = Column(NVARCHAR(256))
