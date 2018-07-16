from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, SMALLINT, VARCHAR


class TbInvestigateEntryPointSetting(Base):
    __tablename__ = 'tb_InvestigateEntryPointSetting'
    id = Column(INTEGER, primary_key=True, nullable=False)
    IPAddress = Column(VARCHAR(256), nullable=False)
    Protocol = Column(VARCHAR(16), nullable=False)
    PortList = Column(VARCHAR(128), nullable=False)
    Direction = Column(SMALLINT, nullable=False)
