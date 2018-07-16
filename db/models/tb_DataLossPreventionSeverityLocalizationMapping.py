from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, VARCHAR


class TbDataLossPreventionSeverityLocalizationMapping(Base):
    __tablename__ = 'tb_DataLossPreventionSeverityLocalizationMapping'
    Language = Column(VARCHAR(10), primary_key=True, nullable=False)
    Severity = Column(NVARCHAR(32), primary_key=True, nullable=False)
    Code = Column(INTEGER, nullable=False)
