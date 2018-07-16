from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbSecondSuccessInstance(Base):
    __tablename__ = 'tb_SecondSuccessInstance'
    SSI_EntityID = Column(CHAR(36), primary_key=True)
    SSI_ProductType = Column(INTEGER)
    SSI_VirusName = Column(VARCHAR(64))
    SSI_InfectionDestination = Column(NVARCHAR(254))
    SSI_TotalInstances = Column(INTEGER)
    SSI_FoundTime = Column(DATETIME)
    SSI_YEAR = Column(INTEGER)
    SSI_MONTH = Column(INTEGER)
    SSI_DAY = Column(INTEGER)
