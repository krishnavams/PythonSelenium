from requests import request
from json import loads

def test_login_positive():
    url = "https://reqres.in/api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    
    response = request("POST", url, json=payload)

    assert response.status_code == 200

    json_string = response.text

    # de-serial
    python_object = loads(json_string)

    is_token_present = "token" in python_object

    assert is_token_present == True

def test_login_negative_missing_pwd():
    url = "https://reqres.in/api/login"
    payload = {
        "email": "eve.holt@reqres.in"
    }
    
    response = request("POST", url, json=payload)

    assert response.status_code == 400

    json_string = response.text

    # de-serial
    python_object = loads(json_string)

    assert python_object['error'] == "Missing password"


def test_login_negative_missing_email():
    url = "https://reqres.in/api/login"
    payload = {
        "password": "cityslicka"
    }
    
    response = request("POST", url, json=payload)

    assert response.status_code == 400

    json_string = response.text

    # de-serial
    python_object = loads(json_string)

    assert python_object['error'] == "Missing email or username"
