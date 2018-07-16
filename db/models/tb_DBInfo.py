from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, VARCHAR


class TbDBInfo(Base):
    __tablename__ = 'tb_DBInfo'
    DB_Version = Column(VARCHAR(38), primary_key=True)
    DB_UpdateTime = Column(DATETIME)
