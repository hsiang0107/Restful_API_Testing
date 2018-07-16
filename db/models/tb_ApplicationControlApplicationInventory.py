from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbApplicationControlApplicationInventory(Base):
    __tablename__ = 'tb_ApplicationControlApplicationInventory'
    SLF_ProductID = Column(INTEGER, nullable=False)
    SLF_CreateUTCDatetime = Column(DATETIME, nullable=False)
    SLF_ApplicationFileHash = Column(VARCHAR(40), primary_key=True, nullable=False)
    SLF_ApplicationFileType = Column(INTEGER)
    SLF_ApplicationDisplayName = Column(NVARCHAR(256))
    SLF_ApplicationOriginalFileName = Column(NVARCHAR(256))
    SLF_ApplicationFileVersion = Column(NVARCHAR(128))
    SLF_ApplicationFileSize = Column(BIGINT)
    SLF_ApplicationFileDescription = Column(NVARCHAR(256))
    SLF_ApplicationFileProductVersion = Column(NVARCHAR(128))
    SLF_ApplicationFileProductName = Column(NVARCHAR(256))
    SLF_ApplicationFileCopyright = Column(NVARCHAR(256))
    SLF_ApplicationFileLanguage = Column(NVARCHAR(32))
    SLF_ApplicationRequestedPriviledges = Column(VARCHAR(256))
    SLF_ApplicationFileSignatureIssuer = Column(NVARCHAR(1024))
    SLF_ApplicationFileSignatureSubject = Column(NVARCHAR(1024))
