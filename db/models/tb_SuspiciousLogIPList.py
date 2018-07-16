from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbSuspiciousLogIPList(Base):
    __tablename__ = 'tb_SuspiciousLogIPList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ProductGUID = Column(CHAR(36))
    InterestedIP = Column(VARCHAR(15))
    HostName = Column(VARCHAR(256))
    Group = Column(NVARCHAR(128))
    LastestDetectionTime_H = Column(DATETIME)
    LastestDetectionTime_HM = Column(DATETIME)
    LastestDetectionTime_HML = Column(DATETIME)
    LastestDetectionTime_HMLI = Column(DATETIME)
