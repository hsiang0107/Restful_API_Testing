from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIT, CHAR, DATETIME, INTEGER, NVARCHAR, VARCHAR


class TbCustomViews(Base):
    __tablename__ = 'tb_CustomViews'
    CV_ID = Column(CHAR(36), primary_key=True, nullable=False)
    CV_UserGuid = Column(CHAR(36), nullable=False)
    CV_BasedViewID = Column(VARCHAR(64), nullable=False)
    CV_Name = Column(NVARCHAR(64), nullable=False)
    CV_Description = Column(NVARCHAR(1024))
    CV_Enable = Column(BIT, nullable=False)
    CV_ViewType = Column(INTEGER)
    CV_TMCMOnly = Column(BIT)
    CV_ReferenceKey = Column(VARCHAR(261))
    CV_FunctionType = Column(INTEGER)
    CV_TargetType = Column(INTEGER)
    CV_ProductScopeType = Column(INTEGER)
    CV_CreatedUTCTime = Column(DATETIME)
    CV_LastUpdateUTCTime = Column(DATETIME)
    CV_CustomizedColumns = Column(VARCHAR)
    CV_SortBy = Column(VARCHAR)
