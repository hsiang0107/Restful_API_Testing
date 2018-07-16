from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbsCloudScopeChangeDetail(Base):
    __tablename__ = 'tb_sCloudScopeChangeDetail'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ChangeID = Column(UNIQUEIDENTIFIER, nullable=False)
    EntityID = Column(VARCHAR(36), nullable=False)
    ActionType = Column(SMALLINT, nullable=False)
