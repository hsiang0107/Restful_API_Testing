from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbCommandPRInfo(Base):
    __tablename__ = 'tb_CommandPRInfo'
    CT_ID = Column(CHAR(36), primary_key=True, nullable=False)
    CT_AC = Column(VARCHAR(31), primary_key=True, nullable=False)
    CT_PRProfile = Column(VARCHAR(160))
    CT_ErrorCode = Column(INTEGER)
