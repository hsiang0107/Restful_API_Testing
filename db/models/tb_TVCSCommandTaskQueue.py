from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbTVCSCommandTaskQueue(Base):
    __tablename__ = 'tb_TVCSCommandTaskQueue'
    TSK_CommandItemID = Column(CHAR(36), primary_key=True)
    TSK_CommandID = Column(CHAR(36))
    TSK_ProductType = Column(VARCHAR(255))
    TSK_GenDateTime = Column(DATETIME)
    TSK_Processed = Column(INTEGER)
    TSK_EntityID = Column(CHAR(36))
    TSK_Token = Column(VARCHAR(1024))
