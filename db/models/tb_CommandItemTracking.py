from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbCommandItemTracking(Base):
    __tablename__ = 'tb_CommandItemTracking'
    CIT_ID = Column(CHAR(36), primary_key=True, nullable=False)
    CIT_ReceiverID = Column(CHAR(36), nullable=False)
    CIT_CommandID = Column(CHAR(36), nullable=False)
    CIT_MessageID = Column(INTEGER, nullable=False)
    CIT_TriggerTime = Column(DATETIME, nullable=False)
    CIT_UpdateTime = Column(DATETIME, nullable=False)
    CIT_Status = Column(INTEGER, nullable=False)
    CIT_ErrorDescription = Column(NVARCHAR(1024))
    CIT_Location = Column(NVARCHAR(254))
    CIT_Parameters = Column(NVARCHAR(1024))
