from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR


class TbSingleSignOnUserInfo(Base):
    __tablename__ = 'tb_SingleSignOnUserInfo'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ProductType = Column(INTEGER, nullable=False)
    SingleSignOnUserID = Column(NVARCHAR(64), nullable=False)
