from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbCheckCascadingEntityUpdate(Base):
    __tablename__ = 'tb_CheckCascadingEntityUpdate'
    Guid = Column(CHAR(36), primary_key=True, nullable=False)
    CMGuid = Column(CHAR(36), primary_key=True, nullable=False)
    NeedUpdate = Column(INTEGER, nullable=False)
