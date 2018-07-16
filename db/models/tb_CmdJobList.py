from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbCmdJobList(Base):
    __tablename__ = 'tb_CmdJobList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    JobID = Column(CHAR(36), nullable=False)
    CmdType = Column(INTEGER, nullable=False)
    UserID = Column(CHAR(36), nullable=False)
    ParamJSON = Column(NVARCHAR)
    ResultTbName = Column(VARCHAR(512))
    Status = Column(INTEGER)
    Progress = Column(INTEGER)
    LastAccessTme = Column(DATETIME)
