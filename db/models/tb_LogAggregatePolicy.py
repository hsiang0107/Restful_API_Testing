from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER, NVARCHAR, UNIQUEIDENTIFIER


class TbLogAggregatePolicy(Base):
    __tablename__ = 'tb_LogAggregatePolicy'
    RuleID = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    Name = Column(NVARCHAR(256), nullable=False)
    Comment = Column(NVARCHAR(1024))
    Priority = Column(INTEGER, nullable=False)
    Enabled = Column(BIT, nullable=False)
