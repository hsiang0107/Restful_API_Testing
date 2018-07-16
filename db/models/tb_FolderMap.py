from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbFolderMap(Base):
    __tablename__ = 'tb_FolderMap'
    folder_id = Column(INTEGER, primary_key=True, nullable=False)
    folder_path = Column(NVARCHAR(450))
    cm_guid = Column(CHAR(36), nullable=False)
    lastupdatetime = Column(DATETIME(36))
