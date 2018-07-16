from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbsCloudPolicyScopeDetail(Base):
    __tablename__ = 'tb_sCloudPolicyScopeDetail'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ScopeID = Column(UNIQUEIDENTIFIER, nullable=False)
    ScopeType = Column(SMALLINT, nullable=False)
    ScopeValue = Column(VARCHAR(256), nullable=False)
