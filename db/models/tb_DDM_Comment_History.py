from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT


class TbDDMCommentHistory(Base):
    __tablename__ = 'tb_DDM_Comment_History'
    id = Column(INTEGER, primary_key=True, nullable=False)
    SID = Column(BIGINT, nullable=False)
    Category = Column(SMALLINT, nullable=False)
    Comment = Column(NVARCHAR(1024), nullable=False)
    User = Column(CHAR(36), nullable=False)
    UTCTime = Column(DATETIME, nullable=False)
