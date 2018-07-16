from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT


class TbDwellTimeDetail(Base):
    __tablename__ = 'tb_DwellTimeDetail'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MachineGUID = Column(CHAR(36), nullable=False)
    DwellTimeInfoID = Column(INTEGER, nullable=False)
    TaskGUID = Column(CHAR(36))
    ServerGUID = Column(CHAR(36))
    ClientGUID = Column(CHAR(36))
    FileFullPathName = Column(NVARCHAR(261))
    FirstObsUTCTime = Column(DATETIME)
    Remediation = Column(SMALLINT)
    LogGenLocalTime = Column(DATETIME)
    DismissedACName = Column(NVARCHAR(256))
    DismissedTime = Column(DATETIME)
    CreateTime = Column(DATETIME, nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
