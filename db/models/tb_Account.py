from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, SMALLINT


class TbAccount(Base):
    __tablename__ = 'tb_Account'
    Guid = Column(CHAR(36), primary_key=True, nullable=False)
    id = Column(NVARCHAR(256), nullable=False)
    Type = Column(INTEGER, nullable=False)
    Category = Column(INTEGER, nullable=False)
    DisplayName = Column(NVARCHAR(256))
    CreateTime = Column(DATETIME)
    CreatorGuid = Column(CHAR(36))
    CMGuid = Column(CHAR(36))
    IsDLPComplianceOfficer = Column(SMALLINT)
    AccountPermission = Column(SMALLINT)

    @classmethod
    def find_by_id(cls, name):
        return cm_session.query(cls).filter(cls.id == name).first()
