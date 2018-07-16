from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, BINARY, DATETIME, NVARCHAR


class TbInventorySecurityToUserDataMD5Map(Base):
    __tablename__ = 'tb_Inventory_Security_To_User_DataMD5Map'
    id = Column(BIGINT, primary_key=True, nullable=False)
    Data = Column(NVARCHAR(2048))
    Data_MD5 = Column(BINARY(16))
    DataNormalized_MD5 = Column(BINARY(16))
    LastUpdateTime = Column(DATETIME)
