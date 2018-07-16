from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, INTEGER, NVARCHAR, SMALLINT, VARCHAR


class Tbtippingpointsetting(Base):
    __tablename__ = 'tb_tipping_point_setting'
    id = Column(BIGINT, primary_key=True, nullable=False)
    ServerName = Column(VARCHAR(256))
    ServerAddress = Column(VARCHAR(512), nullable=False)
    Username = Column(NVARCHAR(64), nullable=False)
    Password = Column(NVARCHAR(256), nullable=False)
    IsEnable = Column(SMALLINT, nullable=False)
    RiskRating = Column(SMALLINT, nullable=False)
    Watermark = Column(BIGINT, nullable=False)
    Batchsize = Column(INTEGER, nullable=False)
    LastUpdateTime = Column(DATETIME)
    IsSuccess = Column(SMALLINT)
