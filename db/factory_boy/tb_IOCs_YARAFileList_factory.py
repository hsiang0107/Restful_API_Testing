from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import TbIOCsYARAFileList


class TbIOCsYARAFileListFactory(CMFactory):
    class Meta:
        model = TbIOCsYARAFileList
        sqlalchemy_session_persistence = 'commit'

    FileHashID = '71EAB2143940EF63899DBD8C99994FD374174EAB'
    FileName = 'APT_Gholee.yara'
    FileContent_BASE64 = '123='
    UploadedTime = ExtendDateTime.current_time()
    UploadedFrom = 1
    UploadedBy = 'test app 1'
