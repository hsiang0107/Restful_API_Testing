from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BIT, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbWhitelistForSoDistB(Base):
    __tablename__ = 'tb_WhitelistForSoDist_B'
    id = Column(INTEGER, primary_key=True, nullable=False)
    SLF_Type = Column(INTEGER, nullable=False)
    SLF_Data = Column(NVARCHAR, nullable=False)
    UserDefinedNotes = Column(NVARCHAR)
    SLF_Key = Column(VARCHAR(256), nullable=False)
    SLF_RiskLevel = Column(INTEGER, nullable=False)
    ScanAction = Column(SMALLINT)
    SLF_URLCorrelationKey = Column(VARCHAR(64))
    SLF_ExpireDateTimeStamp = Column(BIGINT)
    SLF_ExpiredUTCDate = Column(DATETIME)
    IsWildcardException = Column(BIT)
    IsExceptionDueToWildcard = Column(BIT)
