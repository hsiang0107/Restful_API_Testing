from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, TINYINT, VARCHAR


class TbInventorySecurityToUserActionStatusEndpoint(Base):
    __tablename__ = 'tb_Inventory_Security_To_User_ActionStatus_Endpoint'
    SeqID = Column(BIGINT, primary_key=True, nullable=False)
    Status = Column(TINYINT, nullable=False)
    actionID = Column(VARCHAR(36))
