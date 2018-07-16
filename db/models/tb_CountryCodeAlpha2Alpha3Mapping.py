from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbCountryCodeAlpha2Alpha3Mapping(Base):
    __tablename__ = 'tb_CountryCodeAlpha2Alpha3Mapping'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Alpha2CountryCode = Column(CHAR(2), nullable=False)
    Alpha3CountryCode = Column(CHAR(3), nullable=False)
