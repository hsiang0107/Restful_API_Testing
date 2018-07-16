from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, SMALLINT, VARCHAR


class TbsCloudPolicySortingState(Base):
    __tablename__ = 'tb_sCloudPolicySortingState'
    id = Column(INTEGER, primary_key=True, nullable=False)
    PolicyType = Column(VARCHAR(32), nullable=False)
    LastResortUTCTime = Column(DATETIME, nullable=False)
    RunningState = Column(SMALLINT, nullable=False)
    TriggerResortFlag = Column(SMALLINT, nullable=False)
    RepeatCycleInSecs = Column(INTEGER, nullable=False)
    LastUpdateRuleID = Column(CHAR(36))
