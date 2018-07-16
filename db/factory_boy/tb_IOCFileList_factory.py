from lib.extend_datetime import ExtendDateTime
from db.factory_boy.cm_factory import CMFactory
from db import TbIOCFileList


class TbIOCFileListFactory(CMFactory):
    class Meta:
        model = TbIOCFileList
        sqlalchemy_session_persistence = 'commit'

    IOC_GUID = '111111111111-AAAAAAAA-1111-0000-0001'
    FileHashID = '31DD9A3F6863946E36E7A6762609CFE22C7154FC'
    FileName = 'Test IOC file 1'
    Author = 'Tester'
    AuthoredUTCTime = ExtendDateTime.current_time()
    ShortDesc = 'Short description sample'
    Description = 'Description sample'
    FileContent_BASE64 = '123='
    UploadedTime = ExtendDateTime.current_time()
    UploadedFrom = 1
    UploadedBy = 'app name 1'
    ExtractingStatus = 1
