from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbTotalVirusCount(Base):
    __tablename__ = 'tb_TotalVirusCount'
    CLF_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    CLF_CMServerID = Column(CHAR(36))
    CLF_ProductType = Column(INTEGER, nullable=False)
    VLF_CleanFail = Column(INTEGER, nullable=False)
    VLF_DeleteFail = Column(INTEGER, nullable=False)
    VLF_MoveFail = Column(INTEGER, nullable=False)
    VLF_RenameFail = Column(INTEGER, nullable=False)
    VLF_BypassFail = Column(INTEGER, nullable=False)
    VLF_DenyAccessFail = Column(INTEGER)
    VLF_AttachStripFail = Column(INTEGER, nullable=False)
    VLF_TotalFail = Column(INTEGER, nullable=False)
    VLF_CleanSuccess = Column(INTEGER, nullable=False)
    VLF_DenyAccessSuccess = Column(INTEGER)
    VLF_DeleteSuccess = Column(INTEGER, nullable=False)
    VLF_MoveSuccess = Column(INTEGER, nullable=False)
    VLF_RenameSuccess = Column(INTEGER, nullable=False)
    VLF_BypassSuccess = Column(INTEGER, nullable=False)
    VLF_AttachStripSuccess = Column(INTEGER, nullable=False)
    VLF_TotalSuccess = Column(INTEGER, nullable=False)
    TVC_TotalClean = Column(INTEGER, nullable=False)
    TVC_TotalDelete = Column(INTEGER, nullable=False)
    TVC_TotalMove = Column(INTEGER, nullable=False)
    TVC_TotalRename = Column(INTEGER, nullable=False)
    TVC_TotalBypass = Column(INTEGER, nullable=False)
    TVC_TotalAttachStrip = Column(INTEGER, nullable=False)
    TVC_Total = Column(INTEGER, nullable=False)
    TVC_SummaryTime = Column(DATETIME)
    TVC_YEAR = Column(INTEGER, nullable=False)
    TVC_MONTH = Column(INTEGER, nullable=False)
    TVC_DAY = Column(INTEGER, nullable=False)
    CasStatus = Column(INTEGER)
    MajorType = Column(INTEGER)
