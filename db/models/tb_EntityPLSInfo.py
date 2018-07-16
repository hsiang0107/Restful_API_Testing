from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, VARCHAR


class TbEntityPLSInfo(Base):
    __tablename__ = 'tb_EntityPLSInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    EntityID = Column(CHAR(36), nullable=False)
    ProductID = Column(VARCHAR(21), nullable=False)
    ProductType = Column(INTEGER, nullable=False)
    PropertyID = Column(INTEGER, nullable=False)
    PluginServiceID = Column(INTEGER, nullable=False)
    Version = Column(VARCHAR(19))
    Status = Column(INTEGER)
    LastUpdateTime = Column(DATETIME)
    LastCompliantState = Column(BIGINT)
