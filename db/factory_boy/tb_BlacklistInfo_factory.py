import factory
from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import TbBlacklistInfo


class TbBlacklistInfoFactory(CMFactory):
    class Meta:
        model = TbBlacklistInfo
        sqlalchemy_session_persistence = 'commit'

    SLF_Key = '0x36e77307362d14b49b9d61f24b221082'
    SLF_Action = 1
    SLF_Type = 2
    SLF_Data = '1.1.1.1'
    SLF_RiskLevel = 3
    SourceType = 1
    ScanAction = 1
    Status = 1
    UserDefinedTime = ExtendDateTime.current_time()

    class Params:
        expire_date = '+5'
        expire_utc_date = '+13'

    @factory.lazy_attribute_sequence
    def EntityID(self, n):
        return '11111111-AAAA-BBBB-CCCC-DDDDDDDD{:A>4}'.format(n)

    @factory.lazy_attribute
    def SLF_ExpireDateTimeStamp(self):
        return ExtendDateTime.get_time_stamp_by_offset(self.expire_date)

    @factory.lazy_attribute
    def SLF_ExpiredUTCDate(self):
        return ExtendDateTime.get_date_by_offset(self.expire_utc_date)
