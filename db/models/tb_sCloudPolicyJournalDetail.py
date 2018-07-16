from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, UNIQUEIDENTIFIER


class TbsCloudPolicyJournalDetail(Base):
    __tablename__ = 'tb_sCloudPolicyJournalDetail'
    JournalDetailGUID = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    EntityGUID = Column(CHAR(36), nullable=False)
    UTCApplyTime = Column(DATETIME, nullable=False)
    UTCEndTime = Column(DATETIME)
