from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbNetworkOutbreakInstance(Base):
    __tablename__ = 'tb_NetworkOutbreakInstance'
    CLF_EntityID = Column(CHAR(36), primary_key=True)
    CLF_ProductType = Column(INTEGER)
    VLF_VirusName = Column(VARCHAR(64))
    VLF_InfectionDestination = Column(NVARCHAR(254))
    IFVID_TotalInstances = Column(INTEGER)
    IFVID_FoundTime = Column(DATETIME)
    IFVID_YEAR = Column(INTEGER)
    IFVID_MONTH = Column(INTEGER)
    IFVID_DAY = Column(INTEGER)
