from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, DATETIME, INTEGER


class TbSystemPolicy(Base):
    __tablename__ = 'tb_SystemPolicy'
    SP_TotalPolicyMode = Column(INTEGER, primary_key=True)
    SP_PolicyEnforcerActive = Column(BIT)
    SP_PolicyEnforcerMode = Column(INTEGER)
    SP_PolicyEnforcerLastActTime = Column(DATETIME)
    SP_PolicyEnforcerLastDueTime = Column(DATETIME)
