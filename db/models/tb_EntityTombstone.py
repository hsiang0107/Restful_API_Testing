from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME


class TbEntityTombstone(Base):
    __tablename__ = 'tb_EntityTombstone'
    EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    LastUpdateTime = Column(DATETIME)
