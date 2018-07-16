from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import INTEGER, VARCHAR


class TbLanguageCodeRelation(Base):
    __tablename__ = 'tb_LanguageCodeRelation'
    SQL_LanguageID = Column(INTEGER, primary_key=True, nullable=False)
    Server_LanguageCode = Column(VARCHAR(10), nullable=False)
    UI_LanguageCode = Column(VARCHAR(10), nullable=False)
