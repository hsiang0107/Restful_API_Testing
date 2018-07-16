from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbVirusSummaryCondition(Base):
    __tablename__ = 'tb_VirusSummaryCondition'
    USER_ID = Column(VARCHAR(38), primary_key=True)
    TVC_Token = Column(VARCHAR(1024), primary_key=True)
    TVC_Node = Column(VARCHAR(1024))
    TVC_Begin_YEAR = Column(INTEGER, nullable=False)
    TVC_Begin_MONTH = Column(INTEGER, nullable=False)
    TVC_Begin_DAY = Column(INTEGER, nullable=False)
    TVC_End_YEAR = Column(INTEGER, nullable=False)
    TVC_End_MONTH = Column(INTEGER, nullable=False)
    TVC_End_DAY = Column(INTEGER, nullable=False)
