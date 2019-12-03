import mysql.connector
import json

CFG_PATH = 'db_helper/config.json'


class MysqlConnection:
    """Create necessary methods to perform operations over the database"""
    __instance = None

    def __init__(self):
        """Loads the initial configuration from the config.json file"""
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
        """Singleton to instantiate the connection object
        :return: db connection
        """
        if MysqlConnection.__instance is None:
            MysqlConnection.__instance = object.__new__(cls)
        return MysqlConnection.__instance