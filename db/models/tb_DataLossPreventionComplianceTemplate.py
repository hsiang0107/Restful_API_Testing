from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, VARCHAR


class TbDataLossPreventionComplianceTemplate(Base):
    __tablename__ = 'tb_DataLossPreventionComplianceTemplate'
    Guid = Column(CHAR(36), primary_key=True, nullable=False)
    Name = Column(NVARCHAR(256), nullable=False)
    Severity = Column(NVARCHAR(32), nullable=False)
    Code = Column(INTEGER, nullable=False)
    Language = Column(VARCHAR(10), primary_key=True, nullable=False)
