import requests
import pytest


class TestRequestHeader:
    def test_request_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")

        assert response.status_code == 200, "Wrong response code"

        assert "x-secret-homework-header" in response.headers, "There is no header x-secret-homework-header1 in the " \
                                                               "headers"
        actual_header_value = response.headers.get('x-secret-homework-header')
        assert actual_header_value == "Some secret value", "Actual header value in the response is not correct"

