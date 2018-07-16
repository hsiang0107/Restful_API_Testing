from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER


class TbRegistrationJournal(Base):
    __tablename__ = 'tb_RegistrationJournal'
    id = Column(INTEGER, primary_key=True, nullable=False)
    guid = Column(CHAR(36), nullable=False)
    parent_guid = Column(CHAR(36), nullable=False)
    operation = Column(INTEGER, nullable=False)
    lutontmcm = Column(DATETIME, nullable=False)
    parententitytype = Column(INTEGER)
