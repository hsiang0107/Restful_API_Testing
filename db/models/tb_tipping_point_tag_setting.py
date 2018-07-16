from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, SMALLINT, VARCHAR


class Tbtippingpointtagsetting(Base):
    __tablename__ = 'tb_tipping_point_tag_setting'
    id = Column(BIGINT, primary_key=True, nullable=False)
    IsEnable = Column(SMALLINT, nullable=False)
    AppendColumn = Column(VARCHAR(256), nullable=False)
    TagName = Column(VARCHAR(512), nullable=False)
