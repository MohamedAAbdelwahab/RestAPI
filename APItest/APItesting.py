import unittest

import requests_cache
from mock import patch, Mock
import app
from API import BaseAPI
from DataBase import OfflineData

class TestAPI(unittest.TestCase):

    # only in online scenario
    def test_info_BaseAPI(self):
        baseAPI = BaseAPI()
        result,temp = baseAPI.get_country_info("Egypt")
        result2 = result['name']
        self.assertEqual(result2, "Egypt")
    def test_info_BaseAPI2(self):
        baseAPI = BaseAPI()
        result=baseAPI.get_country_info("Cairo")
        if result=="Not Found":
            self.assertEqual(result,"Not Found")
    #offline functions from class DataBase
    def test_GetData(self):
        offline=OfflineData()
        result=offline.GetData("Egypt")
        result2=result['name']
        self.assertEqual(result2,"Egypt")

    #Some Test Functions
    def test_getSpecificData(self):
        string="capital,population,area"
        result=app.GetSpecificInfo(string,"Egypt")
        self.assertEqual(" area= 1002450.0 population= 91290000 capital= Cairo    ",result)
    def test_getSpecificData2(self):
        string="captiall"
        result=app.GetSpecificInfo(string,"Egypt")
        self.assertEqual("invalid key",result)
    def test_Connection(self): #in online mode only
        self.assertTrue(app.CheckInternetConnection())
    def test_Connection2(self): #in offline mode only
        self.assertTrue(app.CheckInternetConnection())
    def test_APP_gettingdatafn(self): #integration test
        result,temp=app.gettingInfo("egypt")
        actual=result['name']
        self.assertEqual("Egypt",actual)
        requests_cache.clear()


    def testForFalseCash(self):
        result,temp = app.gettingInfo("egypt")
        self.assertFalse(temp)
    def testForTrueCash(self):
        result,temp=app.gettingInfo("egypt")
        self.assertTrue(temp)
        requests_cache.clear()
    def test_offlineGetDataFail(self):
        offline = OfflineData()
        result = offline.GetData("cairo")
        result2 = None
        self.assertEqual(result2, result)
