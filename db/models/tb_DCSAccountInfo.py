from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, NVARCHAR, VARCHAR


class TbDCSAccountInfo(Base):
    __tablename__ = 'tb_DCSAccountInfo'
    AccountInfoID = Column(INTEGER, primary_key=True, nullable=False)
    DomainName = Column(NVARCHAR(16), nullable=False)
    Username = Column(VARCHAR(64), nullable=False)
    Password = Column(VARCHAR(128), nullable=False)
    EMailAddress = Column(VARCHAR(64))
    Description = Column(VARCHAR(128))
    Properties = Column(INTEGER)
