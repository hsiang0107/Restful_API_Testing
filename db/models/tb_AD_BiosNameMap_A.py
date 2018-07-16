from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import NVARCHAR


class TbADBiosNameMapA(Base):
    __tablename__ = 'tb_AD_BiosNameMap_A'
    Domain = Column(NVARCHAR(256), primary_key=True, nullable=False)
    DiosName = Column(NVARCHAR(256), primary_key=True)
