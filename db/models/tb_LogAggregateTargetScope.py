from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, UNIQUEIDENTIFIER


class TbLogAggregateTargetScope(Base):
    __tablename__ = 'tb_LogAggregateTargetScope'
    id = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    RuleID = Column(UNIQUEIDENTIFIER, nullable=False)
    NodeID = Column(CHAR(36), nullable=False)
    NodeType = Column(INTEGER, nullable=False)
