from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR, VARCHAR


class TbRedAlertTamMsgBoard(Base):
    __tablename__ = 'tb_RedAlertTamMsgBoard'
    RATMB_ID = Column(CHAR(36), primary_key=True, nullable=False)
    RATMB_TamVersion = Column(VARCHAR(64))
    RATMB_AutoRedAlert = Column(INTEGER)
    RATMB_ActiveRedAlertOfAU = Column(CHAR(36))
    RATMB_MsgXmlStream = Column(NVARCHAR(3072), nullable=False)
    RATMB_LUT = Column(DATETIME)
    RATMB_SrvcMsgBrd = Column(IMAGE)
    RATMB_RAModeCmpToDep = Column(INTEGER)
