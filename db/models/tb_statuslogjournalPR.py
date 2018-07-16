from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbstatuslogjournalPR(Base):
    __tablename__ = 'tb_statuslogjournalPR'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_ACKey = Column(VARCHAR(31), nullable=False)
    SLF_Profile = Column(VARCHAR(160))
    SLF_LastUpdateTime = Column(DATETIME)
    SLF_PRState = Column(INTEGER)
    SLF_ExpireDate = Column(DATETIME)
    SLF_ACDescription = Column(NVARCHAR(1024))
    SLF_SlotID = Column(INTEGER)
    lutontmcm = Column(DATETIME)
