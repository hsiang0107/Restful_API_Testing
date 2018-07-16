from db.factory_boy.cm_factory import CMFactory
from db import TbBlacklistSourceInfo


class TbBlacklistSourceInfoFactory(CMFactory):
    class Meta:
        model = TbBlacklistSourceInfo
        sqlalchemy_session_persistence = 'commit'

    SLF_Key = '0x36e77307362d14b49b9d61f24b221082'
    FileHashID = '31DD9A3F6863946E36E7A6762609CFE22C7154FC'
    Source = 4
    UploadedBy = 'aaa'
    FileName = 'aaa.txt'
