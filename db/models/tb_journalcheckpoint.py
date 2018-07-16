from sqlalchemy import Column
from db.cm_session import cm_session, Base
from sqlalchemy.dialects.mssql import BIGINT, DATETIME, INTEGER, VARCHAR


class Tbjournalcheckpoint(Base):
    __tablename__ = 'tb_journalcheckpoint'
    name = Column(VARCHAR(128), primary_key=True, nullable=False)
    watermark = Column(INTEGER, nullable=False)
    batchsize = Column(INTEGER)
    lutontmcm = Column(DATETIME, nullable=False)
    bigwatermark = Column(BIGINT)

    @classmethod
    def reset_all_watermark(cls, value=0):
        cm_session.query(cls).update({cls.watermark: value})
        cm_session.commit()

    @classmethod
    def reset_all_bigwatermark(cls, value=0):
        cm_session.query(cls).update({cls.bigwatermark: value})
        cm_session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cm_session.query(cls).filter(cls.name == name).first()
