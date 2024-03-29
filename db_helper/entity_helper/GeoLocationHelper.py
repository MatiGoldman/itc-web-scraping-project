from db_helper.entity_helper.EntityHelper import EntityHelper
from classes.GeoLocationAPI import GeoLocationAPI


class GeoLocationHelper(EntityHelper):
    """
    Allows to persist the geolocation using the Persistor class
    """

    def __init__(self):
        """Inheritance of the Persistor class"""
        super().__init__()

    def insert(self, restaurant):
        """
        Inserts the geolocation to the database
        :param restaurant: object restaurant
        """
        db_cursor = self.conn.db_cursor

        geo_location_db = self.select(f"SELECT id FROM geolocation WHERE tripadvisor_id = {restaurant.key}")

        if not geo_location_db:
            lat, lng = GeoLocationAPI().request(restaurant.address + " " + restaurant.city.name)
            self.persist("INSERT INTO geolocation (lat, lng, tripadvisor_id) VALUES (%s, %s, %s)",
                         (lat, lng, restaurant.key))
