from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbEntityPolicyInfo(Base):
    __tablename__ = 'tb_EntityPolicyInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    EntityGuid = Column(CHAR(36), nullable=False)
    PolicyGuid = Column(CHAR(36))
    PolicyType = Column(VARCHAR(32))
    PolicyLock = Column(SMALLINT)
    OriginalPolicyGuid = Column(CHAR(36))
    PolicyStatus = Column(SMALLINT)
    IsDeployed = Column(SMALLINT)
    UserID = Column(NVARCHAR(256))
    LastUpdateTime = Column(DATETIME)
