from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR


class TbCommandTracking(Base):
    __tablename__ = 'tb_CommandTracking'
    CT_ID = Column(CHAR(36), primary_key=True, nullable=False)
    CT_MotherID = Column(CHAR(36))
    CT_TargetGroup = Column(INTEGER, nullable=False)
    CT_ReceiverID = Column(CHAR(36), nullable=False)
    CT_UserAccessID = Column(NVARCHAR(64))
    CT_MessageID = Column(INTEGER, nullable=False)
    CT_TriggerTime = Column(DATETIME, nullable=False)
    CT_UpdateTime = Column(DATETIME, nullable=False)
    CT_TotalCommandItems = Column(INTEGER, nullable=False)
    CT_TotalSuccess = Column(INTEGER, nullable=False)
    CT_ErrorDescription = Column(NVARCHAR(1024))
    CT_Location = Column(NVARCHAR(254))
    CT_Parameters = Column(NVARCHAR(1024))
    CT_CommandData = Column(IMAGE)
    CT_TotalFailure = Column(INTEGER, nullable=False)
