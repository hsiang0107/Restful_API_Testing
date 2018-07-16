from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbLogDataDiscoveryFileAction(Base):
    __tablename__ = 'tb_LogDataDiscoveryFileAction'
    SLF_JobID = Column(CHAR(36), primary_key=True, nullable=False)
    SLF_FileLogID = Column(VARCHAR(36), nullable=False)
    SLF_Action = Column(INTEGER)
