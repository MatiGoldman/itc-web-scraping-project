from classes.RestaurantScrapper import RestaurantScrapper


def main():
    """
    Executes the functions to get the web scraped and prints the information
    """
    scrapper_data = RestaurantScrapper('g293984').get_restaurants(2)
    for restaurant in scrapper_data:
        print(restaurant.__dict__)


if __name__ == "__main__":
    main()
