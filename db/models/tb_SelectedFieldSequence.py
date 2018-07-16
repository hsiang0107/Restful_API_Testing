from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER, VARCHAR


class TbSelectedFieldSequence(Base):
    __tablename__ = 'tb_SelectedFieldSequence'
    SFS_CustomViewID = Column(CHAR(36), primary_key=True, nullable=False)
    SFS_FieldID = Column(VARCHAR(64), nullable=False)
    SFS_SequenceNum = Column(INTEGER, nullable=False)
