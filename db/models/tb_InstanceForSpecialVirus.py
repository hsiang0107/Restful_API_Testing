from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbInstanceForSpecialVirus(Base):
    __tablename__ = 'tb_InstanceForSpecialVirus'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_ProductType = Column(INTEGER, nullable=False)
    VLF_VirusName = Column(VARCHAR(64))
    VLF_InfectionDestination = Column(NVARCHAR(254))
    VIFSV_FoundTime = Column(DATETIME)
    VIFSV_IsFirst = Column(BIT)
    VIFSV_YEAR = Column(INTEGER, nullable=False)
    VIFSV_MONTH = Column(INTEGER, nullable=False)
    VIFSV_DAY = Column(INTEGER, nullable=False)
