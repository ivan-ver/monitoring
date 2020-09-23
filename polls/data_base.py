import configparser
import os
import pymysql



# noinspection SqlNoDataSourceInspection,SqlResolve
class Database:
    _connection = None
    _cursor = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def _get_conn(self):
        config = configparser.ConfigParser()
        t = os.getcwd() + '\\config\\services.cfg'
        config.read(os.getcwd() + '\\config\\services.cfg')
        if 'db_conn' not in config:
            print('db config error')  # TODO correct handling
            exit(1)
        props = dict(config.items('db_conn'))
        return pymysql.connect(cursorclass=pymysql.cursors.DictCursor, **props)

    def connect(self):
        if self._connection is None:
            self._connection = self._get_conn()
            self._cursor = self._connection.cursor()
            print('connected')

    def disconnect(self):
        if self._connection is not None:
            self._connection.commit()
            self._connection.close()
            print('disconnected')

    def get_services_info(self, table_name):
        req = """SELECT *FROM services.{}""".format(table_name)
        self._cursor.execute(req)
        return self._cursor.fetchall()
