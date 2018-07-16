from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, SMALLINT


class TbADGroupA(Base):
    __tablename__ = 'tb_AD_Group_A'
    id = Column(INTEGER, primary_key=True, nullable=False)
    GUID = Column(CHAR(36), nullable=False)
    Name = Column(NVARCHAR(256), nullable=False)
    DN = Column(NVARCHAR(1024), nullable=False)
    Domain = Column(NVARCHAR(256), nullable=False)
    Sid = Column(NVARCHAR(256))
    ReferenceCount = Column(INTEGER)
    MemberGotten = Column(SMALLINT)
    RootDomain = Column(NVARCHAR(256))
    Members = Column(NVARCHAR)
