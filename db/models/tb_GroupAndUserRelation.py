from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import VARCHAR


class TbGroupAndUserRelation(Base):
    __tablename__ = 'tb_GroupAndUserRelation'
    GROUP_ID = Column(VARCHAR(64), primary_key=True)
    USER_ID = Column(VARCHAR(64), primary_key=True)
