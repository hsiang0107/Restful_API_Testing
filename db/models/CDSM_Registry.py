from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, TEXT, VARCHAR


class CDSMRegistry(Base):
    __tablename__ = 'CDSM_Registry'
    cdsm_id = Column(INTEGER, primary_key=True, nullable=False)
    cdsm_key = Column(VARCHAR(900), nullable=False)
    cdsm_level = Column(INTEGER, nullable=False)
    cdsm_timestamp = Column(INTEGER, nullable=False)
    cdsm_xml = Column(TEXT(2147483647), nullable=False)
