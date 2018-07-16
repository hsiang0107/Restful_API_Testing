from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbLogDataLossPreventionActionCasStorage(Base):
    __tablename__ = 'tb_LogDataLossPreventionAction_CasStorage'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    SLF_Action = Column(INTEGER)
