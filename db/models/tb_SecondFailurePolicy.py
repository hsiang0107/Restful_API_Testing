from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER


class TbSecondFailurePolicy(Base):
    __tablename__ = 'tb_SecondFailurePolicy'
    SFP_EnableOccurFreqPerNHour = Column(BIT, primary_key=True)
    SFP_EnableTotalExceededVirus = Column(BIT, primary_key=True)
    SFP_EnableTotalExceededDest = Column(BIT, primary_key=True)
    SFP_OccurFrequencyPerNHour = Column(INTEGER)
    SFP_TotalExceededVirus = Column(INTEGER)
    SFP_TotalExceededDestinations = Column(INTEGER)
