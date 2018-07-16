from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, INTEGER, NVARCHAR


class TbSecurityLogViolateBlackInfo(Base):
    __tablename__ = 'tb_SecurityLogViolateBlackInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    SLF_Type = Column(INTEGER, nullable=False)
    SLF_Data = Column(NVARCHAR, nullable=False)
    SLF_RiskLevel = Column(INTEGER, nullable=False)
