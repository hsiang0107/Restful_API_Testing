from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR, VARCHAR


class TbRedAlertTAM(Base):
    __tablename__ = 'tb_RedAlertTAM'
    RAT_ID = Column(CHAR(36), primary_key=True, nullable=False)
    RAT_CloseAlert = Column(BIT, nullable=False)
    RAT_IssuedTime = Column(DATETIME)
    RAT_DateOfOrigin = Column(DATETIME)
    RAT_PlaceOfOrigin = Column(VARCHAR(50))
    RAT_AlertLevel = Column(INTEGER)
    RAT_RiskRating = Column(INTEGER)
    RAT_Destructive = Column(BIT)
    RAT_VirusName = Column(VARCHAR(64))
    RAT_AliasName = Column(VARCHAR(64))
    RAT_VirusType = Column(VARCHAR(50))
    RAT_VirusDescription = Column(NVARCHAR(3584))
    RAT_TriggerconditionOrDate = Column(VARCHAR(256))
    RAT_Encrypted = Column(BIT)
    RAT_Password = Column(BIT)
    RAT_SizeOfVirus = Column(INTEGER)
    RAT_Language = Column(VARCHAR(16))
    RAT_Platform = Column(VARCHAR(25))
    RAT_DetectedByPattern = Column(VARCHAR(16))
    RAT_DetectedByEngine = Column(VARCHAR(16))
    RAT_DetectedByEngineXML = Column(IMAGE)
    RAT_Solution = Column(VARCHAR(256))
    RAT_BlockingOption = Column(IMAGE)
    RAT_ResideAt = Column(VARCHAR(32))
    RAT_SpreadBy = Column(VARCHAR(32))
    RAT_DetectedBySpamVersion = Column(VARCHAR(16))
    RAT_DetectedByAntiSpamVersion = Column(VARCHAR(16))
    RAT_RequiredDCT = Column(VARCHAR(16))
    RAT_RequiredDCE = Column(VARCHAR(16))
    RAT_RequiredPattern2 = Column(VARCHAR(16))
    RAT_RequiredEngine2 = Column(VARCHAR(16))
    RAT_RequiredCAV = Column(VARCHAR(16))
