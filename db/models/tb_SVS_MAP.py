from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR


class TbSVSMAP(Base):
    __tablename__ = 'tb_SVS_MAP'
    SVS_ID = Column(INTEGER, primary_key=True, nullable=False)
    SVS_Name = Column(NVARCHAR(64))
