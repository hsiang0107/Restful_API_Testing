from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, VARCHAR


class TbEventCenterSetting(Base):
    __tablename__ = 'tb_EventCenterSetting'
    Event_ID = Column(VARCHAR(64), primary_key=True, nullable=False)
    SettingField = Column(VARCHAR(64), primary_key=True, nullable=False)
    SettingValue = Column(VARCHAR(256))
    DisableDelete = Column(BIT, nullable=False)
