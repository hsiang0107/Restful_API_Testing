from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, INTEGER, NVARCHAR, VARCHAR


class TbLogMail(Base):
    __tablename__ = 'tb_LogMail'
    CMGuid = Column(CHAR(36))
    id = Column(INTEGER, nullable=False)
    Recipient = Column(NVARCHAR(1024))
    Sender = Column(NVARCHAR(320))
    Subject = Column(NVARCHAR(512))
    MsgLogID = Column(CHAR(36))
    SeqID = Column(BIGINT, primary_key=True, nullable=False)
    AttachmentFileName = Column(NVARCHAR(1024))
    AttachmentFileSize = Column(INTEGER)
    AttachmentFileType = Column(VARCHAR(64))
    AttachmentSHA1 = Column(VARCHAR(40))
