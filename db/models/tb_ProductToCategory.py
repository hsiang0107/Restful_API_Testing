from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER


class TbProductToCategory(Base):
    __tablename__ = 'tb_ProductToCategory'
    ID_ProductType = Column(INTEGER, primary_key=True, nullable=False)
    ID_ProductCategory = Column(INTEGER)
