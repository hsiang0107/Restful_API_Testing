import factory
from db.factory_boy.cm_factory import CMFactory
from db import TbLogFile, TbSystemInfo


class TbLogFileFactory(CMFactory):
    class Meta:
        model = TbLogFile
        sqlalchemy_session_persistence = 'commit'

    CMGuid = TbSystemInfo.get_CM_guid()
    FileExt = "exe"
    FileName = "Fake.txt"
    FileNameInArchive = "fake.zip"
    FileSize = "5566"
    HasQFile = 1
    QFilePath = "fake.zip"
    SharedFolder = "FakeFolder"
    TrueFileType = "troj"
    TrueFileTypeDescription = "WIN32EXEC"
    SHA1inArc = "Fake"
    FileTypeInArc = "exe"

    class Params:
        log_general = None

    @factory.lazy_attribute_sequence
    def id(self, n):
        return n

    @factory.lazy_attribute
    def MsgLogID(self):
        return self.log_general.MsgLogID

    @factory.lazy_attribute_sequence
    def SHA1(self, n):
        return "DCB63A930713A07525AE07A149F1A2DF911{:A>5}".format(n)

    @factory.lazy_attribute_sequence
    def MD5(self, n):
        return "9e107d9d372bb6826bd81d3542a{:A>5}".format(n)
