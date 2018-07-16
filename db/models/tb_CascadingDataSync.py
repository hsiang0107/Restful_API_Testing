from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME


class TbCascadingDataSync(Base):
    __tablename__ = 'tb_CascadingDataSync'
    CDS_Guid = Column(CHAR(36), primary_key=True, nullable=False)
    CDS_LastUpdateTime = Column(DATETIME)
    CDS_LastReceivedTime = Column(DATETIME)
