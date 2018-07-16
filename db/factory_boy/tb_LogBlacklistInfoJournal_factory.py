import factory
from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import TbLogBlacklistInfoJournal, TbServerList


class TbLogBlacklistInfoJournalFactory(CMFactory):
    class Meta:
        model = TbLogBlacklistInfoJournal
        sqlalchemy_session_persistence = 'commit'

    SLF_Action = 1
    SLF_Type = 0
    SLF_Data = '100.1.1.1'
    SLF_RiskLevel = 3
    ViolatedDTASPolicy = 'Executable code in document headers;Malicious site accessed'
    SourceFileSHA1 = '4E35830C1466C5CEE98B8E8C29778E7F033DBF86'
    Detectable = 1
    FileName = 'Factory_Attack.troj'
    TrueFileType = 'MIME'
    SubmitterProductName = 'TMES'
    SubmitterHostName = 'tw-Factory'
    SubmitterIPAddress = '10.1.2.3'
    DetectionName = 'SuspiciousIP.umxx'
    ThreatCharacteristics = 2
    SampleIdentity = '111.exe'
    AnalyzeReportID = 'E9630429-9039-4DF3-9DA4-C27FAEE507E1'
    Protocol = None
    Source = '100.1.2.3'
    Destination = '100.2.3.4'
    RootFileSHA1 = 'BF6C100866F54BDDC710D128E5640935EF9882F9'
    DataMD5 = 'BF6C100866F54BDDC710D128E5640935EF9882F9'
    ScanAction = None
    SourceType = 0
    SoStatus = None

    class Params:
        server_name = 'DDI01'
        expire_date = '+5'
        submit = '-1'
        analyze = '-1'

    @factory.lazy_attribute
    def EntityID(self):
        return TbServerList.find_by_displayname(self.server_name).ServerID

    @factory.lazy_attribute_sequence
    def SLF_URLCorrelationKey(self, n):
        if int(self.SLF_Type) == 1:
            return '96aeff92ffd18acbbf0a1f0c43e9{:0>4}'.format(str(n))
        else:
            return None

    @factory.lazy_attribute_sequence
    def FilterCRC(self, n):
        if int(self.SLF_Type) == 2:
            return '0x8C27{:0>4}'.format(str(n))
        else:
            return None

    @factory.lazy_attribute
    def SLF_ExpireDateTimeStamp(self):
        return ExtendDateTime.get_time_stamp_by_offset(self.expire_date)

    @factory.lazy_attribute
    def SubmitTime(self):
        return ExtendDateTime.get_date_by_offset(self.submit)

    @factory.lazy_attribute
    def AnalyzeTime(self):
        return ExtendDateTime.get_date_by_offset(self.analyze)
