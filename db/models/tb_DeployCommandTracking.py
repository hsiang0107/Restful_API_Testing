from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbDeployCommandTracking(Base):
    __tablename__ = 'tb_DeployCommandTracking'
    DCT_ID = Column(CHAR(36), primary_key=True, nullable=False)
    DCT_CommandTrackingID = Column(CHAR(36), nullable=False)
    DCT_ComponentType = Column(INTEGER)
    DCT_ComponentCmdTrackingID = Column(CHAR(36))
    DCT_CommandMsgID = Column(INTEGER)
    DCT_CreateTime = Column(DATETIME)
