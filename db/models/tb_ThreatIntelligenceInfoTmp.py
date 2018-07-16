from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, SMALLINT


class TbThreatIntelligenceInfoTmp(Base):
    __tablename__ = 'tb_ThreatIntelligenceInfoTmp'
    DetectionName = Column(NVARCHAR(128), primary_key=True, nullable=False)
    Type = Column(SMALLINT, nullable=False)
    DataSource = Column(INTEGER)
    OverallRiskRating = Column(INTEGER)
    DamagePotential = Column(INTEGER)
    DistributionPotential = Column(INTEGER)
    InformationExposureRating = Column(INTEGER)
    ReportedInfection = Column(INTEGER)
