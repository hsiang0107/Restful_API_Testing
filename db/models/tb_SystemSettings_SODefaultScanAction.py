from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER


class TbSystemSettingsSODefaultScanAction(Base):
    __tablename__ = 'tb_SystemSettings_SODefaultScanAction'
    id = Column(INTEGER, primary_key=True, nullable=False)
    SOType = Column(INTEGER, nullable=False)
    RiskLevel = Column(INTEGER, nullable=False)
    ScanAction = Column(INTEGER, nullable=False)
    ApplyTo = Column(INTEGER, nullable=False)
