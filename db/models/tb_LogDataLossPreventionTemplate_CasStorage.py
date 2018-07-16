from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR


class TbLogDataLossPreventionTemplateCasStorage(Base):
    __tablename__ = 'tb_LogDataLossPreventionTemplate_CasStorage'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    SLF_PolicyName = Column(NVARCHAR(256))
    SLF_Template = Column(NVARCHAR(256))
