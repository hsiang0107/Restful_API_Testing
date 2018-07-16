from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbSystemConfiguration(Base):
    __tablename__ = 'tb_SystemConfiguration'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Name = Column(VARCHAR(256), nullable=False)
    Value = Column(VARCHAR(4096), nullable=False)
