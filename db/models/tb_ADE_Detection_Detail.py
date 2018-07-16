from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, VARCHAR


class TbADEDetectionDetail(Base):
    __tablename__ = 'tb_ADE_Detection_Detail'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36), nullable=False)
    SLF_LocalId = Column(INTEGER, nullable=False)
    SLF_ParentID = Column(INTEGER, nullable=False)
    SLF_ObjectType = Column(VARCHAR(32))
    SLF_ObjectValue = Column(NVARCHAR(512))
    SLF_FirstSight = Column(VARCHAR(30))
    SLF_Properties = Column(NVARCHAR)
