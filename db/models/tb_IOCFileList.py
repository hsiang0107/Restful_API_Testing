from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbIOCFileList(Base):
    __tablename__ = 'tb_IOCFileList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    IOC_GUID = Column(CHAR(36))
    FileHashID = Column(VARCHAR(64))
    FileName = Column(NVARCHAR(256))
    Author = Column(NVARCHAR(256))
    AuthoredUTCTime = Column(DATETIME)
    ShortDesc = Column(NVARCHAR(1024))
    Description = Column(NVARCHAR(1024))
    FileContent_BASE64 = Column(VARCHAR)
    UploadedTime = Column(DATETIME)
    UploadedFrom = Column(INTEGER)
    UploadedBy = Column(NVARCHAR(256))
    ExtractingStatus = Column(INTEGER)

    @classmethod
    def find_by_file_hash_id(cls, hash_id):
        return cm_session.query(cls).filter(cls.FileHashID == hash_id).first()
