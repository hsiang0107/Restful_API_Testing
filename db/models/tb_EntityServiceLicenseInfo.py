from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbEntityServiceLicenseInfo(Base):
    __tablename__ = 'tb_EntityServiceLicenseInfo'
    EI_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    EI_SlotID = Column(INTEGER, primary_key=True, nullable=False)
    EI_LicenseStatus = Column(INTEGER, nullable=False)
    EI_AC = Column(VARCHAR(31), nullable=False)
    EI_ExpiredDate = Column(DATETIME, nullable=False)
    SeatCount = Column(INTEGER, nullable=False)
    EI_Description = Column(NVARCHAR(1024))
