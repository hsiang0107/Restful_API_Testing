from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbLogDataDiscoveryDevice(Base):
    __tablename__ = 'tb_LogDataDiscoveryDevice'
    id = Column(INTEGER, primary_key=True, nullable=False)
    SLF_ClientGUID = Column(CHAR(36))
    SLF_DeviceClassName = Column(NVARCHAR(256))
    SLF_DeviceDisplayName = Column(NVARCHAR(256))
    SLF_GUID = Column(CHAR(36))
    SLF_DeviceDisablable = Column(INTEGER)
    SLF_DeviceProvider = Column(NVARCHAR(256))
    SLF_DeviceHidden = Column(INTEGER)
    SLF_DeviceDisabled = Column(INTEGER)
    SLF_DeviceStarted = Column(INTEGER)
    SLF_LastScanTime = Column(DATETIME)
