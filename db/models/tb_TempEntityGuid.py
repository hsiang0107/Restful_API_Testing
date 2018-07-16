from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR


class TbTempEntityGuid(Base):
    __tablename__ = 'tb_TempEntityGuid'
    GUID = Column(CHAR(36), primary_key=True, nullable=False)
