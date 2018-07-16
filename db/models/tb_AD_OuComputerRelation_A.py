from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER


class TbADOuComputerRelationA(Base):
    __tablename__ = 'tb_AD_OuComputerRelation_A'
    id = Column(INTEGER, primary_key=True, nullable=False)
    GUID = Column(UNIQUEIDENTIFIER, nullable=False)
    ParentGUID = Column(UNIQUEIDENTIFIER, nullable=False)
    Name = Column(NVARCHAR(64), nullable=False)
    Type = Column(SMALLINT, nullable=False)
    DN = Column(NVARCHAR)
    DomainName = Column(NVARCHAR(64))
    LastLogonTime = Column(DATETIME)
    RootDomain = Column(NVARCHAR(256))
