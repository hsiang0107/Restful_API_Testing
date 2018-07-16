from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR


class TbThreatIntelligenceDataSource(Base):
    __tablename__ = 'tb_ThreatIntelligenceDataSource'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Name = Column(NVARCHAR(254), nullable=False)
