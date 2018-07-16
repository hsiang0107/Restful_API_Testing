from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbResourceACL(Base):
    __tablename__ = 'tb_ResourceACL'
    AccountGuid = Column(CHAR(36), primary_key=True, nullable=False)
    ResourceGuid = Column(CHAR(36), primary_key=True, nullable=False)
    Type = Column(INTEGER, nullable=False)
    Permission = Column(INTEGER, nullable=False)
