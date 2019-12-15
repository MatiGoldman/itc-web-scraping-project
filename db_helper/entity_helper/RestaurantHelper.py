from db_helper.entity_helper.EntityHelper import EntityHelper
import logging


class RestaurantHelper(EntityHelper):
    """Inserts the restaurants into the database"""

    def __init__(self):
        super().__init__()

    def insert(self, restaurant):
        """
        Inserts a restaurant into a db
        :param restaurant: restaurant to insert
        """
        self.persist('''
            INSERT INTO restaurant(
                name,
                review,
                rating,
                address,
                timestamp,
                tripadvisor_id,
                city_id
            )
            VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );
        ''', (
            restaurant.name,
            restaurant.review,
            restaurant.rating,
            restaurant.address,
            restaurant.timestamp,
            restaurant.key,
            restaurant.city.id
        )
                     )
