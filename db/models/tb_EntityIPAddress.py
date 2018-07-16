from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BINARY, CHAR, TINYINT, VARCHAR


class TbEntityIPAddress(Base):
    __tablename__ = 'tb_EntityIPAddress'
    EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    IPAddress = Column(VARCHAR(256), primary_key=True)
    FirstOctet = Column(TINYINT)
    SecondOctet = Column(TINYINT)
    ThirdOctet = Column(TINYINT)
    FourthOctet = Column(TINYINT)
    IPv4INT = Column(BIGINT)
    IPv6Bin = Column(BINARY(16))
