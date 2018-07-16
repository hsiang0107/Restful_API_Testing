from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbSecondFailureInstance(Base):
    __tablename__ = 'tb_SecondFailureInstance'
    SFI_EntityID = Column(CHAR(36), primary_key=True)
    SFI_ProductType = Column(INTEGER)
    SFI_VirusName = Column(VARCHAR(64))
    SFI_InfectionDestination = Column(NVARCHAR(254))
    SFI_TotalInstances = Column(INTEGER)
    SFI_FoundTime = Column(DATETIME)
    SFI_YEAR = Column(INTEGER)
    SFI_MONTH = Column(INTEGER)
    SFI_DAY = Column(INTEGER)
