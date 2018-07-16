from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER


class TbFirstSuccessPolicy(Base):
    __tablename__ = 'tb_FirstSuccessPolicy'
    FSP_EnableOccurFreqPerNHour = Column(BIT, primary_key=True)
    FSP_EnableTotalExceededVirus = Column(BIT)
    FSP_EnableTotalExceededDest = Column(BIT)
    FSP_OccurFrequencyPerNHour = Column(INTEGER)
    FSP_TotalExceededVirus = Column(INTEGER)
    FSP_TotalExceededDestinations = Column(INTEGER)
