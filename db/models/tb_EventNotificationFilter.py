from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER, VARCHAR


class TbEventNotificationFilter(Base):
    __tablename__ = 'tb_EventNotificationFilter'
    USER_ID = Column(VARCHAR(38), primary_key=True)
    GROUP_ID = Column(VARCHAR(38))
    Event_ID = Column(VARCHAR(64))
    Enabled = Column(BIT)
    Category = Column(VARCHAR(32))
    FuncFilename = Column(VARCHAR(128))
    EditFilename = Column(VARCHAR(128))
    ComponentID = Column(VARCHAR(64))
    Site = Column(VARCHAR(64))
    Result = Column(INTEGER)
