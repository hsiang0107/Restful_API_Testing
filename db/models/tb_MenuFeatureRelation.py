from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import VARCHAR


class TbMenuFeatureRelation(Base):
    __tablename__ = 'tb_MenuFeatureRelation'
    FeatureKey = Column(VARCHAR(32), primary_key=True, nullable=False)
    MenuId = Column(VARCHAR(10), primary_key=True, nullable=False)
