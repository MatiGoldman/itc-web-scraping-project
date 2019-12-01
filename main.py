from classes.RestaurantScrapper import RestaurantScrapper
import argparse
import mysql.connector

HOST = 'localhost'
USER = 'root'
PASSWD = ''
DATABASE = 'tripAdvisorScrapper'


def check_positive(value):
    if int(value) <= 0:
        raise argparse.ArgumentTypeError("Please, enter a positive number")


def get_city_page():
    parser = argparse.ArgumentParser(description='''Please, write the code related to the city. Example
        url: https://www.tripadvisor.com/Restaurants-g293984-Tel_Aviv_Tel_Aviv_District.html
        The code is between Restaurants - and - Tel_Aviv: g293984
                                                 ''')
    parser.add_argument("city", help="The city code to be scrapped.")
    parser.add_argument("--pages", help="The amount of pages to be scrapped.", default=1, type=check_positive)
    args = parser.parse_args()
    print(args)
    return args.city, args.pages


def save_data(city, scrapper_data):
    print(f'Persisting {len(scrapper_data)} results')

    city_id = city[1:]
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        database=DATABASE
    )
    db_cursor = mydb.cursor()

    db_cursor.execute(f"SELECT id FROM city WHERE id = {city_id}")
    city_db = db_cursor.fetchall()

    if len(city_db) == 0:
        db_cursor.execute("INSERT INTO city (id, name) VALUES (%s, %s)", (city_id, scrapper_data[0].city))

    for restaurant in scrapper_data:
        db_cursor.execute('''
            INSERT INTO restaurant(
                name,
                review,
                rating,
                address,
                timestamp,
                tripadvisor_id,
                city_id
            )
            VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );
        ''', (
            restaurant.name,
            restaurant.review,
            restaurant.rating,
            restaurant.address,
            restaurant.timestamp,
            restaurant.key,
            city_id
        ))

        mydb.commit()

        print('Done.')


def main():
    """
    Executes the functions to get the web scraped and prints the information
    #TODO Modificar el envio por parametro de la url/codigo
    """

    city, pages = get_city_page()
    scrapper_data = RestaurantScrapper(city).get_restaurants(pages)

    save_data(city, scrapper_data)


if __name__ == "__main__":
    main()
