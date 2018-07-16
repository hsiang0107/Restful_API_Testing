from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR


class TbCasVirtualUserList(Base):
    __tablename__ = 'tb_CasVirtualUserList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    CVUL_CMGuid = Column(CHAR(36))
    CVUL_GUID = Column(CHAR(36))
    CVUL_SAMAccountName = Column(NVARCHAR(32))
    CVUL_Domain = Column(NVARCHAR(256))
