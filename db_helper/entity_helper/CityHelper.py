from db_helper.entity_helper.EntityHelper import EntityHelper


class CityHelper(EntityHelper):
    """
    Allows to persist the cities using the Persistor class
    """

    def __init__(self):
        """Inheritance of the Persistor class"""
        super().__init__()

    def insert(self, city):
        """Inserts the city into the database
        :param city: city to persist
        """
        city_db = self.select(f"SELECT id FROM city WHERE id = {city.id}")

        if not city_db:
            self.persist("INSERT INTO city (id, name) VALUES (%s, %s)", (city.id, city.name))

        self.commit()
