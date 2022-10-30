import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
import random
import string

class TestUserRegister(BaseCase):
    exclude_fields = [
        ("no_password"),
        ("no_username"),
        ("no_firstname"),
        ("no_lastname"),
        ("no_email")
    ]
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}{domain}"

    def test_create_user_successfully(self):
        data = {
            'password':'1234',
            'username':'learnqa',
            'firstname':'learnqa',
            'lastname':'learnqa',
            'email': self.email,
        }
        response = requests.post('https://playground.learnqa/api/user', data=data)
        Assertions.assert_code_status(response,200)
        Assertions.assert_json_has_key(response,"id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstname': 'learnqa',
            'lastname': 'learnqa',
            'email': email,
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_with_incorrect_email(self):
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstname': 'learnqa',
            'lastname': 'learnqa',
            'email': self.incorrect_email,
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == "Invalid email format", f"Unexpected response content {response.content}"

    @pytest.mark.parametrize('condition', exclude_fields)
    def test_create_user_without_any_field(self, condition):

        if condition == "no_password":
            response = requests.post('https://playground.learnqa.ru/api/user/',
                                     data={'username': 'learnqa', 'firstname': 'learnqa', 'lastname': 'learnqa', 'email': self.email})
        elif condition == "no_username":
            response = requests.post('https://playground.learnqa.ru/api/user/',
                                     data={'password': '1234', 'firstname': 'learnqa', 'lastname': 'learnqa', 'email': self.email})
        elif condition == "no_firstname":
            response = requests.post('https://playground.learnqa.ru/api/user/',
                                     data={'password': '1234', 'username': 'learnqa', 'lastname': 'learnqa', 'email': self.email})
        elif condition == "no_lastname":
            response = requests.post('https://playground.learnqa.ru/api/user/',
                                     data={'password': '1234', 'username': 'learnqa', 'firstname': 'learnqa', 'email': self.email})
        else:
            response = requests.post('https://playground.learnqa.ru/api/user/',
                                     data={'password': '1234', 'username': 'learnqa', 'firstname': 'learnqa', 'lastname': 'learnqa'})

        field_name = condition.split('_')

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"The following required params are missed: {field_name[1]}", f"Unexpected response content {response.content}"

    def test_create_user_with_long_name(self):
        length = random.randint(251, 1000)
        firstname = ''.join(random.choices(string.ascii_letters, k=length))
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstname': firstname,
            'lastname': 'learnqa',
            'email': self.email,
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == "The value of 'firstname' field is too long", f"Unexpected response content {response.content}"

    def test_create_user_with_short_name(self):
        firstname = ''.join(random.choices(string.ascii_letters, k=1))
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstname': firstname,
            'lastname': 'learnqa',
            'email': self.email,
        }
        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == "The value of 'firstname' field is too short", f"Unexpected response content {response.content}"


