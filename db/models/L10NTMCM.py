from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, VARCHAR


class L10NTMCM(Base):
    __tablename__ = 'L10NTMCM'
    id = Column(INTEGER, primary_key=True, nullable=False)
    category = Column(INTEGER, nullable=False)
    idmap = Column(INTEGER)
    symbolic = Column(VARCHAR(128))
    displayname = Column(NVARCHAR(2048))
    lang = Column(VARCHAR(16))
