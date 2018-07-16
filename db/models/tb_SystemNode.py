from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbSystemNode(Base):
    __tablename__ = 'tb_SystemNode'
    Guid = Column(CHAR(36), primary_key=True, nullable=False)
    Type = Column(INTEGER, nullable=False)
