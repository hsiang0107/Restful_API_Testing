from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbUGNtfRelation(Base):
    __tablename__ = 'tb_UGNtfRelation'
    USER_ID = Column(VARCHAR(64), primary_key=True)
    Event_ID = Column(VARCHAR(64))
    ComponentID = Column(VARCHAR(64))
    UG_ID = Column(VARCHAR(64))
    TokenID = Column(VARCHAR(36))
    Result = Column(INTEGER)
