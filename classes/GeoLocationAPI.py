import requests
import json

KEY = "key="
JOINT = "&"
LOCATION = "location="
CFG_PATH = '/config.json'

class GeoLocationAPI:
    def __init__(self):
        with open(CFG_PATH) as cfg:
            config = json.load(cfg)

        self.api_url = "http://open.mapquestapi.com/geocoding/v1/address?"
        self.api_key = config['geo_location_key']

    def request(self, loc):
        """Requests to the API the geolocation given a specific location
        :param loc: string"""
        response = requests.get(self.api_url + KEY + self.api_key + JOINT + LOCATION + loc)
        data = response.json()
        lat, lng = self._validate_geolocation(data)
        return lat, lng

    def _validate_geolocation(self, data):
        """Checks if the API could retrieve the geolocation. If not, the API always returns 39.78373 and -100.445882.
        Instead of that, it will return 0 for both lat and lng.
        :param data: dict
        """
        lat = data["results"][0]["locations"][0]["latLng"]["lat"]
        lng = data["results"][0]["locations"][0]["latLng"]["lng"]
        if lat == 39.78373 and lng == -100.445882:
            return None, None
        else:
            return lat, lng
