from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbCasMachineList(Base):
    __tablename__ = 'tb_CasMachineList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    CML_CMGuid = Column(CHAR(36))
    CML_MachineID = Column(CHAR(36))
    CML_Platform_Type = Column(VARCHAR(16))
    CML_OS_Type = Column(VARCHAR(16))
    CML_OS_Name = Column(NVARCHAR(128))
    CML_OS_Version = Column(VARCHAR(64))
    CML_OS_SPVersion = Column(VARCHAR(32))
    CML_OS_Language = Column(INTEGER)
    CML_OS_ContryCode = Column(VARCHAR(8))
    CML_MachineName = Column(NVARCHAR(64))
    CML_IPAddressList = Column(VARCHAR(1024))
    CML_MACAddressList = Column(VARCHAR(256))
    CML_DomainName = Column(NVARCHAR(64))
    CML_GroupName = Column(NVARCHAR(64))
    CML_ADObjectGuid = Column(UNIQUEIDENTIFIER)
    CML_FQDN = Column(VARCHAR(80))
    CML_UserGuid = Column(CHAR(36))
    CML_SystemModel = Column(SMALLINT)
