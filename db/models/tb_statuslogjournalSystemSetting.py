from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, NVARCHAR, SMALLINT


class TbstatuslogjournalSystemSetting(Base):
    __tablename__ = 'tb_statuslogjournalSystemSetting'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_ProductGUID = Column(CHAR(36))
    SettingKind = Column(SMALLINT, nullable=False)
    SettingValue = Column(NVARCHAR(256), nullable=False)
