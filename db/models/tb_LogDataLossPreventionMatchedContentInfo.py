from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, VARCHAR


class TbLogDataLossPreventionMatchedContentInfo(Base):
    __tablename__ = 'tb_LogDataLossPreventionMatchedContentInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    MatchedContent = Column(NVARCHAR(128), nullable=False)
    MatchedInfo = Column(VARCHAR(256), nullable=False)
