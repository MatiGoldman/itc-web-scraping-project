import mysql.connector
import json

CFG_PATH = 'persistor/config.json'


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
        """Creates a new connection to the database
        :return: db connection
        """
        if MysqlConnection.__instance is None:
            MysqlConnection.__instance = object.__new__(cls)
        return MysqlConnection.__instance

    def __del__(self):
        """Closes the connection to the databsae"""
        self.db_conn.close()

    def commit(self):
        """Commit the changes to the database"""
        self.db_conn.commit()
