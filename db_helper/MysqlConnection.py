import mysql.connector
import json

CFG_PATH = 'config.json'


class MysqlConnection:
    """Create necessary methods to perform operations over the database"""
    __instance = None

    def __init__(self):
        """Loads the initial configuration from the config.json file"""
        with open(CFG_PATH) as cfg:
            config = json.load(cfg)

        self.db_conn = mysql.connector.connect(
            host=config['db']['host'],
            user=config['db']['user'],
            passwd=config['db']['password'],
            database=config['db']['database'],
            use_pure=True
        )

        self.db_cursor = self.db_conn.cursor()

    def __new__(cls):
        """Singleton to instantiate the connection object
        :return: db connection
        """
        if MysqlConnection.__instance is None:
            MysqlConnection.__instance = object.__new__(cls)
        return MysqlConnection.__instance