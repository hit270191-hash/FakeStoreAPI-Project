from dataclasses import asdict
import pytest
import requests
import json
from routes.Routes import Routes
from payloads.Payloads import Payloads

class TestUserAPI:
    @pytest.fixture(autouse=True)
    def ini_class_var(self, setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]
        self.payload= Payloads().user_payload()

    @pytest.mark.regression
    @pytest.mark.run(order=1)
    def test_get_all_users(self):
        response= requests.get(self.base_url+Routes.GET_ALL_USERS)
        assert response.status_code == 200
        data= response.json()
        # print(json.dumps(data, indent=4))
        assert len(data)>0

    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    def test_get_user_by_id(self):
        user_id= self.config.get_property("userId")
        endpoint= self.base_url+Routes.GET_USER_BY_ID.format(id= user_id)
        response= requests.get(endpoint)
        assert response.status_code == 200
        data= response.json()
        # print(json.dumps(data, indent=4))

    @pytest.mark.sanity
    @pytest.mark.run(order=3)
    def test_get_user_by_limit(self):
        limit= self.config.get_property("limit")
        endpoint= self.base_url+Routes.GET_USER_WITH_LIMIT.format(limit= limit)
        response= requests.get(endpoint)
        assert response.status_code == 200
        data= response.json()
        # print(json.dumps(data, indent=4))
        assert len(data)== int(limit)

    @pytest.mark.regression
    @pytest.mark.run(order=4)
    def test_get_user_sorted_desc(self):
        endpoint= self.base_url+Routes.GET_USER_SORTED.format(order= "desc")
        response= requests.get(endpoint)
        assert response.status_code == 200
        data= response.json()
        # print(json.dumps(data, indent=4))
        ids= [user["id"] for user in data]
        assert ids == sorted(ids, reverse= True)

    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    def test_get_user_sorted_asc(self):
        endpoint= self.base_url+Routes.GET_USER_SORTED.format(order= "asc")
        response= requests.get(endpoint)
        assert response.status_code == 200
        data= response.json()
        # print(json.dumps(data, indent=4))
        ids= [user["id"] for user in data]
        assert ids == sorted(ids)

    @pytest.mark.dependency(name= 'create_user')
    @pytest.mark.regression
    @pytest.mark.run(order=6)
    def test_create_user(self):
        user_payload= self.payload
        response= requests.post(self.base_url+Routes.CREATE_USER, json= asdict(user_payload))
        assert response.status_code == 201
        data= response.json()
        # print(json.dumps(data, indent=4))
        assert 'id' in data
        print('Generated Userid:', data['id'])

    @pytest.mark.dependency(depends= ['create_user'])
    @pytest.mark.regression
    @pytest.mark.run(order=7)
    def test_update_user(self):
        user_id= self.config.get_property("userId")
        updated_user= self.payload
        endpoint= self.base_url+Routes.UPDATE_USER.format(id= user_id)
        response= requests.put(endpoint, json= asdict(updated_user))
        assert response.status_code == 200
        data= response.json()
        # print(json.dumps(data, indent=4))
        assert data['username']== updated_user.username

    @pytest.mark.dependency(depends=['create_user'])
    @pytest.mark.regression
    @pytest.mark.run(order=8)
    def test_delete_user(self):
        user_id= self.config.get_property("userId")
        endpoint= self.base_url+Routes.DELETE_USER.format(id= user_id)
        response= requests.delete(endpoint)
        assert response.status_code == 200

