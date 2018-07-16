from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, UNIQUEIDENTIFIER, VARCHAR


class TbsCloudPolicyJournal(Base):
    __tablename__ = 'tb_sCloudPolicyJournal'
    PolicyID = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    UTCDurationStart = Column(DATETIME, nullable=False)
    UTCDurationEnd = Column(DATETIME)
    DisplayName = Column(NVARCHAR(256))
    PolicyType = Column(VARCHAR(32), nullable=False)
    ProductType = Column(INTEGER, nullable=False)
    Settings = Column(NVARCHAR, nullable=False)
    ActivatedSettings = Column(NVARCHAR, nullable=False)
    JournalDetailGUID = Column(UNIQUEIDENTIFIER)
