from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, VARCHAR


class TbCloudScanServerSourceList(Base):
    __tablename__ = 'tb_CloudScanServerSourceList'
    SourceHash = Column(BIGINT, primary_key=True, nullable=False)
    Source = Column(VARCHAR(2048), nullable=False)
    AddedDate = Column(DATETIME, nullable=False)
