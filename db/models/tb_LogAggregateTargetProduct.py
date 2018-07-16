from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, UNIQUEIDENTIFIER


class TbLogAggregateTargetProduct(Base):
    __tablename__ = 'tb_LogAggregateTargetProduct'
    id = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    RuleID = Column(UNIQUEIDENTIFIER, nullable=False)
    ProductType = Column(INTEGER, nullable=False)
