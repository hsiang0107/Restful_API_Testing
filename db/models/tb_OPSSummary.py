from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbOPSSummary(Base):
    __tablename__ = 'tb_OPSSummary'
    VLF_VirusName = Column(VARCHAR(64), primary_key=True)
    VLF_GenerationTime = Column(DATETIME)
    VLF_VirusLogType = Column(INTEGER)
    VLF_Year = Column(INTEGER, nullable=False)
    VLF_Month = Column(INTEGER, nullable=False)
    VLF_Day = Column(INTEGER, nullable=False)
    VLF_Hour = Column(INTEGER, nullable=False)
    OPS_Count = Column(INTEGER, nullable=False)
    RA_ID = Column(CHAR(36))
