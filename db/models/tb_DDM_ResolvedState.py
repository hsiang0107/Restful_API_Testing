from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, SMALLINT


class TbDDMResolvedState(Base):
    __tablename__ = 'tb_DDM_ResolvedState'
    SID = Column(BIGINT, primary_key=True, nullable=False)
    Category = Column(SMALLINT, primary_key=True, nullable=False)
    Status = Column(SMALLINT, nullable=False)
