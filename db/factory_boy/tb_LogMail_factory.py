import factory
from db.factory_boy.cm_factory import CMFactory
from db import TbLogMail, TbSystemInfo


class TbLogMailFactory(CMFactory):
    class Meta:
        model = TbLogMail
        sqlalchemy_session_persistence = 'commit'

    CMGuid = TbSystemInfo.get_CM_guid()
    Recipient = "Fake Recipient"
    Sender = "Fake Sender"
    Subject = "Fake Subject"
    AttachmentFileName = "Fake attached file"
    AttachmentFileSize = "5566"
    AttachmentFileType = "exe"
    AttachmentSHA1 = "aabbcc"

    class Params:
        log_general = None

    @factory.lazy_attribute_sequence
    def id(self, n):
        return n

    @factory.lazy_attribute
    def MsgLogID(self):
        return self.log_general.MsgLogID
