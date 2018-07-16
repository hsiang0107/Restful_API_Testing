from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, INTEGER, NVARCHAR, VARCHAR


class TbIPCountries(Base):
    __tablename__ = 'tb_IPCountries'
    id = Column(INTEGER, primary_key=True, nullable=False)
    FromIP = Column(VARCHAR(15), nullable=False)
    ToIP = Column(VARCHAR(15), nullable=False)
    BeginNum = Column(BIGINT, nullable=False)
    EndNum = Column(BIGINT, nullable=False)
    CountryCode = Column(CHAR(2), nullable=False)
    CountryName = Column(NVARCHAR(128), nullable=False)
