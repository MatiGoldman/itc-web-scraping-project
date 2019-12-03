from persistor.Persistor import Persistor


class CityPersistor(Persistor):
    """
    Allows to persist the cities using the Persistor class
    """
    def __init__(self):
        """Inheritance of the Persistor class"""
        super().__init__()

    def insert(self, city):
        """Inserts the city into the database"""
        db_cursor = self.conn.db_cursor

        db_cursor.execute(f"SELECT id FROM city WHERE id = {city.id}")
        city_db = db_cursor.fetchall()

        if not city_db:
            db_cursor.execute("INSERT INTO city (id, name) VALUES (%s, %s)", (city.id, city.name))
