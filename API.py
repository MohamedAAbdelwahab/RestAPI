import json

import requests
import time
import request_cache

requests_cache.install_cache(cache_name='My_cache', backend='sqlite', expire_after=10)


class BaseAPI:

    def __init__(self):
        self.__api_url_base = 'https://restcountries.eu/rest/v2/name/'



    def get_country_info(self, country):
        api_url = self.__api_url_base + country

        response = requests.get(api_url)



        if response.status_code == 200:
            return json.loads(response.content)[0]
        else:
            return "Not Found"