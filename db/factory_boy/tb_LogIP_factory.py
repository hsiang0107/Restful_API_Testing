import factory
from db.factory_boy.cm_factory import CMFactory
from db import TbLogIP, TbSystemInfo


class TbLogIPFactory(CMFactory):
    class Meta:
        model = TbLogIP
        sqlalchemy_session_persistence = 'commit'

    CMGuid = TbSystemInfo.get_CM_guid()
    BOTCmd = 'exec'
    BOTUrl = "www.abc.com"
    ChannelName = "fake channel"
    ConfidenceLevel = "1"
    DestIP = "10.1.1.5"
    DestMAC = "00-00-00-00"
    DestPort = "81"
    DomainName = "trend"
    HostName = None
    Nickname = "Fake Nickname"
    SourceIP = None
    SourceMAC = "00-00-00-00"
    SourcePort = "80"
    URL = "www.fakeurl.com"
    UserAgent = "Fake Agent"
    UserName = "Fake Username"
    SrcGroupName = "Fake Group"
    SrcZone = 1
    DstGroupName = "Fake Group"
    DstZone = 2
    Score = None
    SrcUserName = "Fake Src Username"
    DestUserName = "Fake dest username"
    SrcHostname = "fake src hostname"
    DestHostname = "fake dest hostname"
    ProtocolHostname = "fake protocol"
    CategoryIDList = "fake id list"
    SrcUserName2 = "fake src username2"
    SrcUserName3 = "fake src username3"
    SrcUserLoginTime1 = "2014-05-06 22:15:56"
    SrcUserLoginTime2 = "2014-05-06 22:15:56"
    SrcUserLoginTime3 = "2014-05-06 22:15:56"
    DestUsername2 = "fake dest username2"
    DestUsername3 = "fake dest username2"
    DestUserLoginTime1 = "2014-05-06 22:15:56"
    DestUserLoginTime2 = "2014-05-06 22:15:56"
    DestUserLoginTime3 = "2014-05-06 22:15:56"
    SrcOS = "Fake src OS"
    DestOS = "Fake dest os"
    Is_CCCA_Detection = 1
    HTTPReferer = None
    CE_FilterID = 'F'

    class Params:
        log_general = None
        blacklist = None

    @factory.lazy_attribute_sequence
    def id(self, n):
        return n

    @factory.lazy_attribute
    def MsgLogID(self):
        return self.log_general.MsgLogID

    @factory.lazy_attribute_sequence
    def SLF_URLCorrelationKey(self, n):
        if self.blacklist is not None:
            return self.blacklist.SLF_URLCorrelationKey
        else:
            return '96aeff92ffd18acbbf0a1f0c43e9{:0>4}'.format(str(n))
