from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbSpecialVirusNotifHistory(Base):
    __tablename__ = 'tb_SpecialVirusNotifHistory'
    id = Column(INTEGER, primary_key=True, nullable=False)
    VLF_VirusName = Column(VARCHAR(64), nullable=False)
    lastnotifytime = Column(DATETIME, nullable=False)
