from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, VARCHAR


class TbRedAlertHistory(Base):
    __tablename__ = 'tb_RedAlertHistory'
    RAH_RedAlertID = Column(CHAR(36), primary_key=True, nullable=False)
    RAH_VirusCountResult = Column(VARCHAR(3074))
    RAH_StatusResult = Column(VARCHAR(512))
