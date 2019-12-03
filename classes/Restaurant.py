import datetime
from classes.City import City

ID_LIMITOR = 1


class Restaurant:
    """ Represent a restaurant in TripAdvisor"""

    def __init__(self, key, name, review, rating, address, city, city_id, country):
        """
        Initialize the information related to a restaurant

        :param key: int
        :param name: string
        :param review: int
        :param rating: float
        :param address: str
        :param city: str
        :param country: str
        """
        self.key = key
        self.name = name
        self.review = review
        self.rating = rating
        self.address = address
        self.city = City(city_id, city)
        self.country = country
        self.timestamp = datetime.datetime.now()
