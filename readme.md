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
  "db": {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "tripAdvisorScrapper"
  },
  "geo_location_key": YOUR_KEY"
}
````

#### Config file for API KEY
Please, create your own `config.py` file to use your own API KEY.
The file should have the following line:

`API_KEY = "YOUR_API_KEY"`
