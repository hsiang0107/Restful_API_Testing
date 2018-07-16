from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BIT, CHAR, INTEGER, NVARCHAR, VARCHAR


class TbLogFile(Base):
    __tablename__ = 'tb_LogFile'
    CMGuid = Column(CHAR(36))
    id = Column(INTEGER, nullable=False)
    FileExt = Column(VARCHAR(512))
    FileName = Column(NVARCHAR(512))
    FileNameInArchive = Column(NVARCHAR(512))
    FileSize = Column(INTEGER)
    HasQFile = Column(BIT)
    MD5 = Column(VARCHAR(36))
    QFilePath = Column(NVARCHAR(512))
    SharedFolder = Column(VARCHAR(1024))
    TrueFileType = Column(VARCHAR(64))
    TrueFileTypeDescription = Column(NVARCHAR(64))
    MsgLogID = Column(CHAR(36))
    SeqID = Column(BIGINT, primary_key=True, nullable=False)
    SHA1 = Column(VARCHAR(40))
    SHA1inArc = Column(VARCHAR(40))
    FileTypeInArc = Column(VARCHAR(64))
