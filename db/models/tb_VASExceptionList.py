from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, VARCHAR


class TbVASExceptionList(Base):
    __tablename__ = 'tb_VASExceptionList'
    VAS_ExceptionListID = Column(INTEGER, primary_key=True, nullable=False)
    VAS_Properties = Column(INTEGER, nullable=False)
    VAS_HostName = Column(NVARCHAR(64), nullable=False)
    VAS_IPAddress1 = Column(VARCHAR(256), nullable=False)
    VAS_IPAddress2 = Column(VARCHAR(256), nullable=False)
