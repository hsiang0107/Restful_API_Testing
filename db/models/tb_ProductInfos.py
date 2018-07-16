from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbProductInfos(Base):
    __tablename__ = 'tb_ProductInfos'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ProductType = Column(INTEGER, nullable=False)
    ProductID = Column(VARCHAR(256), nullable=False)
    ComponentType = Column(INTEGER)
    ComponentID = Column(INTEGER)
    TargetVersion = Column(VARCHAR(36))
    MenuVersion = Column(VARCHAR(36))
    ProductLanguage = Column(VARCHAR(36))
    ComponentLanguage = Column(INTEGER)
    ComponentProductID = Column(INTEGER)
    ComponentPlatform = Column(INTEGER)
