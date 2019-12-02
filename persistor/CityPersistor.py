from persistor.Persistor import Persistor


class CityPersistor(Persistor):
    def __init__(self):
        super().__init__()

    def insert(self, city):
        db_cursor = self.conn.db_cursor

        db_cursor.execute(f"SELECT id FROM city WHERE id = {city.id}")
        city_db = db_cursor.fetchall()

        if not city_db:
            db_cursor.execute("INSERT INTO city (id, name) VALUES (%s, %s)", (city.id, city.name))
