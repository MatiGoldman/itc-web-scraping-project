from persistor.MysqlConnection import MysqlConnection


class Persistor:

    def __init__(self):
        self.conn = MysqlConnection()

    def commit(self):
        self.conn.db_conn.commit()
