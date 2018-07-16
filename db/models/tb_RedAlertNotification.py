from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, VARCHAR


class TbRedAlertNotification(Base):
    __tablename__ = 'tb_RedAlertNotification'
    RAN_ID = Column(CHAR(36), primary_key=True, nullable=False)
    RAN_RedAlertID = Column(CHAR(36), nullable=False)
    RAN_TrackingID = Column(CHAR(36), nullable=False)
    RAN_GroupList = Column(VARCHAR(1024))
    RAN_Subject = Column(VARCHAR(128))
    RAN_Message = Column(VARCHAR(1024))
    RAN_SendEmail = Column(BIT)
    RAN_EmailReceiverList = Column(VARCHAR(1024))
    RAN_SendSMS = Column(BIT)
    RAT_SMSNumberList = Column(VARCHAR(1024))
    RAN_SendPager = Column(BIT)
    RAN_PagerNumberList = Column(VARCHAR(1024))
