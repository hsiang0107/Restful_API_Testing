from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbPolicyMode(Base):
    __tablename__ = 'tb_PolicyMode'
    PM_Mode = Column(INTEGER, primary_key=True, nullable=False)
    PM_PolicyID = Column(VARCHAR(128), nullable=False)
