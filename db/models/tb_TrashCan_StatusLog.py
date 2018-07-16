from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, NVARCHAR, VARCHAR


class TbTrashCanStatusLog(Base):
    __tablename__ = 'tb_TrashCan_StatusLog'
    id = Column(BIGINT, primary_key=True, nullable=False)
    Timestamp = Column(DATETIME)
    SourceTableName = Column(VARCHAR(64))
    SeqIdInSourceTable = Column(BIGINT)
    ProductGuid = Column(CHAR(36))
    Data = Column(NVARCHAR)
