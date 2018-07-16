from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, UNIQUEIDENTIFIER, VARCHAR


class TbsCloudPolicyTask(Base):
    __tablename__ = 'tb_sCloudPolicyTask'
    id = Column(INTEGER, primary_key=True, nullable=False)
    PolicyTaskID = Column(UNIQUEIDENTIFIER, nullable=False)
    PolicyID = Column(UNIQUEIDENTIFIER, nullable=False)
    Context = Column(VARCHAR(1024))
    CreationTime = Column(DATETIME, nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
    Result = Column(INTEGER, nullable=False)
    ResultDescription = Column(NVARCHAR(2048))
