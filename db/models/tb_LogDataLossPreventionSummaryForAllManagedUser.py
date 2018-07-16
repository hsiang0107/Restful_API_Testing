from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbLogDataLossPreventionSummaryForAllManagedUser(Base):
    __tablename__ = 'tb_LogDataLossPreventionSummaryForAllManagedUser'
    id = Column(INTEGER, primary_key=True, nullable=False)
    UserGuid = Column(CHAR(36))
    UserName = Column(NVARCHAR(64))
    Domain = Column(NVARCHAR(256))
    Date = Column(DATETIME, nullable=False)
    SeverityCode = Column(INTEGER, nullable=False)
    Status = Column(INTEGER, nullable=False)
    Count = Column(INTEGER, nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
