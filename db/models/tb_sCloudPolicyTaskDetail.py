from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbsCloudPolicyTaskDetail(Base):
    __tablename__ = 'tb_sCloudPolicyTaskDetail'
    id = Column(INTEGER, primary_key=True, nullable=False)
    PolicyTaskDetailID = Column(UNIQUEIDENTIFIER, nullable=False)
    PolicyID = Column(UNIQUEIDENTIFIER, nullable=False)
    PolicyTaskID = Column(UNIQUEIDENTIFIER, nullable=False)
    CreationTime = Column(DATETIME, nullable=False)
    ProgressState = Column(SMALLINT, nullable=False)
    TargetServer = Column(VARCHAR(36), nullable=False)
    TargetClients = Column(VARCHAR)
    ChangedClients = Column(VARCHAR)
    TargetDomains = Column(VARCHAR)
    LastUpdateTime = Column(DATETIME, nullable=False)
    PolicyType = Column(VARCHAR(32))
