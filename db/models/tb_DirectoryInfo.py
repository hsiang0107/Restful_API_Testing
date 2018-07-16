from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, NVARCHAR


class TbDirectoryInfo(Base):
    __tablename__ = 'tb_DirectoryInfo'
    AccountGuid = Column(CHAR(36), primary_key=True, nullable=False)
    ObjectGuid = Column(NVARCHAR(256), nullable=False)
    Domain = Column(NVARCHAR(256))
    BaseDN = Column(NVARCHAR(256))
