from classes.RestaurantScrapper import RestaurantScrapper
from persistor.RestaurantPersistor import RestaurantPersistor
from persistor.CityPersistor import CityPersistor
import argparse


def check_positive(value):
    """Checks if the value of the pages is positive. Otherwise will raise an error
    :param value: str
    :returns: int
    """
    if int(value) <= 0:
        raise argparse.ArgumentTypeError("Please, enter a positive number")
    return int(value)


def get_city_page():
    """Parse the arguments from the CLI. It is asked to provide a city and the amount of cities to be scrapped
    (default = 1)
    returns: city, pages
    """
    parser = argparse.ArgumentParser(description='''Please, write the code related to the city. Example
        url: https://www.tripadvisor.com/Restaurants-g293984-Tel_Aviv_Tel_Aviv_District.html
        The code is between Restaurants - and - Tel_Aviv: g293984
                                                 ''')
    parser.add_argument("city", help="The city code to be scrapped.")
    parser.add_argument("--pages", help="The amount of pages to be scrapped.", default=1, type=check_positive)
    args = parser.parse_args()
    return args.city, args.pages


def save_data(scrapper_data):
    """For each of the cities and restaurant, the data is saved into the database"""
    print(f'Persisting {len(scrapper_data)} results')

    restaurant_persistor, city_persistor = RestaurantPersistor(), CityPersistor()

    city_persistor.insert(scrapper_data[0].city)
    city_persistor.commit()

    for restaurant in scrapper_data:
        restaurant_persistor.insert(restaurant)

    restaurant_persistor.commit()

    print('Done.')


def main():
    """
    Executes the functions to get the web scraped and prints the information
    """

    city, pages = get_city_page()
    scrapper_data = RestaurantScrapper(city).get_restaurants(pages)
    save_data(scrapper_data)


if __name__ == "__main__":
    main()
