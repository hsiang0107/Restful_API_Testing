from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbCasPolicyInfo(Base):
    __tablename__ = 'tb_CasPolicyInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    CPI_CMGuid = Column(CHAR(36))
    CPI_PolicyGUID = Column(CHAR(36))
    CPI_EntityID = Column(CHAR(36))
    CPI_DisplayName = Column(NVARCHAR(256))
    CPI_PolicyType = Column(VARCHAR(32))
    CPI_Status = Column(SMALLINT)
