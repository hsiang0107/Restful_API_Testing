from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbSysLogServerInfo(Base):
    __tablename__ = 'tb_SysLogServerInfo'
    IP = Column(VARCHAR(130), nullable=False)
    Port = Column(INTEGER, nullable=False)
    id = Column(VARCHAR(140), primary_key=True, nullable=False)
