from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, DATETIME, INTEGER, SMALLINT, VARCHAR


class TbDwellTimeInfo(Base):
    __tablename__ = 'tb_DwellTimeInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    FileSHA1 = Column(VARCHAR(64), nullable=False)
    DetectionName = Column(VARCHAR(64), nullable=False)
    EventContent_MD5 = Column(BINARY(16), nullable=False)
    EventContentCategory = Column(SMALLINT, nullable=False)
    RetroScanData_MD5 = Column(BINARY(16), nullable=False)
    Status = Column(SMALLINT, nullable=False)
    CreateTime = Column(DATETIME, nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)
