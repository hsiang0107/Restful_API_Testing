from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, TINYINT, DATETIME, BINARY


class TbInventoryQuickInvScanMapping(Base):
    __tablename__ = 'tb_Inventory_QuickInvScanMapping'
    id = Column(BIGINT, primary_key=True, nullable=False)
    EventContent_MD5 = Column(BINARY(16), nullable=False)
    RetroScanData_MD5 = Column(BINARY(16), nullable=False)
    RetroScanCategory = Column(TINYINT, nullable=False)
    LastUpdateTime = Column(DATETIME, nullable=False)

    @classmethod
    def find_by_retroscandata_md5(cls, md5):
        return cm_session.query(cls).filter(cls.RetroScanData_MD5 == md5).first()
