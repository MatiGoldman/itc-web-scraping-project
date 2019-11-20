import requests
from bs4 import BeautifulSoup as bs

from classes.Restaurant import Restaurant


class RestaurantScrapper:
    """ TripAdvisor restaurant scrapper, put the city id and get the restaurants"""

    def __init__(self, city_id):
        """
        :param city_id: the code of the city in tripAdvisor, it is inside the url.
        EX:
        url: https://www.tripadvisor.com/Restaurants-g293984-Tel_Aviv_Tel_Aviv_District.html
        the id is between Restaurants- and -Tel_Aviv: g293984

        """
        self.WEB_URL = "https://www.tripadvisor.com"
        self.RESTAURANTS_URL = f"/Restaurants-{city_id}-xxx.html"

    def _create_parser(self, url):
        """
        Creates a parser
        :param url: string
        :return: string
        """
        # TODO: use TALanguage cookie set to ALL.
        response = requests.get(url)
        content = response.content
        parser = bs(content, 'html.parser')
        return parser

    def _get_urls(self, pages):
        """
        Gets the urls of all the restaurants in different pages
        :param pages: number of pages that you want to explore

        :return: list
        """
        parser = self._create_parser(self.WEB_URL + self.RESTAURANTS_URL)

        urls = []
        for _ in range(pages):
            raw_urls = parser.find_all("a", class_="restaurants-list-ListCell__restaurantName--2aSdo", href=True)
            urls.extend([url["href"] for url in raw_urls])
            next_page = parser.find("a", class_="nav next rndBtn ui_button primary taLnk", href=True)["href"]
            parser = self._create_parser(self.WEB_URL + next_page)

        return urls

    def _get_url_key(self, url):
        """Splits the url and gets key
        :param url: string
        :return: int
        """
        return int(url.split("-")[2][1:])

    def _get_country(self, parser):
        """ parse and return the country of the restaurant """
        country_parser = parser.find("span", class_="country-name")
        return country_parser.text if country_parser is not None else ""

    def _get_city(self, parser):
        """ parse and return the city of the restaurant """
        locality_parser = parser.find("span", class_="locality")
        return locality_parser.text if locality_parser is not None else ""

    def _get_address(self, parser):
        """ parse and return the adress of the restaurant """
        address_parser = parser.find("span", class_="street-address")
        return address_parser.text if address_parser is not None else ""

    def _get_rating(self, parser):
        """ parse and return the rating of the restaurant """
        raw_rating = parser.find("span",
                                 class_="restaurants-detail-overview-cards-RatingsOverviewCard__overallRating--nohTl")
        return float(raw_rating.text.replace("\xa0", ""))

    def _get_review(self, parser):
        """ parse and return the review of the restaurant """
        raw_review = parser.find("span", class_="reviewCount")
        review = int(raw_review.text.split()[0].replace(",", ""))
        return review

    def _get_name(self, parser):
        """ parse and return the name of the restaurant """
        raw_name = parser.find("h1", class_="ui_header h1")
        return raw_name.text

    def get_restaurants(self, pages):
        """
        Scrap the data from each of the restaurants urls
        :param pages: number of pages that you want to explore
        :return: list(Restaurant)
        """
        print("Scrapping {} page".format(pages)) if pages == 1 else print("Scrapping {} pages".format(pages))

        urls = self._get_urls(pages)
        restaurants = []

        for url in urls:
            full_url = self.WEB_URL + url
            print(f"Scrapping {full_url}")
            parser = self._create_parser(full_url)

            key = self._get_url_key(url)
            name = self._get_name(parser)
            review = self._get_review(parser)
            rating = self._get_rating(parser)
            address = self._get_address(parser)
            city = self._get_city(parser)
            country = self._get_country(parser)

            restaurants.append(Restaurant(key, name, review, rating, address, city, country))

        return restaurants
