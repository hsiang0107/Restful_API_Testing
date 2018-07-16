from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, VARCHAR


class TbRegisteredProductList(Base):
    __tablename__ = 'tb_RegisteredProductList'
    RPL_ID = Column(CHAR(36), primary_key=True, nullable=False)
    RPL_ProductType = Column(INTEGER, nullable=False)
    RPL_Version = Column(VARCHAR(19), nullable=False)
    RPL_Language = Column(INTEGER, nullable=False)
    RPL_Platform = Column(INTEGER, nullable=False)
    RPL_TotalCount = Column(INTEGER, nullable=False)
    RPL_ProductInfoState = Column(INTEGER, nullable=False)
    RPL_RetryTime = Column(DATETIME, nullable=False)
    RPL_MenuVersion = Column(VARCHAR(8))
    RPL_BuildNumber = Column(INTEGER)
