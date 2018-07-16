from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbSpecialVirusSummary(Base):
    __tablename__ = 'tb_SpecialVirusSummary'
    id = Column(INTEGER, primary_key=True, nullable=False)
    wholemin = Column(DATETIME, nullable=False)
    VLF_VirusName = Column(VARCHAR(64), nullable=False)
    cnt = Column(INTEGER, nullable=False)
