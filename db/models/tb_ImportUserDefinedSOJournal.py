from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class TbImportUserDefinedSOJournal(Base):
    __tablename__ = 'tb_ImportUserDefinedSOJournal'
    id = Column(BIGINT, primary_key=True, nullable=False)
    SLF_Type = Column(INTEGER, nullable=False)
    SLF_Data = Column(NVARCHAR, nullable=False)
    SLF_URLCorrelationKey = Column(VARCHAR(64))
    ScanAction = Column(SMALLINT, nullable=False)
    UserDefinedNotes = Column(NVARCHAR)
    OperationType = Column(INTEGER, nullable=False)
    FilterCRC = Column(VARCHAR(64))
    UploadedBy = Column(NVARCHAR(256))
    UploadChannel = Column(SMALLINT)
    IOCsFileHashID = Column(VARCHAR(256))
