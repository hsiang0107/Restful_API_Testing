from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbVirtualTAMInterval(Base):
    __tablename__ = 'tb_VirtualTAM_Interval'
    VTI_ID = Column(CHAR(36), primary_key=True, nullable=False)
    VTI_Frequency = Column(INTEGER, nullable=False)
    VTI_FreqGrade = Column(INTEGER, nullable=False)
    VTI_Enabled = Column(INTEGER)
    VTI_ServerType = Column(VARCHAR(32))
    VTI_Server = Column(VARCHAR(256), nullable=False)
