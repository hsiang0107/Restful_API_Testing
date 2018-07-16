from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, DATETIME, INTEGER


class TbNetworkOutbreakPolicy(Base):
    __tablename__ = 'tb_NetworkOutbreakPolicy'
    VOP_EnableOccurFreqPerNHour = Column(BIT, primary_key=True)
    VOP_EnableTotalExceededVirus = Column(BIT)
    VOP_EnableTotalExceededDest = Column(BIT)
    VOP_OccurFrequencyPerNHour = Column(INTEGER)
    VOP_TotalExceededVirus = Column(INTEGER)
    VOP_TotalExceededDestinations = Column(INTEGER)
    VOP_PreventSpamNMin = Column(INTEGER)
    VOP_LastAccumulationTime = Column(DATETIME)
