from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbChildSystemPatternList(Base):
    __tablename__ = 'tb_ChildSystemPatternList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    CSPL_SystemID = Column(CHAR(36), nullable=False)
    CSPL_PatternID = Column(INTEGER, nullable=False)
    CSPL_PatternVersion = Column(VARCHAR(19), nullable=False)
    CSPL_PatternUpdate = Column(DATETIME, nullable=False)
