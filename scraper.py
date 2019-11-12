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

    restaurants = []

    for url in urls:
        parser = get_parser(TRIP_ADVISOR + url)

        key = get_url_key(url)

        raw_name = parser.find("h1", class_="ui_header h1")
        name = raw_name.text

        raw_review = parser.find("span", class_="reviewCount")
        review = int(raw_review.text.split()[0].replace(",", ""))

        raw_rating = parser.find("span",
                                 class_="restaurants-detail-overview-cards-RatingsOverviewCard__overallRating--nohTl")
        rating = float(raw_rating.text.replace("\xa0", ""))

        # TODO think a way to make this if statements more pretty
        if parser.find("span", class_="street-address") is not None:
            raw_address = parser.find("span", class_="street-address").text
        else:
            raw_address = ""

        if parser.find("span", class_="locality") is not None:
            raw_city = parser.find("span", class_="locality").text
        else:
            raw_city = ""

        if parser.find("span", class_="country-name") is not None:
            raw_country = parser.find("span", class_="country-name").text
        else:
            raw_country = ""

        location = raw_address + " " + raw_city + raw_country

        restaurants.append({"key": key, "name": name, "review": review, "rating": rating, "location": location})

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
