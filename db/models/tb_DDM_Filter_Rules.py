from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT, TINYINT


class TbDDMFilterRules(Base):
    __tablename__ = 'tb_DDM_Filter_Rules'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Category = Column(SMALLINT, nullable=False)
    Enabled = Column(TINYINT, nullable=False)
    applyMode = Column(SMALLINT, nullable=False)
    Criteria = Column(NVARCHAR, nullable=False)
    Status = Column(SMALLINT, nullable=False)
    Creator = Column(CHAR(36), nullable=False)
    CreateUTCTime = Column(DATETIME, nullable=False)
    LastUpdateUTCTime = Column(DATETIME, nullable=False)
    Comment = Column(NVARCHAR(256))
