from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import CHAR, INTEGER


class TbInventorySecurityToUserPreSumMachine(Base):
    __tablename__ = 'tb_Inventory_Security_To_User_PreSum_Machine'
    id = Column(INTEGER, primary_key=True, nullable=False)
    MachineGuid = Column(CHAR(36))
    Count_Today = Column(INTEGER)
    Count_7days = Column(INTEGER)
    Count_14days = Column(INTEGER)
    Count_30days = Column(INTEGER)
    Count_90days = Column(INTEGER)
