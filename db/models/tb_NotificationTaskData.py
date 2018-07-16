from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import NVARCHAR, UNIQUEIDENTIFIER, VARCHAR


class TbNotificationTaskData(Base):
    __tablename__ = 'tb_NotificationTaskData'
    NotificationDataKey = Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False)
    DataToken = Column(VARCHAR(32), nullable=False)
    DataValue = Column(NVARCHAR(2048))
