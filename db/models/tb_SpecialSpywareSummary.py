from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbSpecialSpywareSummary(Base):
    __tablename__ = 'tb_SpecialSpywareSummary'
    id = Column(INTEGER, primary_key=True, nullable=False)
    wholemin = Column(DATETIME, nullable=False)
    VirusName = Column(VARCHAR(64), nullable=False)
    cnt = Column(INTEGER, nullable=False)
