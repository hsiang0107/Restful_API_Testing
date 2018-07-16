from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR


class TbIMSSData(Base):
    __tablename__ = 'tb_IMSSData'
    CLF_EntityID = Column(CHAR(36), primary_key=True)
    CLF_ProductType = Column(INTEGER)
    CLF_LogReceivedTime = Column(DATETIME)
    SL_FilterType = Column(INTEGER)
    SL_Recipient = Column(NVARCHAR(256))
    SL_Domain = Column(NVARCHAR(256))
    SL_Count = Column(INTEGER)
