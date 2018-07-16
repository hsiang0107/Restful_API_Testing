from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbDDESScanResult(Base):
    __tablename__ = 'tb_DDES_ScanResult'
    id = Column(INTEGER, primary_key=True, nullable=False)
    TaskGUID = Column(CHAR(36))
    MachineGUID = Column(CHAR(36))
    ClientGUID = Column(CHAR(36))
    ServerGUID = Column(CHAR(36))
    IOC_GUID = Column(CHAR(36))
    MatchObj_Type = Column(VARCHAR(32))
    MatchObj_Data = Column(NVARCHAR(2048))
    SLF_Key = Column(VARCHAR(256))
    FileFullPathName = Column(NVARCHAR(261))
    FileCreationUTCTime = Column(DATETIME)
    FirstObsUTCTime = Column(DATETIME)
    LastUpdateTime = Column(DATETIME)
