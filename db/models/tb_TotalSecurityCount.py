from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbTotalSecurityCount(Base):
    __tablename__ = 'tb_TotalSecurityCount'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_CMServerID = Column(CHAR(36))
    CLF_ProductType = Column(INTEGER, nullable=False)
    VLF_CleanFail = Column(INTEGER)
    VLF_DeleteFail = Column(INTEGER)
    VLF_MoveFail = Column(INTEGER)
    VLF_RenameFail = Column(INTEGER)
    VLF_BypassFail = Column(INTEGER)
    VLF_AttachStripFail = Column(INTEGER)
    VLF_TotalFail = Column(INTEGER)
    SL_Deliver = Column(INTEGER)
    VLF_DeleteSuccess = Column(INTEGER)
    SL_Forward = Column(INTEGER)
    SL_Quarantine = Column(INTEGER)
    SL_Postpone = Column(INTEGER)
    VLF_AttachStripSuccess = Column(INTEGER)
    VLF_TotalSuccess = Column(INTEGER)
    TVC_TotalClean = Column(INTEGER)
    TVC_TotalDelete = Column(INTEGER)
    TVC_TotalMove = Column(INTEGER)
    TVC_TotalRename = Column(INTEGER)
    TVC_TotalBypass = Column(INTEGER)
    TVC_TotalAttachStrip = Column(INTEGER)
    TVC_Total = Column(INTEGER)
    TVC_SummaryTime = Column(DATETIME)
    TVC_YEAR = Column(INTEGER)
    TVC_MONTH = Column(INTEGER)
    TVC_DAY = Column(INTEGER)
    CasStatus = Column(INTEGER)
