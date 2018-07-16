from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import VARCHAR


class TbUserAddressBook(Base):
    __tablename__ = 'tb_UserAddressBook'
    USER_ID = Column(VARCHAR(64), primary_key=True, nullable=False)
