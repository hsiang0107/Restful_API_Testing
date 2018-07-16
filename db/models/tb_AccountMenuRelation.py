from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbAccountMenuRelation(Base):
    __tablename__ = 'tb_AccountMenuRelation'
    accguid = Column(CHAR(36), primary_key=True, nullable=False)
    menuid = Column(VARCHAR(10), primary_key=True, nullable=False)
    permission = Column(INTEGER)
