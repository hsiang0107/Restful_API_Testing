from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbCriticalEventFilterCategoryRelation(Base):
    __tablename__ = 'tb_CriticalEventFilterCategoryRelation'
    id = Column(INTEGER, primary_key=True, nullable=False)
    CE_FilterID = Column(VARCHAR(35))
    CE_CategoryID = Column(VARCHAR(1))
