import imp
from telnetlib import STATUS
from unittest.mock import patch
import pytest
import unittest
import sys
sys.path.append('C:\\Users\\selva\\Documents\\Nobroker')

from src.house import add_many, view, view_all, add
from src.house import Rent_house,House_list

class Testmongodb():

    @pytest.fixture(autouse=True)
    def mongo_get(self, mongodb):
        resp = mongodb.list_collection_names()
        self.mongodb = mongodb

    def test_view(self):
        with patch('src.house.get_collection') as mock_mongo:
            mock_mongo.return_value = self.mongodb.mycollection
            resp = view(1)
            assert resp

    # def test_fail_to_view(self):
    #     with patch('src.house.get_collection') as mock_mongo:
    #         mock_mongo.return_value = self.mongodb.mycollection
    #         resp = view(3)
    #         if not resp:
    #             pytest.fail(f"error on adding list : {resp}")
    #         assert resp 

    def test_view_all(self):
        with patch('src.house.get_collection') as mock_mongo:
            mock_mongo.return_value = self.mongodb.mycollection
            resp = view_all()
            assert resp

    def test_add(self):
        with patch('src.house.get_collection') as mock_mongo:
            mock_mongo.return_value = self.mongodb.mycollection
            d = {"house_id": 3, "place": "selaiyur",
                 "squarefeet": 1200, "type": "3bhk", "rent": 18000}
            resp = add(d)
            assert resp

    def test_add_many(self):
        with patch('src.house.get_collection') as mock_mongo:
            mock_mongo.return_value = self.mongodb.mycollection
            d = [{"house_id": 4, "place": "medavakkam",
                 "squarefeet": 1200, "type": "3bhk", "rent": 18000},
                 {"house_id": 5, "place": "sipcot",
                 "squarefeet": 1200, "type": "3bhk", "rent": 18000}
            ]
            houselist = House_list(data=d)
            resp = add_many(house=houselist)
            
            assert resp == {"status":200}