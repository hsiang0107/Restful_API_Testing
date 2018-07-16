from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbPRIConfiguration(Base):
    __tablename__ = 'tb_PRI_Configuration'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Name = Column(VARCHAR(256))
    Value = Column(VARCHAR(4096))
