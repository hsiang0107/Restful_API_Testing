from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class Tbosceclients(Base):
    __tablename__ = 'tb_osceclients'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Guid = Column(CHAR(36))
    ParentGuid = Column(CHAR(36))
    CMGuid = Column(CHAR(36))
