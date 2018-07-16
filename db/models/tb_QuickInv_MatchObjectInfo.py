from sqlalchemy import Column, and_
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, BINARY, NVARCHAR, SMALLINT, VARCHAR, TINYINT
from db import TbEntityInfo


class TbQuickInvMatchObjectInfo(Base):
    __tablename__ = 'tb_QuickInv_MatchObjectInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    AgentID = Column(CHAR(36), nullable=False)
    SLF_Key = Column(VARCHAR(256), nullable=False)
    RetroScanData_MD5 = Column(BINARY(16), nullable=False)
    RetroScanCategory = Column(TINYINT, nullable=False)
    MetaValue = Column(NVARCHAR(2048))
    MetaCategory = Column(SMALLINT)
    FirstSeenUTCTime = Column(DATETIME)
    RCAScanID = Column(CHAR(36))
    FileFullPath = Column(NVARCHAR(512))
    FileCreationUTCTime = Column(DATETIME)
    LastUpdateTime = Column(DATETIME)

    @classmethod
    def find_by_slf_key_and_agent(cls, key, agent):
        agent_guid = TbEntityInfo.find_by_machine_name(agent).EI_EntityID
        return cm_session.query(cls).filter(and_(cls.SLF_Key == key, cls.AgentID == agent_guid)).first()
