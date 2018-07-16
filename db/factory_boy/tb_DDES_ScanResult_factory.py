import factory
from datetime import datetime
from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import TbEntityInfo, TbDDESScanResult, TbDDESTask


class TbDDESScanResultFactory(CMFactory):
    class Meta:
        model = TbDDESScanResult
        sqlalchemy_session_persistence = 'commit'

    IOC_GUID = None
    FileFullPathName = None
    LastUpdateTime = datetime.now()

    class Params:
        client = 'Client11'
        match_so = None
        create_date = '-1'
        observe_date = '-1'
        task = None

    @factory.lazy_attribute
    def TaskGUID(self):
        if isinstance(self.task, TbDDESTask):
            return self.task.TaskGUID
        else:
            return '1732AD3B-B41F-41B4-A640-DF632F479A2A'

    @factory.lazy_attribute
    def MachineGUID(self):
        entity = TbEntityInfo.find_by_machine_name(self.client)
        return entity.EI_MachineID

    @factory.lazy_attribute
    def ClientGUID(self):
        entity = TbEntityInfo.find_by_machine_name(self.client)
        return entity.EI_EntityID

    @factory.lazy_attribute
    def ServerGUID(self):
        entity = TbEntityInfo.find_by_machine_name(self.client)
        return entity.EI_AgentID

    @factory.lazy_attribute
    def SLF_Key(self):
        return self.match_so.SLF_Key

    @factory.lazy_attribute
    def MatchObj_Type(self):
        type = {0: 'ip', 2: 'file', 3: 'dns_query'}
        return type[int(self.match_so.SLF_Type)]

    @factory.lazy_attribute
    def MatchObj_Data(self):
        return self.match_so.SLF_Data

    @factory.lazy_attribute
    def FileFullPathName(self):
        if int(self.match_so.SLF_Type) == 2:
            return 'Fake File'
        else:
            None

    @factory.lazy_attribute
    def FileCreationUTCTime(self):
        return ExtendDateTime.get_date_by_offset(self.create_date)

    @factory.lazy_attribute
    def FirstObsUTCTime(self):
        return ExtendDateTime.get_date_by_offset(self.observe_date)
