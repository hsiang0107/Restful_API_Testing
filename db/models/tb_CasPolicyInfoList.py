from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbCasPolicyInfoList(Base):
    __tablename__ = 'tb_CasPolicyInfoList'
    id = Column(INTEGER, primary_key=True, nullable=False)
    CPIL_CMGuid = Column(CHAR(36))
    CPIL_PolicyGUID = Column(CHAR(36))
    CPIL_EntityID = Column(CHAR(36))
    CPIL_DisplayName = Column(NVARCHAR(256))
    CPIL_PolicyType = Column(VARCHAR(32))
    CPIL_Status = Column(SMALLINT)
