from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER


class TbCascadingStatus(Base):
    __tablename__ = 'tb_CascadingStatus'
    IsChild = Column(BIT, primary_key=True)
    ParentCMVersion = Column(INTEGER, primary_key=True)
    ParentCMMinorVersion = Column(INTEGER)
    ParentCMBuild = Column(INTEGER)
