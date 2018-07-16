from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbInfoOS(Base):
    __tablename__ = 'tb_Info_OS'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Guid = Column(CHAR(36), nullable=False)
    OS_Name = Column(NVARCHAR(64))
    OS_Version = Column(VARCHAR(32))
    OS_ServicePack = Column(VARCHAR(32))
    OS_Language = Column(INTEGER)
    OS_ContryCode = Column(VARCHAR(8))
    CPUType = Column(SMALLINT)
