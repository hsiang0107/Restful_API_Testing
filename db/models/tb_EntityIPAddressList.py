from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, VARCHAR


class TbEntityIPAddressList(Base):
    __tablename__ = 'tb_EntityIPAddressList'
    EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    IPAddressList = Column(VARCHAR(1024))
