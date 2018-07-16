from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbSpecialSpywareNotifHistory(Base):
    __tablename__ = 'tb_SpecialSpywareNotifHistory'
    id = Column(INTEGER, primary_key=True, nullable=False)
    VirusName = Column(VARCHAR(64), nullable=False)
    lastnotifytime = Column(DATETIME, nullable=False)
