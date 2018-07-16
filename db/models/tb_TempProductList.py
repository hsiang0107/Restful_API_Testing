from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER


class TbTempProductList(Base):
    __tablename__ = 'tb_TempProductList'
    Product_ID = Column(INTEGER, primary_key=True, nullable=False)
