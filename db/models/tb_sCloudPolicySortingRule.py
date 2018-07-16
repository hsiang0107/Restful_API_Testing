from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbsCloudPolicySortingRule(Base):
    __tablename__ = 'tb_sCloudPolicySortingRule'
    id = Column(INTEGER, primary_key=True, nullable=False)
    RuleID = Column(UNIQUEIDENTIFIER, nullable=False)
    PolicyID = Column(CHAR(36), nullable=False)
    SortingSequence = Column(SMALLINT)
    RuleForUI = Column(NVARCHAR, nullable=False)
    RuleForQuery = Column(NVARCHAR, nullable=False)
    LastUpdateUTCTime = Column(DATETIME)
    UserGuid = Column(CHAR(36), nullable=False)
    PolicyType = Column(VARCHAR(32), nullable=False)
