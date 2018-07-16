from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbNtfUserGROUP(Base):
    __tablename__ = 'tb_NtfUserGROUP'
    GROUP_ID = Column(VARCHAR(64), primary_key=True, nullable=False)
    Add_EMailAddress = Column(VARCHAR(1025))
    Add_MobilePhoneNumber = Column(VARCHAR(257))
    Add_PagerNumber = Column(VARCHAR(257))
    UserNum = Column(INTEGER)
