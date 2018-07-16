from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, NVARCHAR, VARCHAR


class TbLoginUserSessionData(Base):
    __tablename__ = 'tb_LoginUserSessionData'
    id = Column(CHAR(36), primary_key=True, nullable=False)
    LUSD_LoginToken = Column(VARCHAR(255), nullable=False)
    LUSD_SessionTableName = Column(VARCHAR(255), nullable=False)
    LUSD_Expired = Column(BIT, nullable=False)
    LUSD_CreateTime = Column(DATETIME)
    LUSD_UserID = Column(NVARCHAR(255))
