from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, NVARCHAR


class TbRCAMatchObjectJournal(Base):
    __tablename__ = 'tb_RCA_MatchObjectJournal'
    id = Column(BIGINT, primary_key=True, nullable=False)
    TaskID = Column(CHAR(36), nullable=False)
    AgentID = Column(CHAR(36), nullable=False)
    FileFullPath = Column(NVARCHAR(512))
    FileCreationUTCTime = Column(DATETIME)
