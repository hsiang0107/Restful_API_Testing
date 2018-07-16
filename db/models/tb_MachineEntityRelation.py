from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbMachineEntityRelation(Base):
    __tablename__ = 'tb_MachineEntityRelation'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MI_MachineID = Column(CHAR(36), nullable=False)
    MI_Platform_Type = Column(VARCHAR(16))
    MI_OS_Type = Column(VARCHAR(16))
    MI_OS_Name = Column(NVARCHAR(128))
    MI_OS_Version = Column(VARCHAR(64))
    MI_OS_SPVersion = Column(VARCHAR(32))
    MI_OS_Language = Column(INTEGER)
    MI_OS_ContryCode = Column(VARCHAR(8))
    MI_MachineName = Column(NVARCHAR(64))
    MI_IPAddressList = Column(VARCHAR(1024))
    MI_MACAddressList = Column(VARCHAR(256))
    MI_DomainName = Column(NVARCHAR(64))
    MI_GroupName = Column(NVARCHAR(64))
    MI_ADObjectGuid = Column(UNIQUEIDENTIFIER)
    MI_FQDN = Column(VARCHAR(80))
    MI_UserGuid = Column(CHAR(36))
    MI_CMGuid = Column(CHAR(36))
    MI_SystemModel = Column(SMALLINT)
    MI_NetworkQuarantineSetting = Column(SMALLINT)
    MI_NetworkQuarantineSettingResult = Column(SMALLINT)
