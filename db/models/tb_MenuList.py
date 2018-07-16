from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER, NVARCHAR, VARCHAR


class TbMenuList(Base):
    __tablename__ = 'tb_MenuList'
    SeqId = Column(INTEGER, primary_key=True, nullable=False)
    MenuId = Column(VARCHAR(10), nullable=False)
    ParentMenuId = Column(VARCHAR(10))
    Title = Column(NVARCHAR(256))
    Alias = Column(NVARCHAR(256))
    Link = Column(NVARCHAR(1024))
    LeftIndex = Column(INTEGER, nullable=False)
    RightIndex = Column(INTEGER, nullable=False)
    Underbar = Column(BIT)
    IsActive = Column(BIT)
    IsPlugIn = Column(INTEGER)
    Target = Column(VARCHAR(64))
