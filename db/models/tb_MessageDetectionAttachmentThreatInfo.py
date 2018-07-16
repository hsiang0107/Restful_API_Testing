from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbMessageDetectionAttachmentThreatInfo(Base):
    __tablename__ = 'tb_MessageDetectionAttachmentThreatInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Instance_ID = Column(VARCHAR(256))
    SLF_AttachmentFileName = Column(NVARCHAR(1024), nullable=False)
    SLF_AttachmentSHA1 = Column(VARCHAR(64), nullable=False)
    SLF_AttachmentFileType = Column(VARCHAR(2048))
    SLF_DetectedBy = Column(INTEGER)
    SLF_KnownThreatName = Column(VARCHAR(64))
    SLF_SBXDetectionName = Column(VARCHAR(64))
    SLF_SBXSubmissionTime = Column(DATETIME)
    SLF_SBXSubmissionRule = Column(VARCHAR(64))
    SLF_SBXRiskLevel = Column(INTEGER)
    SLF_SBXThreatCategories = Column(NVARCHAR(128))
