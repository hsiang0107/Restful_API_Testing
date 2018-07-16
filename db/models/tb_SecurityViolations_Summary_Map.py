from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbSecurityViolationsSummaryMap(Base):
    __tablename__ = 'tb_SecurityViolations_Summary_Map'
    MsgLogID = Column(CHAR(36), primary_key=True, nullable=False)
    SVS_ID = Column(INTEGER, nullable=False)
