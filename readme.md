# ITC Data Mining Project

### This web scraper is for the ITC Datamining Project

Its intention is to scrap the tripadvisor web to find restaurants.

### USAGE

`python3 main.py {ID} --pages={NUMBER_OF_PAGES}`

#### EX:

URL: https://www.tripadvisor.com/Restaurants-g293984-Tel_Aviv_Tel_Aviv_District.html

The id is between Restaurants- and -Tel_Aviv: **g293984**, therefore `python3 main.py g293984 --pages=1`



### Database Config
The database schema is `tripAdvisorScrapper.sql`

Please modify `db_helper/config.json` accordingly to your parameters.

#### DB Config file
````
{
  "host": YOUR_HOST,
  "user": YOUR_USER,
  "password": YOUR_PASSWORD,
  "database": "tripAdvisorScrapper"
}
````
