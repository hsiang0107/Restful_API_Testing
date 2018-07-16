from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbInstanceForVirusOutbreak(Base):
    __tablename__ = 'tb_InstanceForVirusOutbreak'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_ProductType = Column(INTEGER, nullable=False)
    VLF_VirusName = Column(VARCHAR(64))
    IFVO_TotalInstances = Column(INTEGER, nullable=False)
    IFVO_FoundTime = Column(DATETIME)
    IFVO_YEAR = Column(INTEGER, nullable=False)
    IFVO_MONTH = Column(INTEGER, nullable=False)
    IFVO_DAY = Column(INTEGER, nullable=False)
