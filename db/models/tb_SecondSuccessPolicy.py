from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER


class TbSecondSuccessPolicy(Base):
    __tablename__ = 'tb_SecondSuccessPolicy'
    SSP_EnableOccurFreqPerNHour = Column(BIT, primary_key=True)
    SSP_EnableTotalExceededVirus = Column(BIT, primary_key=True)
    SSP_EnableTotalExceededDest = Column(BIT, primary_key=True)
    SSP_OccurFrequencyPerNHour = Column(INTEGER)
    SSP_TotalExceededVirus = Column(INTEGER)
    SSP_TotalExceededDestinations = Column(INTEGER)
