from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, NVARCHAR, SMALLINT, VARCHAR


class TbDDM3rdPartyTagging(Base):
    __tablename__ = 'tb_DDM_3rdPartyTagging'
    SID = Column(BIGINT, primary_key=True, nullable=False)
    Category = Column(SMALLINT, primary_key=True, nullable=False)
    InterestedHost = Column(NVARCHAR(64))
    HostOwner = Column(NVARCHAR(64))
    Department = Column(NVARCHAR(64))
    Service = Column(NVARCHAR(64))
    DeviceType = Column(NVARCHAR(128))
    MACAddress = Column(NVARCHAR(17))
    ReverseDNS = Column(NVARCHAR(2048))
    Destination = Column(NVARCHAR(128))
    Registrar = Column(VARCHAR(128))
    Registrant = Column(VARCHAR(128))
    CreatedDate = Column(DATETIME)
    OverallScore = Column(SMALLINT)
    IPRating = Column(SMALLINT)
    URLRating = Column(SMALLINT)
    FileRating = Column(SMALLINT)
    MailRating = Column(SMALLINT)
