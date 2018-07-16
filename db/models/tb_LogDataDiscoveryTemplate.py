from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbLogDataDiscoveryTemplate(Base):
    __tablename__ = 'tb_LogDataDiscoveryTemplate'
    id = Column(INTEGER, primary_key=True, nullable=False)
    SLF_JobID = Column(CHAR(36), nullable=False)
    SLF_FileLogID = Column(VARCHAR(36), nullable=False)
    SLF_TemplateGuid = Column(CHAR(36), nullable=False)
    SLF_IdentifierGUID = Column(CHAR(36), nullable=False)
    SLF_IdentifierType = Column(INTEGER)
    SLF_MatchNumber = Column(INTEGER)
