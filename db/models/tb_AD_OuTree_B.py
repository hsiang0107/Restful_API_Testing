from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR


class TbADOuTreeB(Base):
    __tablename__ = 'tb_AD_OuTree_B'
    Guid = Column(CHAR(36), primary_key=True, nullable=False)
    LeftIndex = Column(INTEGER)
    RightIndex = Column(INTEGER)
    RootDomain = Column(NVARCHAR(256))
