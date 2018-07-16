from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE, INTEGER, NVARCHAR, VARCHAR


class TbTVCSCommandList(Base):
    __tablename__ = 'tb_TVCSCommandList'
    CMD_CommandID = Column(CHAR(36), primary_key=True)
    CMD_GenDateTime = Column(DATETIME)
    CMD_RedAlertID = Column(CHAR(32))
    CMD_Processed = Column(INTEGER)
    CMD_TargetType = Column(INTEGER)
    CMD_IsSingleProductCmd = Column(INTEGER)
    CMD_ProductList = Column(VARCHAR(1024))
    CMD_Folders = Column(VARCHAR(2048))
    CMD_LoginToken = Column(VARCHAR(3072))
    CMD_Template = Column(IMAGE)
    CMD_Doable = Column(INTEGER)
    CMD_MsgID = Column(INTEGER)
    CMD_UserID = Column(NVARCHAR(64))
    CMD_NoFilter = Column(INTEGER)
    CMD_UIVersion = Column(VARCHAR(8))
    CMD_DataID = Column(VARCHAR(128))
    CMD_MsgBLOB = Column(IMAGE)
    CMD_MsgBLOBSize = Column(INTEGER)
    CMD_IsHidden = Column(INTEGER)
