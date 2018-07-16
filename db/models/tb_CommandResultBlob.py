from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, IMAGE


class TbCommandResultBlob(Base):
    __tablename__ = 'tb_CommandResultBlob'
    TrackingID = Column(CHAR(36), primary_key=True, nullable=False)
    CommandID = Column(CHAR(36))
    LastUpdateTime = Column(DATETIME)
    Blob = Column(IMAGE)
