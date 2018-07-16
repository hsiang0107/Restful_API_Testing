from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, NVARCHAR


class TbEntityPathInfo(Base):
    __tablename__ = 'tb_EntityPathInfo'
    EPI_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    EPI_FolderPath = Column(NVARCHAR(2048))
