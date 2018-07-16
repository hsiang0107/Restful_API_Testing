from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbCriticalEventCategory(Base):
    __tablename__ = 'tb_CriticalEventCategory'
    id = Column(INTEGER, primary_key=True, nullable=False)
    CE_CategoryID = Column(VARCHAR(1))
    NameID = Column(VARCHAR(128))
    Priority = Column(INTEGER)
