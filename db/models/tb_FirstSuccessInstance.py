from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbFirstSuccessInstance(Base):
    __tablename__ = 'tb_FirstSuccessInstance'
    FSI_EntityID = Column(CHAR(36), primary_key=True)
    FSI_ProductType = Column(INTEGER)
    FSI_VirusName = Column(VARCHAR(64))
    FSI_InfectionDestination = Column(NVARCHAR(254))
    FSI_TotalInstances = Column(INTEGER)
    FSI_FoundTime = Column(DATETIME)
    FSI_YEAR = Column(INTEGER)
    FSI_MONTH = Column(INTEGER)
    FSI_DAY = Column(INTEGER)
