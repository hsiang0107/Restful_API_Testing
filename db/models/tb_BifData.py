from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, VARCHAR


class TbBifData(Base):
    __tablename__ = 'tb_BifData'
    Type = Column(VARCHAR(50), primary_key=True, nullable=False)
    BIFKey = Column(VARCHAR(1024), primary_key=True, nullable=False)
    BIFValue = Column(VARCHAR)
    BIFRemark = Column(VARCHAR)
    BIFAccountGuid = Column(CHAR(36))
    LastUpdateTime = Column(DATETIME)
