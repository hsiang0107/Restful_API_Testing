from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER, VARCHAR


class TbPolicySupportVersionInfo(Base):
    __tablename__ = 'tb_PolicySupportVersionInfo'
    ProductType = Column(INTEGER, primary_key=True, nullable=False)
    NodeType = Column(INTEGER, primary_key=True, nullable=False)
    Version = Column(VARCHAR(19))
    BuildNumber = Column(VARCHAR(24))
    IsLastVersion = Column(BIT, nullable=False)
    EnablePolicyByPLS = Column(BIT)
    IsDLPProduct = Column(BIT)
