from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbEntityPRInfo(Base):
    __tablename__ = 'tb_EntityPRInfo'
    EI_EntityID = Column(CHAR(36), primary_key=True, nullable=False)
    EI_AC = Column(VARCHAR(31), primary_key=True, nullable=False)
    EI_PRProfile = Column(VARCHAR(160))
    EI_LastUpdateTime = Column(DATETIME)
    EI_PRState = Column(INTEGER)
    EI_ExpiredDate = Column(DATETIME)
    EI_Description = Column(NVARCHAR(1024))
    EI_SlotID = Column(INTEGER, primary_key=True)
