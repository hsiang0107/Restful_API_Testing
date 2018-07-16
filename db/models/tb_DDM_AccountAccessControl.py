from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, NVARCHAR, SMALLINT


class TbDDMAccountAccessControl(Base):
    __tablename__ = 'tb_DDM_AccountAccessControl'
    Guid = Column(CHAR(36), primary_key=True, nullable=False)
    FeatureID = Column(INTEGER, nullable=False)
    SegmentID = Column(INTEGER, nullable=False)
    Value = Column(NVARCHAR)
    Permission = Column(SMALLINT, nullable=False)
