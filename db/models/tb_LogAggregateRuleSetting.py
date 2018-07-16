from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, UNIQUEIDENTIFIER, VARCHAR


class TbLogAggregateRuleSetting(Base):
    __tablename__ = 'tb_LogAggregateRuleSetting'
    id = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    RuleID = Column(UNIQUEIDENTIFIER, nullable=False)
    LogID = Column(INTEGER, nullable=False)
    LogSetting = Column(VARCHAR(3072), nullable=False)
