from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, INTEGER, VARCHAR


class Tbstatuslogjournalproductinfo(Base):
    __tablename__ = 'tb_statuslogjournalproductinfo'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36), nullable=False)
    SLF_ProductVersion = Column(CHAR(16))
    SLF_MenuVersion = Column(VARCHAR(8))
    SLF_ProductBuildNumber = Column(INTEGER)
    SLF_ProductLanguageCode = Column(INTEGER)
    lutontmcm = Column(DATETIME)
