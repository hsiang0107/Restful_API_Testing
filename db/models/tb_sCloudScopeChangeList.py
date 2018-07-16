from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, UNIQUEIDENTIFIER, VARCHAR


class TbsCloudScopeChangeList(Base):
    __tablename__ = 'tb_sCloudScopeChangeList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ChangeID = Column(UNIQUEIDENTIFIER, nullable=False)
    UserID = Column(UNIQUEIDENTIFIER)
    ProductID = Column(VARCHAR(12), nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
