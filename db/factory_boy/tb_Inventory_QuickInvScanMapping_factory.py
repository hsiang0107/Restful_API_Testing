import factory
from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import *


class TbInventoryQuickInvScanMappingFactory(CMFactory):
    class Meta:
        model = TbInventoryQuickInvScanMapping
        sqlalchemy_session_persistence = 'commit'

    EventContent_MD5 = bytes('123456', 'utf-8')
    RetroScanData_MD5 = bytes('234567', 'utf-8')
    RetroScanCategory = 2
    LastUpdateTime = ExtendDateTime.current_time()

    @factory.lazy_attribute_sequence
    def EventContent_MD5(self, n):
        md5 = '5566nodie{:A>4}'.format(n)
        return bytes(md5, 'utf-8')

    @factory.lazy_attribute_sequence
    def RetroScanData_MD5(self, n):
        md5 = '183nodie{:A>4}'.format(n)
        return bytes(md5, 'utf-8')
