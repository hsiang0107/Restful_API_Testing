from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, NVARCHAR, SMALLINT


class TbQuickInvMatchObjectInfoJournal(Base):
    __tablename__ = 'tb_QuickInv_MatchObjectInfoJournal'
    id = Column(BIGINT, primary_key=True, nullable=False)
    TaskID = Column(CHAR(36), nullable=False)
    AgentID = Column(CHAR(36), nullable=False)
    MetaValue = Column(NVARCHAR(2048))
    MetaCategory = Column(SMALLINT)
    FirstSeenUTCTime = Column(DATETIME)
