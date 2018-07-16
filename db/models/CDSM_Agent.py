from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, INTEGER, SMALLINT, VARCHAR


class CDSMAgent(Base):
    __tablename__ = 'CDSM_Agent'
    guid = Column(BINARY(16), primary_key=True, nullable=False)
    reg_time = Column(INTEGER)
    version = Column(INTEGER)
    last_heartbeat = Column(INTEGER)
    name = Column(VARCHAR(64))
    time_zone = Column(INTEGER)
    status = Column(INTEGER)
    os_type = Column(INTEGER)
    os_version = Column(INTEGER)
    cpu_type = Column(SMALLINT)
    off_hour = Column(BINARY(12))
    token = Column(VARCHAR(1024))
    ip = Column(BINARY(256))
    fqdn = Column(VARCHAR(80))
    code_page = Column(VARCHAR(20))
    guid_t = Column(VARCHAR(36))
    ri4 = Column(BINARY(40))
    reserve = Column(BINARY(64))
    generation = Column(INTEGER)
    os_type_t = Column(VARCHAR(128))
    os_version_t = Column(VARCHAR(32))
    version_t = Column(VARCHAR(32))
    build_t = Column(VARCHAR(32))
