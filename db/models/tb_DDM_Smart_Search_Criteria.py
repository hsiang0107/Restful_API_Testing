from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT


class TbDDMSmartSearchCriteria(Base):
    __tablename__ = 'tb_DDM_Smart_Search_Criteria'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Category = Column(SMALLINT, nullable=False)
    Name = Column(NVARCHAR(256), nullable=False)
    Criteria = Column(NVARCHAR, nullable=False)
    Creator = Column(CHAR(36), nullable=False)
    CreateUTCTime = Column(DATETIME, nullable=False)
    LastUpdateUTCTime = Column(DATETIME, nullable=False)
    UpdateBy = Column(CHAR(36), nullable=False)
