from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR


class TbVASJobQueue(Base):
    __tablename__ = 'tb_VASJobQueue'
    VAS_JobQueueID = Column(INTEGER, primary_key=True, nullable=False)
    VAS_TaskID = Column(INTEGER, nullable=False)
    VAS_TaskName = Column(NVARCHAR(64))
    VAS_IssuedBy = Column(NVARCHAR(32))
    VAS_CleanAction = Column(INTEGER, nullable=False)
    VAS_Properties = Column(INTEGER, nullable=False)
    VAS_Priority = Column(INTEGER, nullable=False)
