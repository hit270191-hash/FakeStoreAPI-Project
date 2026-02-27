from dataclasses import asdict

import pytest
import requests
import json
from routes.Routes import Routes
from datamodels.Product import Product
from utils.DataProviders import read_json_data
from utils.DataProviders import read_excel_data
import os

#Get file path
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testData", "product.json"))
# xlpath= os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testData", "product.xlsx"))

class TestProductAPI:
    @pytest.fixture(autouse=True)
    def ini_class_var(self, setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]

    @pytest.mark.regression
    @pytest.mark.parametrize("order_data", read_json_data(path))
    # @pytest.mark.parametrize("order_data", read_excel_data(xlpath, sheet_name="Sheet1"))
    def test_add_new_delete_product(self,order_data):
        product_data= order_data[0]         #to run for excel remove [0]

        #Extract fields
        title= product_data["title"]
        description= product_data["description"]
        price= product_data["price"]
        category= product_data["category"]
        image= product_data["image"]

        payload= Product(title, description, price, category, image)

        #Adding Product
        # response= requests.post(self.base_url+Routes.CREATE_PRODUCT, json=payload.__dict__)
        response = requests.post(self.base_url + Routes.CREATE_PRODUCT, json= asdict(payload))
        assert response.status_code == 201
        data = response.json()
        # print(json.dumps(data, indent=4))

        #Validation
        assert data["title"] == title
        product_id = data["id"]

        #Delete Product
        endpoint= self.base_url+Routes.DELETE_PRODUCT.format(id= product_id)
        response= requests.delete(endpoint)
        assert response.status_code == 200


