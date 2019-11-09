import requests
from bs4 import BeautifulSoup as bs


TRIP_ADVISOR = "https://www.tripadvisor.com"
RESTAURANTS_URL = "/Restaurants-g293984-Tel_Aviv_Tel_Aviv_District.html"


def get_parser(url):
    response = requests.get(url)
    content = response.content
    parser = bs(content, 'html.parser')
    return parser


def get_urls(parser):
    urls = []
    for _ in range(10):
        raw_urls = parser.find_all("a", class_="restaurants-list-ListCell__restaurantName--2aSdo", href=True)
        urls.extend([url["href"] for url in raw_urls])
        next_page = parser.find("a", class_="nav next rndBtn ui_button primary taLnk", href=True)["href"]
        parser = get_parser(TRIP_ADVISOR + next_page)

    return urls


def get_data(urls):
    names = []
    values = []

    for url in urls:
        parser = get_parser(TRIP_ADVISOR + url)
        raw_name = parser.find("h1", class_="ui_header h1")
        names.append(raw_name.text)

        raw_review = parser.find("span", class_="reviewCount")
        review = int(raw_review.text.split()[0].replace(",", ""))

        raw_rating = parser.find("span",
                                 class_="restaurants-detail-overview-cards-RatingsOverviewCard__overallRating--nohTl")
        rating = float(raw_rating.text.replace("\xa0", ""))
        try:
            raw_address = parser.find("span", class_="street-address").text
        except AttributeError:
            raw_address = ""
        try:
            raw_city = parser.find("span", class_="locality").text
        except AttributeError:
            raw_city = ""
        try:
            raw_country = parser.find("span", class_="country-name").text
        except AttributeError:
            raw_country = ""

        location = raw_address + " " + raw_city + raw_country

        values.append([review, rating, location])

    restaurants = dict(zip(names, values))

    return restaurants


def main():
    parser = get_parser(TRIP_ADVISOR + RESTAURANTS_URL)
    urls = get_urls(parser)
    scrapper_dict = get_data(urls)
    print(scrapper_dict)


if __name__ == "__main__":
    main()
