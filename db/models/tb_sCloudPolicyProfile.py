from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, UNIQUEIDENTIFIER, VARCHAR


class TbsCloudPolicyProfile(Base):
    __tablename__ = 'tb_sCloudPolicyProfile'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ProfileID = Column(UNIQUEIDENTIFIER, nullable=False)
    DisplayName = Column(NVARCHAR(256))
    Settings = Column(NVARCHAR, nullable=False)
    ActivatedSettings = Column(NVARCHAR, nullable=False)
    ManagedSettings = Column(NVARCHAR)
    SettingDeviations = Column(NVARCHAR)
    ProductID = Column(VARCHAR(12), nullable=False)
    TemplateVersion = Column(VARCHAR(48), nullable=False)
    UserID = Column(VARCHAR(256))
    CreationTime = Column(DATETIME, nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
