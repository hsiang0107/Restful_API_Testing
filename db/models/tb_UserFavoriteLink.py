from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbUserFavoriteLink(Base):
    __tablename__ = 'tb_UserFavoriteLink'
    SeqId = Column(INTEGER, primary_key=True, nullable=False)
    UserGuid = Column(CHAR(36), nullable=False)
    MenuId = Column(VARCHAR(10), nullable=False)
