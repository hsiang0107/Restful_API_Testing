from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class Tbvirusspywaresummary(Base):
    __tablename__ = 'tb_virus_spyware_summary'
    EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    Product_Type = Column(INTEGER, nullable=False)
    Category = Column(INTEGER, nullable=False)
    Date = Column(DATETIME, nullable=False)
    Major_Type = Column(INTEGER, nullable=False)
    Name = Column(NVARCHAR(128), nullable=False)
    Count = Column(INTEGER, nullable=False)
    Clean_Success = Column(INTEGER, nullable=False)
