import factory
from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import *


class TbRCATaskFactory(CMFactory):
    class Meta:
        model = TbRCATask
        sqlalchemy_session_persistence = 'commit'

    TaskID = None
    ScanSummaryID = None
    Criteria = 'factory.com'
    CriteriaType = 1
    AgentID = '112E85840114-694DBF9D-44CC-65D3-0003'
    ServerID = None
    SLF_Key = '123'
    Status = 0
    IsAffected = 0
    IsSync = 0
    CreationTime = ExtendDateTime.current_time()
    LastUpdateTime = ExtendDateTime.current_time()
    IsTimeout = 0

    class Params:
        init = True
        agent = 'Client11'
        day_offset = '+0'

    @factory.lazy_attribute
    def AgentID(self):
        return TbEntityInfo.find_by_machine_name(self.agent).EI_EntityID

    @factory.lazy_attribute
    def ServerID(self):
        if self.init:
            return None
        else:
            return TbEntityInfo.find_by_machine_name(self.agent).EI_AgentID

    @factory.lazy_attribute_sequence
    def TaskID(self, n):
        if self.init:
            return None
        else:
            return "a4918672-92da-4065-rcac-1ebf6c5a{:A>4}".format(n)

    @factory.lazy_attribute_sequence
    def ScanSummaryID(self, n):
        if self.init:
            return None
        else:
            return "b4918672-92da-4065-scan-1ebf6c5a{:A>4}".format(n)

    @factory.lazy_attribute
    def CreationTime(self):
        return ExtendDateTime.get_date_by_offset(self.day_offset)
