import factory
from datetime import datetime
from db.factory_boy.cm_factory import CMFactory
from db import TbDDESTask, TbAccount


class TbDDESTaskFactory(CMFactory):
    class Meta:
        model = TbDDESTask
        sqlalchemy_session_persistence = 'commit'

    Status = None
    AtRiskCnt = 0
    SafeCnt = 0
    PendingCnt = 0
    TotalCnt = 0
    RetrieveID = -1
    IOC_GUID = None
    Parameters_JSON = '{"fake" : "json"}'
    InvestigateTime = datetime.now()
    LastUpdateTime = datetime.now()
    TriggerSource = None

    class Params:
        user = 'admin'

    @factory.lazy_attribute_sequence
    def TaskGUID(self, n):
        return '1732AD3B-B41F-41B4-A640-DF632F47{:A>4}'.format(n)

    @factory.lazy_attribute
    def CreatorGUID(self):
        return TbAccount.find_by_id(self.user).Guid
