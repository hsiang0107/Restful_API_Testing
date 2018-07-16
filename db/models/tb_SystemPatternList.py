from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbSystemPatternList(Base):
    __tablename__ = 'tb_SystemPatternList'
    PI_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    PI_PatternType = Column(INTEGER, primary_key=True)
    PI_PatternVersion = Column(VARCHAR(19), primary_key=True)
    PI_PatternLastUpdateTime = Column(DATETIME)
