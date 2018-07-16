from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, VARCHAR


class TbstatuslogjournalPLS(Base):
    __tablename__ = 'tb_statuslogjournalPLS'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36))
    SLF_ProductID = Column(INTEGER)
    SLF_PropertyID = Column(INTEGER)
    SLF_PluginServiceID = Column(INTEGER)
    SLF_Version = Column(VARCHAR(19))
    SLF_Status = Column(INTEGER)
    SLF_LastUpdateTime = Column(DATETIME)
    SLF_LastCompliantState = Column(BIGINT)
