from db_helper.MysqlConnection import MysqlConnection
from abc import ABC, abstractmethod


class EntityHelper(ABC):
    """ Base class to implement in Entity helpers"""

    def __init__(self):
        self.conn = MysqlConnection()

    def commit(self):
        self.conn.db_conn.commit()

    @abstractmethod
    def insert(self):
        pass
