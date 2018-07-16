from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, UNIQUEIDENTIFIER, VARCHAR


class TbsCloudScope(Base):
    __tablename__ = 'tb_sCloudScope'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ProductID = Column(VARCHAR(12), nullable=False)
    ScopeID = Column(UNIQUEIDENTIFIER, nullable=False)
    DisplayName = Column(NVARCHAR(256), nullable=False)
    Description = Column(NVARCHAR(1024))
    UserID = Column(VARCHAR(256))
    CreationTime = Column(DATETIME, nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
