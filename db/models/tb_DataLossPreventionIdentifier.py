from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, NVARCHAR, VARCHAR


class TbDataLossPreventionIdentifier(Base):
    __tablename__ = 'tb_DataLossPreventionIdentifier'
    Guid = Column(CHAR(36), primary_key=True, nullable=False)
    Name = Column(NVARCHAR(256), nullable=False)
    Language = Column(VARCHAR(10), primary_key=True, nullable=False)
