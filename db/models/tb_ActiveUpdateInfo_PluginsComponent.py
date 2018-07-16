from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbActiveUpdateInfoPluginsComponent(Base):
    __tablename__ = 'tb_ActiveUpdateInfo_PluginsComponent'
    id = Column(VARCHAR(36), primary_key=True, nullable=False)
    ProductID = Column(INTEGER)
    ComponentAUType = Column(INTEGER)
    ComponentAUID = Column(INTEGER)
    ComponentPlatform = Column(INTEGER)
    ComponentLanguage = Column(INTEGER)
