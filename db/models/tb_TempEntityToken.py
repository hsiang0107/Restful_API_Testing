from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, VARCHAR


class TbTempEntityToken(Base):
    __tablename__ = 'tb_TempEntityToken'
    GUID = Column(CHAR(36), primary_key=True, nullable=False)
    Token = Column(VARCHAR(255), nullable=False)
