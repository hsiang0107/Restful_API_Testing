from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER


class TbInValidLog(Base):
    __tablename__ = 'tb_InValidLog'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    MsgID = Column(INTEGER)
    TL_ProductType = Column(INTEGER, nullable=False)
    CLF_LogReceivedTime = Column(DATETIME)
    TL_LogData = Column(IMAGE)
    TL_IsRetriveFlag = Column(INTEGER)
    TL_Priority = Column(INTEGER)
    TL_ParentID = Column(CHAR(36))
