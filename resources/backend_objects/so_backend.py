import os
import time
from lib import DBHelper
from lib.LogSender.LogSender import LogSender
from db.models.tb_BlacklistInfo import TbBlacklistInfo
from db.models.tb_journalcheckpoint import Tbjournalcheckpoint
from db.models.tb_BlacklistExtraInfo import TbBlacklistExtraInfo
from db.models.tb_BlacklistRestJournal import TbBlacklistRestJournal
from robot.utils.asserts import assert_equal, assert_not_none


def so_backend_suite_setup():
    """
    Step1. turn off some schedule job setting
    Step2. restart CM service
    Step3. register using Init csv
    Step4. wait for 5 seconds and send status log
    Step5. run sp_SyncEntityIPAddress
    """

    test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  '../../tests/testdata/SOBackend/Initialize/')
    LogSender().register_with_csv_file('Init', test_data_path)
    LogSender().send_log(test_data_path + 'status.csv')
    time.sleep(5)
    DBHelper.execute_store_procedure('sp_SyncEntityIPAddress')


def big_watermark_should_be_correct(**kwargs):
    for name, value in kwargs.items():
        record = Tbjournalcheckpoint.find_by_name(name)
        assert record.bigwatermark == int(value), "%s.bigwatermark should be %s, but is %s instead" %\
                                                  (name, value, record.bigwatermark)


def check_blacklist_table_from_logBlacklistInfoJournal(log, **kwargs):
    blacklistinfo = TbBlacklistInfo.find_by_slf_data(log.SLF_Data)
    assert_not_none(blacklistinfo, "cant find tb_blacklistinfo with slf_data=%s" % log.SLF_Data)
    assert_equal(log.EntityID, blacklistinfo.EntityID)
    assert_equal(str(log.SLF_Type), str(blacklistinfo.SLF_Type))
    assert_equal(str(log.SLF_RiskLevel), str(blacklistinfo.SLF_RiskLevel))
    assert_equal(str(log.SourceType), str(blacklistinfo.SourceType))
    assert_equal(str(log.SLF_ExpireDateTimeStamp), str(blacklistinfo.SLF_ExpireDateTimeStamp))
    assert_equal(str(log.SLF_URLCorrelationKey), str(blacklistinfo.SLF_URLCorrelationKey))
    assert_equal(log.FilterCRC, blacklistinfo.FilterCRC)

    for column, value in kwargs.items():
        if column == 'HasAssessed':
            value = 'True' if value == 1 else 'False'
        assert_equal(str(getattr(blacklistinfo, column)), str(value),
                     "(Data %s)TbBlacklistInfo.%s should be %s, but is %s" % (blacklistinfo.SLF_Data, column, value,
                                                                              getattr(blacklistinfo, column)))
    check_blacklistextrainfo_from_logBlacklistInfoJournal(log, blacklistinfo)
    check_blacklistInfoRESTJournal_from_blacklistinfo(blacklistinfo)

def check_blacklistextrainfo_from_logBlacklistInfoJournal(log, blacklistinfo):
    extra_info = TbBlacklistExtraInfo.find_last_record_by_slf_key(blacklistinfo.SLF_Key)
    assert_equal(log.SubmitTime, str(extra_info.SubmitTime))
    assert_equal(log.AnalyzeTime, str(extra_info.AnalyzeTime))
    assert_equal(log.SubmitterProductName, extra_info.SubmitterProductName)
    assert_equal(log.SubmitterHostName, extra_info.SubmitterHostName)
    assert_equal(log.SubmitterIPAddress, extra_info.SubmitterIPAddress)
    assert_equal(log.FileName, extra_info.FileName)
    assert_equal(log.TrueFileType, extra_info.TrueFileType)
    assert_equal(log.DetectionName, extra_info.DetectionName)
    assert_equal(str(log.ThreatCharacteristics), str(extra_info.ThreatCharacteristics))
    assert_equal(log.SampleIdentity, extra_info.SampleIdentity)
    assert_equal(log.AnalyzeReportID, extra_info.AnalyzeReportID)
    assert_equal(log.Protocol, extra_info.Protocol)
    assert_equal(log.Source, extra_info.Source)
    assert_equal(log.Destination, extra_info.Destination)

def check_blacklistInfoRESTJournal_from_blacklistinfo(blacklistinfo):
    rest_journal = TbBlacklistRestJournal.find_last_record_by_slf_key(blacklistinfo.SLF_Key)
    assert_equal(blacklistinfo.SLF_Type, rest_journal.SLF_Type)
    assert_equal(blacklistinfo.SLF_Data, rest_journal.SLF_Data)
    assert_equal(blacklistinfo.SLF_RiskLevel, rest_journal.SLF_RiskLevel)
    assert_equal(blacklistinfo.SLF_ExpireDateTimeStamp, rest_journal.SLF_ExpireDateTimeStamp)
    assert_equal(blacklistinfo.ViolatedDTASPolicy, rest_journal.ViolatedDTASPolicy)
    assert_equal(blacklistinfo.SourceFileSHA1, rest_journal.SourceFileSHA1)
    assert_equal(blacklistinfo.Detectable, rest_journal.Detectable)
    assert_equal(blacklistinfo.SourceType, rest_journal.SourceType)
    assert_equal(blacklistinfo.ScanAction, rest_journal.ScanAction)
    assert_equal(blacklistinfo.FilterCRC, rest_journal.FilterCRC)
    assert_equal(blacklistinfo.RootFileSHA1, rest_journal.RootFileSHA1)
    assert_equal(blacklistinfo.DataMD5, rest_journal.DataMD5)
    assert_equal(blacklistinfo.Status, rest_journal.Status)
