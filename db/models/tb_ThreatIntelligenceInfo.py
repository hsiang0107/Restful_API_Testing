from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, SMALLINT


class TbThreatIntelligenceInfo(Base):
    __tablename__ = 'tb_ThreatIntelligenceInfo'
    DetectionName = Column(NVARCHAR(128), primary_key=True, nullable=False)
    Type = Column(SMALLINT, nullable=False)
    DataSource = Column(INTEGER, nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
    OverallRiskRating = Column(INTEGER, nullable=False)
    DamagePotential = Column(INTEGER, nullable=False)
    DistributionPotential = Column(INTEGER, nullable=False)
    InformationExposureRating = Column(INTEGER, nullable=False)
    ReportedInfection = Column(INTEGER, nullable=False)
