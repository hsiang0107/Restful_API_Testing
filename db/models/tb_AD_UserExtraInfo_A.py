from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR


class TbADUserExtraInfoA(Base):
    __tablename__ = 'tb_AD_UserExtraInfo_A'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Guid = Column(CHAR(36), nullable=False)
    UEI_Title = Column(NVARCHAR(128))
    UEI_Dept = Column(NVARCHAR(64))
    UEI_Office = Column(NVARCHAR(128))
    UEI_OfficePhoneNO = Column(NVARCHAR(64))
    UEI_HomePhoneNO = Column(NVARCHAR(64))
    UEI_CustomDept = Column(NVARCHAR(1024))
    UEI_CustomDeptColor = Column(NVARCHAR(10))
    RootDomain = Column(NVARCHAR(256))
