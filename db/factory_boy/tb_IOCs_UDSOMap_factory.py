from db.factory_boy.cm_factory import CMFactory
from db import TbIOCsUDSOMap


class TbIOCsUDSOMapFactory(CMFactory):
    class Meta:
        model = TbIOCsUDSOMap
        sqlalchemy_session_persistence = 'commit'

    FileHashID = '31DD9A3F6863946E36E7A6762609CFE22C7154FC'
    UDSOID = '0x36e77307362d14b49b9d61f24b221082'
    FileType = 1
