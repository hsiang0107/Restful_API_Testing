from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR


class TbADUserDistinctDepartment(Base):
    __tablename__ = 'tb_AD_UserDistinctDepartment'
    id = Column(INTEGER, primary_key=True, nullable=False)
    UEI_Dept = Column(NVARCHAR(64))
