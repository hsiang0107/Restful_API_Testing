from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, VARCHAR


class TbsCloudPolicyWcuResourceMapping(Base):
    __tablename__ = 'tb_sCloudPolicyWcuResourceMapping'
    id = Column(BIGINT, primary_key=True, nullable=False)
    ProductId = Column(VARCHAR(12), nullable=False)
    PolicyId = Column(CHAR(36), nullable=False)
    WcuName = Column(VARCHAR(50), nullable=False)
    ResourceId = Column(VARCHAR(72), nullable=False)
    CreateTime = Column(DATETIME, nullable=False)
