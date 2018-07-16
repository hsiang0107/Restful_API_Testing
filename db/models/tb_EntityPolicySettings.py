from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER


class TbEntityPolicySettings(Base):
    __tablename__ = 'tb_EntityPolicySettings'
    PS_FolderID = Column(INTEGER, primary_key=True, nullable=False)
    PS_CurrentPolicyMode = Column(INTEGER)
    PS_PreviousPolicyMode = Column(INTEGER)
    PS_AcceptSmartPolicyEnforcer = Column(BIT)
