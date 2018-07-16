from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, VARCHAR


class TbGroupMapIPs(Base):
    __tablename__ = 'tb_GroupMapIPs'
    GN_GUID = Column(CHAR(36), primary_key=True, nullable=False)
    Group_name = Column(VARCHAR(32), nullable=False)
    Start_IP = Column(VARCHAR(128), nullable=False)
    End_IP = Column(VARCHAR(128), nullable=False)
    Start_IP_2 = Column(VARCHAR(128))
    End_IP_2 = Column(VARCHAR(128))
    Start_IP_3 = Column(VARCHAR(128))
    End_IP_3 = Column(VARCHAR(128))
