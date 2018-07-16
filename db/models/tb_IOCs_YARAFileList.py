from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import NVARCHAR, INTEGER, VARCHAR, DATETIME


class TbIOCsYARAFileList(Base):
    __tablename__ = 'tb_IOCs_YARAFileList'
    FileHashID = Column(VARCHAR(64), primary_key=True, nullable=False)
    FileName = Column(NVARCHAR(256), nullable=False)
    FileContent_BASE64 = Column(VARCHAR, nullable=False)
    UploadedTime = Column(DATETIME)
    UploadedFrom = Column(INTEGER)
    UploadedBy = Column(NVARCHAR(256))
    ExtractingStatus = Column(INTEGER)

    @classmethod
    def find_by_file_hash_id(cls, hash_id):
        return cm_session.query(cls).filter(cls.FileHashID == hash_id).first()
