from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BINARY, CHAR, INTEGER, NVARCHAR, VARCHAR


class TbCDSMEntityCascading(Base):
    __tablename__ = 'tb_CDSM_Entity_Cascading'
    guid = Column(CHAR(36), primary_key=True, nullable=False)
    parent_guid = Column(CHAR(36))
    dm_guid = Column(CHAR(36))
    name = Column(VARCHAR(64))
    type = Column(INTEGER)
    folder_id = Column(INTEGER)
    product_id = Column(VARCHAR(64))
    product_version = Column(VARCHAR(20))
    menu_version = Column(VARCHAR(20))
    status = Column(INTEGER)
    code_page = Column(VARCHAR(20))
    icon_name = Column(VARCHAR(127))
    ri4 = Column(BINARY(40))
    cm_guid = Column(CHAR(36))
    type_in_tree = Column(INTEGER)
    name_in_tree = Column(NVARCHAR(64))
    parent_guid_in_tree = Column(CHAR(36))
