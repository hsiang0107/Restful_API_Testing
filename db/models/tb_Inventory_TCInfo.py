from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbInventoryTCInfo(Base):
    __tablename__ = 'tb_Inventory_TCInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    FamilyName = Column(VARCHAR(256))
    DamagePotential = Column(SMALLINT)
    DistributionPotential = Column(SMALLINT)
    VSAPIEngineVersion = Column(VARCHAR(64))
    FirstSeen = Column(DATETIME)
    LastSeen = Column(DATETIME)
    Rank1AffectedCountry = Column(VARCHAR(3))
    Rank2AffectedCountry = Column(VARCHAR(3))
    Rank3AffectedCountry = Column(VARCHAR(3))
    MalwareDescription = Column(NVARCHAR)
    ThreatName = Column(NVARCHAR(256), nullable=False)
    LUT = Column(DATETIME, nullable=False)
