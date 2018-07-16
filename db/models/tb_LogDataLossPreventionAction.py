from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbLogDataLossPreventionAction(Base):
    __tablename__ = 'tb_LogDataLossPreventionAction'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    SLF_Action = Column(INTEGER)
