from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, VARCHAR


class TbSelectedTreeNodes(Base):
    __tablename__ = 'tb_SelectedTreeNodes'
    STN_NodeGuid = Column(CHAR(36), primary_key=True, nullable=False)
    STN_ReferenceKey = Column(VARCHAR(261), nullable=False)
