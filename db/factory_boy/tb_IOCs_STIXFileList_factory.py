from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import TbIOCsSTIXFileList


class TbIOCsSTIXFileListFactory(CMFactory):
    class Meta:
        model = TbIOCsSTIXFileList
        sqlalchemy_session_persistence = 'commit'

    FileHashID = '017D896BE4991423EB6653077B93ADA1DCC7FFB2'
    FileName = 'STIX_Domain_Watchlist.xml'
    FileContent_BASE64 = '123='
    Title = 'Title line 1 test app 1'
    UploadedTime = ExtendDateTime.current_time()
    UploadedFrom = 1
    UploadedBy = 'test app 1'
    ExtractingStatus = 1
