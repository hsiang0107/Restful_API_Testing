from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER, VARCHAR


class TbUpdatesSelectedFilters(Base):
    __tablename__ = 'tb_Updates_Selected_Filters'
    id = Column(INTEGER, primary_key=True, nullable=False)
    FilterType = Column(VARCHAR(16), nullable=False)
    Value = Column(VARCHAR(128), nullable=False)
    IsSchedule = Column(BIT, nullable=False)
