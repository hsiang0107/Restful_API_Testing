from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, VARCHAR


class CDSMUserLog(Base):
    __tablename__ = 'CDSM_UserLog'
    id = Column(INTEGER, primary_key=True, nullable=False)
    time = Column(INTEGER)
    type = Column(INTEGER)
    event = Column(INTEGER)
    account = Column(VARCHAR(32))
    eq_account = Column(VARCHAR(32))
    result = Column(INTEGER)
    reason = Column(INTEGER)
    desp = Column(NVARCHAR(1023))
    code_page = Column(VARCHAR(20))
    eq_code_page = Column(VARCHAR(20))
