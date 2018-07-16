from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, INTEGER, VARCHAR


class TbIOCsUDSOMap(Base):
    __tablename__ = 'tb_IOCs_UDSOMap'
    id = Column(BIGINT, primary_key=True, nullable=False)
    FileHashID = Column(VARCHAR(64), nullable=False)
    UDSOID = Column(VARCHAR(256), nullable=False)
    FileType = Column(INTEGER)
