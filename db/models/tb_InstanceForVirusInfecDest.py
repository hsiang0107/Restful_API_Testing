from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbInstanceForVirusInfecDest(Base):
    __tablename__ = 'tb_InstanceForVirusInfecDest'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_ProductType = Column(INTEGER, nullable=False)
    VLF_VirusName = Column(VARCHAR(64))
    VLF_InfectionDestination = Column(NVARCHAR(254))
    IFVID_TotalInstances = Column(INTEGER, nullable=False)
    IFVID_FoundTime = Column(DATETIME)
    IFVID_YEAR = Column(INTEGER, nullable=False)
    IFVID_MONTH = Column(INTEGER, nullable=False)
    IFVID_DAY = Column(INTEGER, nullable=False)
