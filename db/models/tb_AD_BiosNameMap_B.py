from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import NVARCHAR


class TbADBiosNameMapB(Base):
    __tablename__ = 'tb_AD_BiosNameMap_B'
    Domain = Column(NVARCHAR(256), primary_key=True, nullable=False)
    DiosName = Column(NVARCHAR(256), primary_key=True)
