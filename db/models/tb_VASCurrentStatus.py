from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbVASCurrentStatus(Base):
    __tablename__ = 'tb_VASCurrentStatus'
    VAS_CurrentStatusID = Column(INTEGER, primary_key=True, nullable=False)
    VAS_DomainName = Column(NVARCHAR(16), nullable=False)
    VAS_HostName = Column(NVARCHAR(64), nullable=False)
    VAS_IPAddress = Column(VARCHAR(256), nullable=False)
    VAS_IPAddressInt = Column(INTEGER, nullable=False)
    VAS_NVWIPAddress = Column(VARCHAR(256), nullable=False)
    VAS_JobID = Column(INTEGER, nullable=False)
    VAS_TaskID = Column(INTEGER, nullable=False)
    VAS_TaskName = Column(NVARCHAR(64))
    VAS_StartTime = Column(DATETIME, nullable=False)
    VAS_EndTime = Column(DATETIME, nullable=False)
    VAS_Action = Column(INTEGER, nullable=False)
    VAS_VASRestricted = Column(INTEGER, nullable=False)
    VAS_NVWRestricted = Column(INTEGER, nullable=False)
    VAS_Status = Column(INTEGER, nullable=False)
    VAS_Description = Column(INTEGER, nullable=False)
