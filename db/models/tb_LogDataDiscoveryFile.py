from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbLogDataDiscoveryFile(Base):
    __tablename__ = 'tb_LogDataDiscoveryFile'
    id = Column(INTEGER, primary_key=True, nullable=False)
    SLF_FileLogID = Column(VARCHAR(36), nullable=False)
    SLF_Filename = Column(NVARCHAR(256))
    SLF_FilePath = Column(NVARCHAR(256))
    SLF_FileSize = Column(INTEGER)
    SLF_FileType = Column(INTEGER)
    SLF_ResultCode = Column(INTEGER)
    SLF_Checksum = Column(VARCHAR(36))
    SLF_LastUpdateTime = Column(DATETIME)
