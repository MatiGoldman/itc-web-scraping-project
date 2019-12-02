import datetime
from classes.City import City

ID_LIMITOR = 1


class Restaurant:
    """ Represent a restaurant in TripAdvisor"""

    def __init__(self, key, name, review, rating, address, city, city_id, country):
        """
        Initialize all of the values

        :param key: restaurant id
        :param name:
        :param review:
        :param rating:
        :param address:
        :param city:
        :param country:
        """
        self.key = key
        self.name = name
        self.review = review
        self.rating = rating
        self.address = address
        self.city = City(city_id, city)
        self.country = country
        self.timestamp = datetime.datetime.now()
