from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, DATETIME, INTEGER


class TbVirusOutbreakPolicy(Base):
    __tablename__ = 'tb_VirusOutbreakPolicy'
    VOP_EnableOccurFreqPerNHour = Column(BIT, primary_key=True, nullable=False)
    VOP_EnableTotalExceededVirus = Column(BIT, primary_key=True, nullable=False)
    VOP_EnableTotalExceededDest = Column(BIT, primary_key=True, nullable=False)
    VOP_OccurFrequencyPerNHour = Column(INTEGER, nullable=False)
    VOP_TotalExceededVirus = Column(INTEGER, nullable=False)
    VOP_TotalExceededDestinations = Column(INTEGER, nullable=False)
    VOP_PreventSpamNHour = Column(INTEGER)
    VOP_LastAccumulationTime = Column(DATETIME)
