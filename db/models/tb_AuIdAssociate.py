from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbAuIdAssociate(Base):
    __tablename__ = 'tb_AuIdAssociate'
    id = Column(CHAR(36), primary_key=True, nullable=False)
    ComponentType = Column(INTEGER, primary_key=True)
    ComponentID = Column(INTEGER, primary_key=True)
    Language = Column(INTEGER, primary_key=True)
    Platform = Column(INTEGER)
