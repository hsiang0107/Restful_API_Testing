from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbsCloudPolicy(Base):
    __tablename__ = 'tb_sCloudPolicy'
    id = Column(INTEGER, primary_key=True, nullable=False)
    PolicyID = Column(UNIQUEIDENTIFIER, nullable=False)
    DisplayName = Column(NVARCHAR(256), nullable=False)
    ScopeID = Column(UNIQUEIDENTIFIER)
    ProfileID = Column(UNIQUEIDENTIFIER, nullable=False)
    UserID = Column(VARCHAR(256))
    CreationTime = Column(DATETIME, nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
    LastModifyTime = Column(DATETIME)
    RepeatCycleInMins = Column(INTEGER, nullable=False)
    IsActivated = Column(SMALLINT, nullable=False)
    Context = Column(NVARCHAR(2048))
    LockFlag = Column(SMALLINT, nullable=False)
    isInherited = Column(SMALLINT)
    ParentPolicyID = Column(UNIQUEIDENTIFIER)
    Deviations = Column(INTEGER)
    PolicyVersion = Column(INTEGER)
    ModifierName = Column(VARCHAR(256))
    IsModified = Column(SMALLINT)
