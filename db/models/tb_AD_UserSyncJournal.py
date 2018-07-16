from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR


class TbADUserSyncJournal(Base):
    __tablename__ = 'tb_AD_UserSyncJournal'
    id = Column(INTEGER, primary_key=True, nullable=False)
    LUT = Column(DATETIME, nullable=False)
    Status = Column(INTEGER)
    Remark = Column(NVARCHAR(256))
