from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbWebSecurityLogCategory(Base):
    __tablename__ = 'tb_WebSecurityLogCategory'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MsgLogID = Column(CHAR(36))
    SLF_CategoryID = Column(INTEGER)
    CE_FilterID = Column(VARCHAR(35))
