from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class Tbmailsendersummary(Base):
    __tablename__ = 'tb_mail_sender_summary'
    EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    Product_Type = Column(INTEGER, nullable=False)
    Date = Column(DATETIME, nullable=False)
    Sender = Column(VARCHAR(254), nullable=False)
    Count = Column(INTEGER, nullable=False)
