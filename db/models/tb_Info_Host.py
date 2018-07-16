from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, CHAR, INTEGER, NVARCHAR, VARCHAR


class TbInfoHost(Base):
    __tablename__ = 'tb_Info_Host'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Guid = Column(CHAR(36), nullable=False)
    ComputerName = Column(NVARCHAR(64))
    IPAddressList = Column(VARCHAR(1024))
    MACAddressList = Column(VARCHAR(256))
    DomainName = Column(NVARCHAR(64))
    FQDN = Column(VARCHAR(80))
    TimeZone = Column(INTEGER)
    DayLightSaving = Column(BINARY(40))
