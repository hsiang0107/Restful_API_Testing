from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbACInfo(Base):
    __tablename__ = 'tb_ACInfo'
    AC = Column(VARCHAR(31), primary_key=True, nullable=False)
    ProductCode = Column(VARCHAR(2), nullable=False)
    APName = Column(VARCHAR(2), nullable=False)
    OSVersion = Column(VARCHAR(2), nullable=False)
    Profile = Column(VARCHAR(160), nullable=False)
    Status = Column(INTEGER, nullable=False)
    ExpiredDate = Column(DATETIME, nullable=False)
    VersionType = Column(BIT, nullable=False)
    SeatCount = Column(INTEGER)
    Note = Column(NVARCHAR(64))
