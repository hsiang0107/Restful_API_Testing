from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME


class TbCloudScanServerSourceInfo(Base):
    __tablename__ = 'tb_CloudScanServerSourceInfo'
    EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    SourceHash = Column(BIGINT, primary_key=True, nullable=False)
    AddedDate = Column(DATETIME, nullable=False)
