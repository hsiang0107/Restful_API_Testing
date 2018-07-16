from sqlalchemy import Column, and_
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, BIT, NVARCHAR, SMALLINT, VARCHAR
from db import TbEntityInfo


class TbRCATask(Base):
    __tablename__ = 'tb_RCA_Task'
    id = Column(BIGINT, primary_key=True, nullable=False)
    TaskID = Column(CHAR(36))
    ScanSummaryID = Column(CHAR(36))
    Criteria = Column(NVARCHAR(2048))
    CriteriaType = Column(SMALLINT)
    AgentID = Column(CHAR(36), nullable=False)
    ServerID = Column(CHAR(36))
    SLF_Key = Column(VARCHAR(256), nullable=False)
    Status = Column(SMALLINT)
    IsAffected = Column(BIT)
    IsSync = Column(BIT)
    CreationTime = Column(DATETIME)
    LastUpdateTime = Column(DATETIME)
    IsTimeout = Column(BIT)

    @classmethod
    def find_by_criteria_and_agent(cls, criteria, agent):
        agent_guid = TbEntityInfo.find_by_machine_name(agent).EI_EntityID
        return cm_session.query(cls).filter(and_(cls.Criteria == criteria, cls.AgentID == agent_guid)).first()

    @classmethod
    def find_by_criteria(cls, criteria):
        return cm_session.query(cls).filter(cls.Criteria == criteria).all()
