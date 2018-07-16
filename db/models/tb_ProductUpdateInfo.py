from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, VARCHAR


class TbProductUpdateInfo(Base):
    __tablename__ = 'tb_ProductUpdateInfo'
    ActiveUpdateID = Column(INTEGER, primary_key=True, nullable=False)
    Language = Column(INTEGER, primary_key=True, nullable=False)
    Platform = Column(INTEGER, primary_key=True, nullable=False)
    Version = Column(VARCHAR(64))
    LastUpdateUTCTime = Column(DATETIME)
