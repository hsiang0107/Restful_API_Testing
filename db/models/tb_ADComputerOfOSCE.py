from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, SMALLINT, UNIQUEIDENTIFIER, VARCHAR


class TbADComputerOfOSCE(Base):
    __tablename__ = 'tb_ADComputerOfOSCE'
    id = Column(INTEGER, primary_key=True, nullable=False)
    GUID = Column(UNIQUEIDENTIFIER, nullable=False)
    Engine = Column(VARCHAR(20))
    Pattern = Column(VARCHAR(20))
    PatternLUT = Column(DATETIME)
    ProgramVersion = Column(VARCHAR(20))
    VDI = Column(SMALLINT)
    SettingID = Column(INTEGER, nullable=False)
