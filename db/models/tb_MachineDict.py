from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbMachineDict(Base):
    __tablename__ = 'tb_MachineDict'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MD_MachineID = Column(CHAR(36), nullable=False)
    MD_MacAddress = Column(VARCHAR(17))
    MD_MachineName = Column(NVARCHAR(64))
    MD_UnReferTime = Column(DATETIME)
