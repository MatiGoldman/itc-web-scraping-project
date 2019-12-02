import mysql.connector
import json

CFG_PATH = 'persistor/config.json'


class MysqlConnection:
    __instance = None

    def __init__(self):
        with open(CFG_PATH) as cfg:
            config = json.load(cfg)

        self.db_conn = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            passwd=config['password'],
            database=config['database']
        )

        self.db_cursor = self.db_conn.cursor()

    def __new__(cls):
        if MysqlConnection.__instance is None:
            MysqlConnection.__instance = object.__new__(cls)
        return MysqlConnection.__instance

    def __del__(self):
        self.db_conn.close()

    def commit(self):
        self.db_conn.commit()
