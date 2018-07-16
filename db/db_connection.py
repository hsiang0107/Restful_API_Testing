# create db session and orm objects for tmcm
import sqlalchemy
from sqlalchemy import orm
from lib.ConfigHelper import ConfigHelper


class DBConnection:
    # def __init__(self):
    #     self.connect(connection_str)

    def connect(self, connection_str):
        try:
            self.engine = sqlalchemy.create_engine(connection_str)
            self.session = orm.create_session(bind=self.engine, autocommit=False, autoflush=True)
            # Due to service will insert some config when service init,
            # so it can't use session maker which will lock table and make restart crash.
            # We need delete data by manual or write method
            # self.session = orm.scoped_session(orm.sessionmaker())
            # self.session.configure(bind=self.engine)
        except Exception as e:
            raise e
            
    def tearDown(self):
        # self.session.rollback()
        self.session.close()


class CMConnection(DBConnection):
    def __init__(self):
        config = ConfigHelper()
        account = config.get_data_from_config('DB', 'account')
        password = config.get_data_from_config('DB', 'password')
        db_server = config.get_data_from_config('DB', 'address')
        db_name = config.get_data_from_config('DB', 'dbname')
        db_instance = config.get_data_from_config('DB', 'instance')
        db_port = config.get_data_from_config('DB', 'port')
        if db_instance:
            connection_str = "mssql+pyodbc://{0}:{1}@{2}\{3}/{4}?driver=SQL+Server".format(account, password,
                                                                                           db_server, db_instance,
                                                                                           db_name)
        else:
            connection_str = "mssql+pyodbc://{0}:{1}@{2}:{3}/{4}?driver=SQL+Server".format(account, password,
                                                                                           db_server, db_port, db_name)
        self.connect(connection_str)
