from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR


class TbRegTmpTreeNode(Base):
    __tablename__ = 'tb_RegTmp_TreeNode'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Guid = Column(CHAR(36))
    Type = Column(INTEGER)
    DisplayName = Column(NVARCHAR(64))
    ParentGuid = Column(CHAR(36))
    IconName = Column(NVARCHAR(128))
    ProductType = Column(INTEGER)
    RelativePath = Column(NVARCHAR(4000))
