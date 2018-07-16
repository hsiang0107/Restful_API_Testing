from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbAccountResourceRelation(Base):
    __tablename__ = 'tb_AccountResourceRelation'
    AccountGuid = Column(CHAR(36), primary_key=True, nullable=False)
    ResourceGuid = Column(CHAR(36), primary_key=True, nullable=False)
    Permission = Column(INTEGER, nullable=False)
