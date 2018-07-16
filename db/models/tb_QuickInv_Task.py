from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, CHAR, DATETIME, BIT, NVARCHAR, SMALLINT, VARCHAR, BINARY, TINYINT


class TbQuickInvTask(Base):
    __tablename__ = 'tb_QuickInv_Task'
    id = Column(BIGINT, primary_key=True, nullable=False)
    TaskID = Column(CHAR(36))
    HasMore = Column(BIT)
    LastContentID = Column(NVARCHAR(2048))
    Criteria = Column(NVARCHAR(2048))
    CriteriaType = Column(SMALLINT)
    RetroScanData_MD5 = Column(BINARY(16))
    RetroScanCategory = Column(TINYINT)
    SLF_Key = Column(VARCHAR(256))
    IsManual = Column(BIT)
    CreationTime = Column(DATETIME)
    LastUpdateTime = Column(DATETIME)
    IsTimeout = Column(BIT)

    @classmethod
    def find_by_criteria(cls, criteria):
        return cm_session.query(cls).filter(cls.Criteria == criteria).first()

    @classmethod
    def get_distinct_taskid(cls):
        return cm_session.query(cls).distinct(cls.TaskID).count()
