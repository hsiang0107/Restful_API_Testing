from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, INTEGER


class TbTree(Base):
    __tablename__ = 'tb_Tree'
    id = Column(INTEGER, primary_key=True, nullable=False)
    stack_top = Column(INTEGER, nullable=False)
    Guid = Column(CHAR(36), nullable=False)
    LeftIndex = Column(BIGINT)
    RightIndex = Column(BIGINT)
    LeftGuid = Column(CHAR(36))
    RightGuid = Column(CHAR(36))
