from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, VARCHAR


class TbPolicyTemplate(Base):
    __tablename__ = 'tb_PolicyTemplate'
    PT_ID = Column(VARCHAR(128), primary_key=True, nullable=False)
    PT_SourceType = Column(INTEGER)
    PT_SourceName = Column(VARCHAR(128))
    PT_Filename = Column(VARCHAR(128))
    PT_DisplayName = Column(NVARCHAR(128))
