from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER


class TbVirusOutbreakNotifHistory(Base):
    __tablename__ = 'tb_VirusOutbreakNotifHistory'
    id = Column(INTEGER, primary_key=True, nullable=False)
    lastnotifytime = Column(DATETIME, nullable=False)
