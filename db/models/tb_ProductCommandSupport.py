from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbProductCommandSupport(Base):
    __tablename__ = 'tb_ProductCommandSupport'
    id = Column(INTEGER, primary_key=True, nullable=False)
    ProductID = Column(INTEGER)
    ProductVersion = Column(VARCHAR(36))
    MenuVersion = Column(VARCHAR(36))
    CommandItem = Column(VARCHAR(256))
    CommandID = Column(VARCHAR(36))
    ProductLanguage = Column(VARCHAR(36))
    Parameters = Column(VARCHAR(1024))
