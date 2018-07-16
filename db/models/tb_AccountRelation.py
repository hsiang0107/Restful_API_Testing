from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR


class TbAccountRelation(Base):
    __tablename__ = 'tb_AccountRelation'
    UserGuid = Column(CHAR(36), primary_key=True, nullable=False)
    AccountGuid = Column(CHAR(36), primary_key=True, nullable=False)
