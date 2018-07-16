from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbLogSuspiciousFile(Base):
    __tablename__ = 'tb_LogSuspiciousFile'
    id = Column(INTEGER, nullable=False)
    MD5 = Column(VARCHAR(256), primary_key=True, nullable=False)
    FileName = Column(NVARCHAR(512))
    ContainerFolderName = Column(VARCHAR(256))
    LastRequestTime = Column(DATETIME)
    RetrievingStatus = Column(SMALLINT)
    UploadingStatus = Column(SMALLINT)
