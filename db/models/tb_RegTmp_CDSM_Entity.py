from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, INTEGER, SMALLINT, VARCHAR


class TbRegTmpCDSMEntity(Base):
    __tablename__ = 'tb_RegTmp_CDSM_Entity'
    id = Column(INTEGER, primary_key=True, nullable=False)
    guid = Column(BINARY(16))
    agent_guid = Column(BINARY(16))
    parent_guid = Column(BINARY(16))
    name = Column(VARCHAR(64))
    type = Column(INTEGER)
    certificate = Column(VARCHAR(80))
    folder_id = Column(INTEGER)
    reg_time = Column(INTEGER)
    update_time = Column(INTEGER)
    product_id = Column(VARCHAR(64))
    product_version = Column(VARCHAR(20))
    menu_version = Column(VARCHAR(20))
    status = Column(INTEGER)
    tms_no = Column(SMALLINT)
    tms = Column(BINARY(132))
    token = Column(VARCHAR(1024))
    off_hour = Column(BINARY(12))
    heartbeat_mode = Column(INTEGER)
    heartbeat_freq = Column(INTEGER)
    event_list = Column(BINARY(400))
    code_page = Column(VARCHAR(20))
    icon_name = Column(VARCHAR(127))
    guid_t = Column(VARCHAR(36))
    agent_guid_t = Column(VARCHAR(36))
    parent_guid_t = Column(VARCHAR(36))
    ri4 = Column(BINARY(40))
    reserve = Column(BINARY(64))
    generation = Column(INTEGER)
    polling_freq = Column(INTEGER)
    icon_index = Column(INTEGER)
