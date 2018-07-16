from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbMDRSettings(Base):
    __tablename__ = 'tb_MDRSettings'
    Enabled = Column(BIT)
    AutoApproval = Column(BIT)
    LastDeployCertCTID = Column(CHAR(36))
    ServerAddress = Column(NVARCHAR(256), primary_key=True)
    Recipient_Users = Column(VARCHAR(1024))
    Recipient_Groups = Column(VARCHAR(1024))
    RegisterTime = Column(DATETIME)
    LastTaskPollingTime = Column(DATETIME)
    LastTaskUpdateTime = Column(DATETIME)
    CertUTCExpiredTime = Column(DATETIME)
