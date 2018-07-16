from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbstatuslogjournalServiceLicense(Base):
    __tablename__ = 'tb_statuslogjournalServiceLicense'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_SlotID = Column(INTEGER, nullable=False)
    SLF_Status = Column(INTEGER, nullable=False)
    SLF_ACKey = Column(VARCHAR(31), nullable=False)
    SLF_ExpirationDate = Column(DATETIME, nullable=False)
    SLF_SeatCount = Column(INTEGER, nullable=False)
    SLF_Description = Column(NVARCHAR(1024))
    lutontmcm = Column(DATETIME)
