# ITC Data Mining Project

### Description

This web scraper is for the ITC Datamining Project (https://www.itc.tech/)
Its intention is to scrap the tripadvisor web to find restaurants.

### Usage

`python3 main.py {ID} --pages={NUMBER_OF_PAGES}`

#### EX:

URL: https://www.tripadvisor.com/Restaurants-g293984-Tel_Aviv_Tel_Aviv_District.html

The id is between Restaurants- and -Tel_Aviv: **g293984**, therefore `python3 main.py g293984 --pages=1`


### Installation
#### Database Config
The database schema is `tripAdvisorScrapper.sql`

Please create file `/config.json` accordingly to your parameters.

#### config.json example
````
{
  "db": {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "tripAdvisorScrapper"
  },
  "geo_location_key": "YOUR_KEY"
}
````
