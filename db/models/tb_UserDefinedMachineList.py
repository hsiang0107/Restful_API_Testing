from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, VARCHAR


class TbUserDefinedMachineList(Base):
    __tablename__ = 'tb_UserDefinedMachineList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    HostName = Column(NVARCHAR(128))
    IPAddress = Column(VARCHAR(256))
