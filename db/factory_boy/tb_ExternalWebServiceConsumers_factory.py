from db.factory_boy.cm_factory import CMFactory
from db import TbExternalWebServiceConsumers


class TbExternalWebServiceConsumersFactory(CMFactory):
    class Meta:
        model = TbExternalWebServiceConsumers
        sqlalchemy_session_persistence = 'commit'

    ApplicationID = '8BC58D63-D045-4F05-9619-0AEFA5F32274'
    APIKey = '!CRYPT!5279A29799F84C337D9390E7078817954E9AF2A9E6775E923405984A1C4D5591B94E480ACCAF235FC901D4B5D1F'
    IsEnabled = 1
    AllowedLatencyInSeconds = 120
    ApplicationName = 'ext_app1'
