import factory
from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import *


class TbQuickInvTaskFactory(CMFactory):
    class Meta:
        model = TbQuickInvTask
        sqlalchemy_session_persistence = 'commit'

    TaskID = None
    HasMore = 1
    LastContentID = ''
    Criteria = 'a.b.c'
    CriteriaType = 1
    RetroScanData_MD5 = None
    RetroScanCategory = 5
    SLF_Key = '123'
    IsManual = 1
    CreationTime = ExtendDateTime.current_time()
    LastUpdateTime = ExtendDateTime.current_time()
    IsTimeout = 0

    class Params:
        init = True
        day_offset = '+0'

    @factory.lazy_attribute_sequence
    def TaskID(self, n):
        if self.init:
            return None
        else:
            return "a4918672-92da-4065-9dec-1ebf6c5a{:A>4}".format(n)

    @factory.lazy_attribute
    def CreationTime(self):
        return ExtendDateTime.get_date_by_offset(self.day_offset)

    @factory.lazy_attribute_sequence
    def RetroScanData_MD5(self, n):
        md5 = '7788no9{:A>4}'.format(n)
        return bytes(md5, 'utf-8')
