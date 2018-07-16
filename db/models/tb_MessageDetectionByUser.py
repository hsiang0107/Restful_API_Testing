from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbMessageDetectionByUser(Base):
    __tablename__ = 'tb_MessageDetectionByUser'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Key = Column(VARCHAR(256), nullable=False)
    SLF_ActionGroup = Column(SMALLINT, nullable=False)
    SL_Recipient = Column(NVARCHAR(254), nullable=False)
    SLF_SOSourceType = Column(SMALLINT, nullable=False)
    SL_FirstSender = Column(NVARCHAR(254))
    SL_FirstSubject = Column(NVARCHAR(254))
    SLF_FirstMsgType = Column(INTEGER)
    SLF_FirstProductID = Column(INTEGER)
    SLF_FirstAction = Column(SMALLINT)
    SLF_FirstUTCTime = Column(DATETIME)
    SL_LatestSender = Column(NVARCHAR(254))
    SL_LatestSubject = Column(NVARCHAR(254))
    SLF_LatestMsgType = Column(INTEGER)
    SLF_LatestProductID = Column(INTEGER)
    SLF_LatestAction = Column(SMALLINT)
    SLF_LatestUTCTime = Column(DATETIME)
