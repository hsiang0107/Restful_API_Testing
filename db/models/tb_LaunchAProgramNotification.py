from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER, NVARCHAR, VARCHAR


class TbLaunchAProgramNotification(Base):
    __tablename__ = 'tb_LaunchAProgramNotification'
    USER_ID = Column(VARCHAR(38))
    Event_ID = Column(VARCHAR(64), primary_key=True)
    ComponentID = Column(VARCHAR(64))
    EnableNotification = Column(BIT)
    Program = Column(NVARCHAR(1024))
    Parameters = Column(NVARCHAR(1024))
    SeledUGList = Column(VARCHAR(1024))
    Result = Column(INTEGER)
