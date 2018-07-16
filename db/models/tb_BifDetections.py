from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, SMALLINT


class TbBifDetections(Base):
    __tablename__ = 'tb_BifDetections'
    Category = Column(SMALLINT, primary_key=True, nullable=False)
    Source = Column(SMALLINT, primary_key=True, nullable=False)
    Count = Column(INTEGER)
