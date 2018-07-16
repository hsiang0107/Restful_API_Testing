from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbSpecialVirusPolicy(Base):
    __tablename__ = 'tb_SpecialVirusPolicy'
    VLF_VirusName = Column(VARCHAR(64), primary_key=True)
    SVP_TakeCarePerNHour = Column(INTEGER, nullable=False)
    SVP_MajorType = Column(INTEGER)
