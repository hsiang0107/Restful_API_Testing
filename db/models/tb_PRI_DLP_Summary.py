from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbPRIDLPSummary(Base):
    __tablename__ = 'tb_PRI_DLP_Summary'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ClientGuid = Column(CHAR(36), nullable=False)
    LastScanEndTime = Column(DATETIME)
    ViolationCount = Column(INTEGER)
