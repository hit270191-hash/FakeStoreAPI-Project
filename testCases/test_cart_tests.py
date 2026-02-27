from dataclasses import asdict

import requests
import json
from routes.Routes import Routes
from payloads.Payloads import Payloads
import pytest
from utils.date_utils import validate_cart_dates_within_range

class TestCartsAPI:
    @pytest.fixture(autouse=True)
    def ini_class_var(self, setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]
        self.payload= Payloads()

    def test_get_all_carts(self):
        response = requests.get(self.base_url+Routes.GET_ALL_CART)
        assert response.status_code == 200
        data=response.json()
        print(data)
        assert len(data)>0

    def test_get_cart_by_id(self):
        user_id= self.config.get_property("cartId")
        response = requests.get(self.base_url+Routes.GET_CART_BY_ID.format(id= user_id))
        assert response.status_code == 200

    def test_get_cart_by_date(self):
        start_date= self.config.get_property("startdate")
        end_date= self.config.get_property("enddate")
        endpoint= self.base_url+Routes.GET_CART_SORTED_BY_DATE.format(
            start_date= start_date,
            end_date= end_date)
        response = requests.get(endpoint)
        assert response.status_code == 200
        data=response.json()
        # print(json.dumps(data, indent=4))
        cart_dates= [item["date"] for item in data]
        assert validate_cart_dates_within_range(cart_dates, start_date, end_date)


    def test_get_user_cart(self):
        user_id= self.config.get_property("userId")
        endpoint= self.base_url+Routes.GET_USER_CART.format(id= user_id)
        response = requests.get(endpoint)
        assert response.status_code == 200
        data=response.json()
        # print(json.dumps(data, indent=4))
        for item in data:
            assert item["userId"]== int(user_id)

    def test_create_cart(self):
        user_id= self.config.get_property("userId")
        cart= self.payload.cart_payload(user_id)
        response = requests.post(self.base_url+Routes.CREATE_CART,json=asdict(cart))
        assert response.status_code == 201
        data=response.json()
        print(json.dumps(data, indent=4))
        assert data["userId"] is not None
        assert data["id"] is not None
        assert len(data["products"]) > 0

    def test_update_cart(self):
        user_id= self.config.get_property("userId")
        cart_id= self.config.get_property("cartId")
        cart= self.payload.cart_payload(user_id)
        endpoint= self.base_url+Routes.UPDATE_CART.format(id= cart_id)
        response = requests.put(endpoint, json=asdict(cart))
        assert response.status_code == 200
        data=response.json()
        # print(json.dumps(data, indent=4))
        assert data["id"] == int(cart_id)
        assert data["userId"] == user_id
        assert len(data["products"]) ==1


    def test_delete_cart(self):
        user_id= self.config.get_property("userId")
        cart_id= self.config.get_property("cartId")
        cart= self.payload.cart_payload(user_id)
        endpoint= self.base_url+Routes.DELETE_CART.format(id= cart_id)
        response = requests.delete(endpoint, json=asdict(cart))
        assert response.status_code == 200









