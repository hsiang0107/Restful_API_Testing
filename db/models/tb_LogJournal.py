from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbLogJournal(Base):
    __tablename__ = 'tb_LogJournal'
    id = Column(INTEGER, primary_key=True, nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    PdtType = Column(INTEGER, nullable=False)
    MsgType = Column(INTEGER, nullable=False)
    MinorVer = Column(INTEGER, nullable=False)
    ComponentID = Column(INTEGER, nullable=False)
    ComponentType = Column(INTEGER, nullable=False)
    lut = Column(DATETIME, nullable=False)
