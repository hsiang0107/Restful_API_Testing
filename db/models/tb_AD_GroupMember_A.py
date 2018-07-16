from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR


class TbADGroupMemberA(Base):
    __tablename__ = 'tb_AD_GroupMember_A'
    GroupGuid = Column(CHAR(36), nullable=False)
    UserGuid = Column(CHAR(36), primary_key=True, nullable=False)
    GroupLevel = Column(CHAR(36))
