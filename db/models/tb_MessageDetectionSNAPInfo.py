from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, INTEGER, NVARCHAR, VARCHAR


class TbMessageDetectionSNAPInfo(Base):
    __tablename__ = 'tb_MessageDetectionSNAPInfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Instance_ID = Column(VARCHAR(256))
    SLF_SNAP_FeatureID = Column(INTEGER)
    SLF_SNAP_DetectionEntityValue = Column(NVARCHAR(2560))
