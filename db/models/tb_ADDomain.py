from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR


class TbADDomain(Base):
    __tablename__ = 'tb_ADDomain'
    ADDomainID = Column(INTEGER, primary_key=True, nullable=False)
    Name = Column(NVARCHAR(850), nullable=False)
