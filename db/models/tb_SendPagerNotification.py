from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER, VARCHAR


class TbSendPagerNotification(Base):
    __tablename__ = 'tb_SendPagerNotification'
    USER_ID = Column(VARCHAR(38), primary_key=True)
    Event_ID = Column(VARCHAR(64), primary_key=True)
    ComponentID = Column(VARCHAR(64))
    EnableNotification = Column(BIT)
    PagerMessage = Column(VARCHAR(1024))
    SeledUGList = Column(VARCHAR(1024))
    Result = Column(INTEGER)
