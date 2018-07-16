from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, NVARCHAR, SMALLINT, VARCHAR


class Tbstatuslogjournalpolicy(Base):
    __tablename__ = 'tb_statuslogjournalpolicy'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36))
    PolicyGUID = Column(CHAR(36))
    PolicyType = Column(VARCHAR(32))
    PolicyStatus = Column(SMALLINT)
    UserID = Column(NVARCHAR(256))
    LastUpdateUTCTime = Column(DATETIME)
