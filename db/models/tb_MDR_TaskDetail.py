from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BIT, CHAR, DATETIME, INTEGER, NVARCHAR


class TbMDRTaskDetail(Base):
    __tablename__ = 'tb_MDR_TaskDetail'
    id = Column(BIGINT, primary_key=True, nullable=False)
    TaskID = Column(CHAR(36))
    TargetID = Column(CHAR(36))
    TargetType = Column(INTEGER)
    Status = Column(INTEGER)
    Finished = Column(BIT)
    MatchCriteria = Column(NVARCHAR)
    CmdResp = Column(NVARCHAR)
    LastUpdateTime = Column(DATETIME)
    OperationTime = Column(DATETIME)
    OperatorName = Column(NVARCHAR(256))
    IsReadyDispatch = Column(BIT)
