from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, INTEGER, NVARCHAR


class TbUserInfo(Base):
    __tablename__ = 'tb_UserInfo'
    UserGuid = Column(CHAR(36), primary_key=True, nullable=False)
    Password = Column(NVARCHAR(256))
    MailAddress = Column(NVARCHAR(256))
    PagerNumber = Column(NVARCHAR(256))
    PhoneNumber = Column(NVARCHAR(256))
    MobilePhoneNumber = Column(NVARCHAR(256))
    MSN = Column(NVARCHAR(256))
    LastLoginTime = Column(DATETIME)
    IsActivate = Column(BIT)
    RowsPerPage = Column(INTEGER)
    LoginFailedTimes = Column(INTEGER)
    LoginBlockedTime = Column(DATETIME)
    LoginView = Column(INTEGER)
    TwoFASecretToken = Column(NVARCHAR(256))
