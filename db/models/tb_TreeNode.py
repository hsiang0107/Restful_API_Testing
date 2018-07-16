from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT


class TbTreeNode(Base):
    __tablename__ = 'tb_TreeNode'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Guid = Column(CHAR(36), nullable=False)
    ParentGuid = Column(CHAR(36), ForeignKey('tb_TreeNode.Guid'))
    Type = Column(INTEGER, nullable=False)
    ProductType = Column(INTEGER)
    DisplayName = Column(NVARCHAR(64), nullable=False)
    IconName = Column(NVARCHAR(128), nullable=False)
    LastUpdateTime = Column(DATETIME)
    PolicyGuid = Column(CHAR(36))
    PolicyLock = Column(SMALLINT)
    OriginalPolicyGuid = Column(CHAR(36))
    parent = relationship("TbTreeNode", remote_side=[Guid])

    @classmethod
    def find_by_displayname(cls, display_name):
        return cm_session.query(cls).filter(cls.DisplayName == display_name).first()

    @classmethod
    def get_parent_tree_node(cls, parent_name, product_name):
        parent_tree_node = cm_session.query(cls).filter(cls.DisplayName == parent_name). \
            join(cls.parent, aliased=True). \
            filter(cls.DisplayName == product_name). \
            first()
        return parent_tree_node

    @classmethod
    def get_server_info(cls, display_name, product_type=None):
        command = 'select A.ProductType, case A.[Type] when 2 then A.[Guid] when 4 then B.ParentGuid END ' + \
                  'as ProductGuid, A.Guid as EntityID from tb_TreeNode as A with(nolock) ' + \
                  'inner join tb_TreeNode as B with(nolock) on A.ParentGuid = B.Guid ' + \
                  'where A.DisplayName = \'%s\'' % display_name
        if product_type:
            command += ' AND A.ProductType = \'%s\'' % product_type

        return cm_session.execute(command).fetchone()

    def __str__(self):
        return "tb_TreeNode DisplayName is %s" % self.DisplayName
