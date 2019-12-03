from persistor.Persistor import Persistor


class RestaurantPersistor(Persistor):
    """Inserts the restaurants into the database"""
    def __init__(self):
        super().__init__()

    def insert(self, restaurant):
        self.conn.db_cursor.execute('''
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
        ))
