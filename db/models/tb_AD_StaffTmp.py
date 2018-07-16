from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR


class TbADStaffTmp(Base):
    __tablename__ = 'tb_AD_StaffTmp'
    GUID = Column(CHAR(36), primary_key=True, nullable=False)
    SAMAccountName = Column(NVARCHAR(32), nullable=False)
    Domain = Column(NVARCHAR(256), nullable=False)
    Type = Column(INTEGER, nullable=False)
    ManagerGUID = Column(CHAR(36))
