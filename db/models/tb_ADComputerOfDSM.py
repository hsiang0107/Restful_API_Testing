from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, SMALLINT


class TbADComputerOfDSM(Base):
    __tablename__ = 'tb_ADComputerOfDSM'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Name = Column(NVARCHAR(254), nullable=False)
    DSVA = Column(SMALLINT)
    SecurityProfile = Column(NVARCHAR(254))
    EsxServerName = Column(NVARCHAR(254))
    SettingID = Column(INTEGER, nullable=False)
