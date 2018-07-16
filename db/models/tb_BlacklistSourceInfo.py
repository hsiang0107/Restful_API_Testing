from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, INTEGER, NVARCHAR, VARCHAR


class TbBlacklistSourceInfo(Base):
    __tablename__ = 'tb_BlacklistSourceInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Key = Column(VARCHAR(256), nullable=False)
    FileHashID = Column(VARCHAR(64))
    Source = Column(INTEGER, nullable=False)
    UploadedBy = Column(VARCHAR(256))
    FileName = Column(NVARCHAR(256))

    @classmethod
    def find_by_key(cls, slf_key):
        return cm_session.query(cls).filter(cls.SLF_Key == slf_key).first()
