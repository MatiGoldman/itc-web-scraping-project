from classes.RestaurantScrapper import RestaurantScrapper
from db_helper.entity_helper.GeoLocationHelper import GeoLocationHelper
from db_helper.entity_helper.RestaurantHelper import RestaurantHelper
from db_helper.entity_helper.CityHelper import CityHelper
from db_helper.MysqlConnection import MysqlConnection
import argparse
import logging

CITY_CODE = 1

def check_positive(value):
    """Checks if the value of the pages is positive. Otherwise will raise an error
    :param value: str
    :returns: int
    """
    if int(value) <= 0:
        raise argparse.ArgumentTypeError("Please, enter a positive number")
    return int(value)


def get_city_code(url):
    return url.split("-")[CITY_CODE]


def get_city_page():
    """Parse the arguments from the CLI. It is asked to provide a city and the amount of cities to be scrapped
    (default = 1)
    returns: city, pages
    """
    parser = argparse.ArgumentParser(description='''Please, enter the url related to the city. Example
        url: https://www.tripadvisor.com/Restaurants-g293984-Tel_Aviv_Tel_Aviv_District.html
                                                 ''')
    parser.add_argument("url", help="The url to be scrapped.")
    parser.add_argument("--pages", help="The amount of pages to be scrapped.", default=1, type=check_positive)
    args = parser.parse_args()
    city = get_city_code(args.url)
    return city, args.pages


def save_data(scrapper_data):
    """For each of the cities and restaurants, the data is saved into the database"""
    print(f'Persisting {len(scrapper_data)} results')

    restaurant_persistor, city_persistor, geo_location_persistor = RestaurantHelper(), CityHelper(), GeoLocationHelper()

    city_persistor.insert(scrapper_data[0].city)

    print("Retrieving geolocation for each restaurant...")
    for restaurant in scrapper_data:
        restaurant_persistor.insert(restaurant)
        geo_location_persistor.insert(restaurant)

    MysqlConnection().close()
    print('Done.')


def main():
    """
    Executes the functions to get the web scraped and prints the information
    """
    logging.basicConfig(filename='app.log', format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

    city, pages = get_city_page()
    scrapper_data = RestaurantScrapper(city).get_restaurants(pages)
    save_data(scrapper_data)


if __name__ == "__main__":
    main()
