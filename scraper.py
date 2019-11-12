import requests
from bs4 import BeautifulSoup as bs

TRIP_ADVISOR = "https://www.tripadvisor.com"
RESTAURANTS_URL = "/Restaurants-g293984-Tel_Aviv_Tel_Aviv_District.html"


def get_parser(url):
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


def get_restaurants_urls(parser, pages):
    """
    Gets the urls of all the restaurants in different pages
    :param parser: string
    :param pages: int, amount of pages to scrap
    :return: list
    """
    urls = []
    for _ in range(pages):
        raw_urls = parser.find_all("a", class_="restaurants-list-ListCell__restaurantName--2aSdo", href=True)
        urls.extend([url["href"] for url in raw_urls])
        next_page = parser.find("a", class_="nav next rndBtn ui_button primary taLnk", href=True)["href"]
        parser = get_parser(TRIP_ADVISOR + next_page)

    return urls


def get_url_key(url):
    """Splits the url and gets key
    :param url: string
    :return: int
    """
    return int(url.split("-")[2][1:])


def get_restaurant_data(urls):
    """
    Scrap the data from each of the restaurants urls
    :param urls: list
    :return: dict
    """
    keys = []
    values = []

    for url in urls:
        parser = get_parser(TRIP_ADVISOR + url)

        key = get_url_key(url)
        keys.append(key)

        # TODO isolate in object method
        raw_name = parser.find("h1", class_="ui_header h1")
        name = raw_name.text

        # TODO isolate in object method
        raw_review = parser.find("span", class_="reviewCount")
        review = int(raw_review.text.split()[0].replace(",", ""))

        # TODO isolate in object method
        raw_rating = parser.find("span",
                                 class_="restaurants-detail-overview-cards-RatingsOverviewCard__overallRating--nohTl")
        rating = float(raw_rating.text.replace("\xa0", ""))

        # TODO isolate in object method
        street_address_parsed = parser.find("span", class_="street-address")
        raw_address = street_address_parsed.text if street_address_parsed is not None else ""

        # TODO isolate in object method
        locality_parsed = parser.find("span", class_="locality")
        raw_city = locality_parsed.text if locality_parsed is not None else ""

        # TODO isolate in object method
        country_name_parsed = parser.find("span", class_="country-name")
        raw_country = country_name_parsed.text if country_name_parsed is not None else ""

        location = raw_address + " " + raw_city + raw_country

        values.append({"name": name, "review": review, "rating": rating, "location": location})

    restaurants = dict(zip(keys, values))

    return restaurants


def main():
    """
    Executes the functions to get the web scraped and prints the information
    """
    parser = get_parser(TRIP_ADVISOR + RESTAURANTS_URL)
    urls = get_restaurants_urls(parser, 1)
    scrapper_dict = get_restaurant_data(urls)
    print(scrapper_dict)


if __name__ == "__main__":
    main()
