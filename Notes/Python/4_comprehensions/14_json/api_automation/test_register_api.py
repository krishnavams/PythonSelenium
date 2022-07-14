from requests import request
from json import loads

def test_registration_positive():
    url = "https://reqres.in/api/register"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = request("POST", url, json=payload)

    assert response.status_code == 200

    json_string = response.text

    # de-serial
    python_object = loads(json_string)

    is_token_present = 'token' in python_object

    print(python_object['token'])

    assert is_token_present == True


def test_registration_negative_missing_pwd():
    url = "https://reqres.in/api/register"

    payload = {
        "email": "eve.holt@reqres.in"
    }

    response = request("POST", url, json=payload)

    assert response.status_code == 400

    print(response.text)

def test_registration_negative_missing_email():
    url = "https://reqres.in/api/register"

    payload = {
        "password": "Password123"
    }

    response = request("POST", url, json=payload)

    assert response.status_code == 400

    print(response.text)