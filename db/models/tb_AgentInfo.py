from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbAgentInfo(Base):
    __tablename__ = 'tb_AgentInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    AI_AgentID = Column(CHAR(36), nullable=False)
    AI_EntityID = Column(CHAR(36), nullable=False)
