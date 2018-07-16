from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER, NVARCHAR, VARCHAR


class TbActiveUpdateInfo(Base):
    __tablename__ = 'tb_ActiveUpdateInfo'
    ActiveUpdateID = Column(INTEGER, primary_key=True, nullable=False)
    Language = Column(INTEGER, primary_key=True, nullable=False)
    Platform = Column(INTEGER, nullable=False)
    GUID = Column(VARCHAR(36))
    AUCategory = Column(INTEGER)
    EnableSchedule = Column(BIT)
    EnableDisplay = Column(BIT)
    ProductName = Column(NVARCHAR(102))
    Version_Major = Column(INTEGER)
    Version_Minor = Column(INTEGER)
    Version_Revision = Column(INTEGER)
    PackageSize = Column(INTEGER)
