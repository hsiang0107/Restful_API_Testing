from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, VARCHAR


class TbRelayNotificationTaskData(Base):
    __tablename__ = 'tb_RelayNotificationTaskData'
    NotificationDataKey = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    DataToken = Column(VARCHAR(32), nullable=False)
    DataValue = Column(VARCHAR(256))
