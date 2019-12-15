from db_helper.MysqlConnection import MysqlConnection
from abc import ABC, abstractmethod
import logging


class EntityHelper(ABC):
    """ Base class to implement in Entity helpers"""

    def __init__(self):
        self.conn = MysqlConnection()

    def commit(self):
        self.conn.db_conn.commit()

    def persist(self, query, params):
        try:
            logging.debug(query % params)

            self.conn.db_cursor.execute(query, params)
            self.commit()
        except Exception as ex:
            print(f'Failed to persist {params}')
            logging.error('Error at %s', 'query', exc_info=ex)

    def select(self, query):
        try:
            logging.debug(query)

            self.conn.db_cursor.execute(query)
            return self.conn.db_cursor.fetchall()
        except Exception as ex:
            logging.error('Error at %s', 'query', exc_info=ex)

    @abstractmethod
    def insert(self):
        pass
