from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, INTEGER, SMALLINT, VARCHAR


class TempEntityResortInfo1(Base):
    __tablename__ = 'temp_EntityResortInfo1'
    id = Column(INTEGER, primary_key=True, nullable=False)
    EntityGuid = Column(CHAR(36), nullable=False)
    PolicyGuid = Column(CHAR(36))
    PolicyLock = Column(SMALLINT)
    Version = Column(VARCHAR(19))
    BuildNumber = Column(VARCHAR(24))
    IsSupport = Column(BIT)
