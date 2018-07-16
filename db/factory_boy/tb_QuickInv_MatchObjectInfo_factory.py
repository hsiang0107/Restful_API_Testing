import factory
from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import *


class TbQuickInvMatchObjectInfoFactory(CMFactory):
    class Meta:
        model = TbQuickInvMatchObjectInfo
        sqlalchemy_session_persistence = 'commit'

    AgentID = '112E85840114-694DBF9D-44CC-65D3-0003'
    SLF_Key = '0x4fa3ac39560cb7f8a1e794840'
    RetroScanCategory = 5
    MetaValue = 8
    MetaCategory = 11
    FirstSeenUTCTime = ExtendDateTime.get_date_by_offset('-3')
    RCAScanID = None
    FileFullPath = None
    FileCreationUTCTime = None
    LastUpdateTime = ExtendDateTime.current_time()

    class Params:
        rca_init = True
        agent = 'Client11'

    @factory.lazy_attribute
    def AgentID(self):
        return TbEntityInfo.find_by_machine_name(self.agent).EI_EntityID

    @factory.lazy_attribute_sequence
    def RetroScanData_MD5(self, n):
        md5 = '7788no9{:A>4}'.format(n)
        return bytes(md5, 'utf-8')

    @factory.lazy_attribute_sequence
    def RCAScanID(self, n):
        if self.rca_init:
            return None
        else:
            return "a4918672-92da-4065-9dec-1ebf6c5a{:A>4}".format(n)
