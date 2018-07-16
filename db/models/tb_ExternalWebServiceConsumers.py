from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, INTEGER, NVARCHAR


class TbExternalWebServiceConsumers(Base):
    __tablename__ = 'tb_ExternalWebServiceConsumers'
    ApplicationID = Column(NVARCHAR(50), primary_key=True, nullable=False)
    APIKey = Column(NVARCHAR(200), nullable=False)
    IsEnabled = Column(BIT, nullable=False)
    AllowedLatencyInSeconds = Column(INTEGER, nullable=False)
    ApplicationName = Column(NVARCHAR(200), nullable=False)

    @classmethod
    def check_if_key_is_duplicated(cls, application_id):
        return cm_session.query(cls).filter(cls.ApplicationID == application_id).count() > 0

    @classmethod
    def find_by_app_name(cls, app_name):
        return cm_session.query(cls).filter(cls.ApplicationName == app_name).first()