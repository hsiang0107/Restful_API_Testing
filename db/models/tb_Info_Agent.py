from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, CHAR, INTEGER, SMALLINT, VARCHAR


class TbInfoAgent(Base):
    __tablename__ = 'tb_Info_Agent'
    id = Column(INTEGER, primary_key=True, nullable=False)
    AgentGuid = Column(CHAR(36), nullable=False)
    AgentType = Column(SMALLINT)
    Status = Column(INTEGER)
    AgentToken = Column(VARCHAR(1024))
    PollingFrequency = Column(INTEGER)
    HeartbeatFrequency = Column(INTEGER)
    LastHeartbeatTime = Column(INTEGER)
    Offhour = Column(BINARY(12))
    AgentVersion = Column(VARCHAR(32))
    AgentBuild = Column(VARCHAR(32))
