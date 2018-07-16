from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbDCSsummary(Base):
    __tablename__ = 'tb_DCS_summary'
    EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    Product_Type = Column(INTEGER, nullable=False)
    Category = Column(INTEGER, nullable=False)
    Date = Column(DATETIME, primary_key=True, nullable=False)
    Major_Type = Column(INTEGER, nullable=False)
    Name = Column(NVARCHAR(64), primary_key=True, nullable=False)
    Count = Column(INTEGER, nullable=False)
    Clean_Success = Column(INTEGER, nullable=False)
