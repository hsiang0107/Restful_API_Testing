from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, NVARCHAR, VARCHAR


class TbTempEntityPath(Base):
    __tablename__ = 'tb_TempEntityPath'
    GUID = Column(CHAR(36), primary_key=True, nullable=False)
    Token = Column(VARCHAR(255), nullable=False)
    Path = Column(NVARCHAR(255), nullable=False)
