from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, SMALLINT, VARCHAR


class TbCnCDetectionByMachine(Base):
    __tablename__ = 'tb_CnCDetectionByMachine'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Key = Column(VARCHAR(256), nullable=False)
    SLF_ActionGroup = Column(SMALLINT, nullable=False)
    SLF_MachineID = Column(CHAR(36))
    SLF_SOSourceType = Column(SMALLINT)
    SLF_FirstMsgType = Column(INTEGER)
    SLF_FirstProductID = Column(INTEGER)
    SLF_FirstSourceEntityGUID = Column(CHAR(36))
    SLF_FirstAction = Column(SMALLINT)
    SLF_FirstUTCTime = Column(DATETIME)
    SLF_LatestMsgType = Column(INTEGER)
    SLF_LatestProductID = Column(INTEGER)
    SLF_LatestSourceEntityGUID = Column(CHAR(36))
    SLF_LatestAction = Column(SMALLINT)
    SLF_LatestUTCTime = Column(DATETIME)
