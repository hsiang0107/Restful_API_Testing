from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, INTEGER, NVARCHAR


class TbExternalWebServiceCallLog(Base):
    __tablename__ = 'tb_ExternalWebServiceCallLog'
    id = Column(BIGINT, primary_key=True, nullable=False)
    CallUTCDate = Column(DATETIME, nullable=False)
    InvokedClassName = Column(NVARCHAR(200))
    InvokedMethodName = Column(NVARCHAR(200))
    RemoteADDR = Column(NVARCHAR(100))
    AuthToken = Column(NVARCHAR)
    ApplicationID = Column(NVARCHAR(50))
    ApplicationName = Column(NVARCHAR(200))
    HTTPMethod = Column(NVARCHAR(50))
    RawUrl = Column(NVARCHAR)
    HTTPHeaders = Column(NVARCHAR)
    RequestBody = Column(NVARCHAR)
    ResponseHttpStatusCode = Column(INTEGER)
    ResponseResultCode = Column(INTEGER)
    RecordUTCDate = Column(DATETIME, nullable=False)
