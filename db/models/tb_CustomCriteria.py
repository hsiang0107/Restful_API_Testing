from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, INTEGER, NVARCHAR, VARCHAR


class TbCustomCriteria(Base):
    __tablename__ = 'tb_CustomCriteria'
    CC_ID = Column(CHAR(36), primary_key=True, nullable=False)
    CC_CustomViewID = Column(CHAR(36), nullable=False)
    CC_FieldID = Column(VARCHAR(64), nullable=False)
    CC_OperatorID = Column(VARCHAR(64), nullable=False)
    CC_Value = Column(NVARCHAR(512), nullable=False)
    CC_ValueType = Column(INTEGER)
    CC_MatchCondition = Column(BIT, nullable=False)
    CC_Type = Column(INTEGER)
