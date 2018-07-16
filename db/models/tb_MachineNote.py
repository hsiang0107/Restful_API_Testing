from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT


class TbMachineNote(Base):
    __tablename__ = 'tb_MachineNote'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MachineGUID = Column(CHAR(36), nullable=False)
    Type = Column(SMALLINT, nullable=False)
    Content = Column(NVARCHAR(1024))
    Username = Column(NVARCHAR(256))
    Time = Column(DATETIME)
