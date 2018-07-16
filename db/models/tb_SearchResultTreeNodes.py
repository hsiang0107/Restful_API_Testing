from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR


class TbSearchResultTreeNodes(Base):
    __tablename__ = 'tb_SearchResultTreeNodes'
    SRTN_ReferenceKey = Column(CHAR(36), primary_key=True, nullable=False)
    SRTN_NodeGuid = Column(CHAR(36), nullable=False)
