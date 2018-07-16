from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbUserAccessLog(Base):
    __tablename__ = 'tb_UserAccessLog'
    id = Column(INTEGER, primary_key=True, nullable=False)
    Time = Column(DATETIME, nullable=False)
    EventType = Column(INTEGER, nullable=False)
    UserGuid = Column(VARCHAR(36))
    UserID = Column(NVARCHAR(64))
    ImpersonatedADGroupName = Column(VARCHAR(256))
    Result = Column(INTEGER, nullable=False)
    Description = Column(NVARCHAR(1024))

    @classmethod
    def find_records_by_event_type(cls, event_type):
        return cm_session.query(cls).filter(cls.EventType == event_type).all()
