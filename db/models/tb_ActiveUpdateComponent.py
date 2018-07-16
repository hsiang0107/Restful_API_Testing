from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbActiveUpdateComponent(Base):
    __tablename__ = 'tb_ActiveUpdateComponent'
    id = Column(INTEGER, primary_key=True, nullable=False)
    StringID = Column(VARCHAR(128))
    ComponentType = Column(INTEGER)
    ComponentID = Column(INTEGER)
    Category = Column(VARCHAR(32))
