import datetime


class Restaurant:
    """ Represent a restaurant in TripAdvisor"""

    def __init__(self, key, name, review, rating, address, city, country):
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
        self.city = city
        self.country = country
        self.timestamp = datetime.datetime.now()
