import unittest

import app
from API import BaseAPI
from DataBase import OfflineData


class TestAPI(unittest.TestCase):
#only in online scenario
    def test_info_BaseAPI(self):
        baseAPI = BaseAPI()
        result=baseAPI.get_country_info("Egypt")
        result2=result['name']
        self.assertEqual(result2,"Egypt")