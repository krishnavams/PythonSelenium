from requests import request
import json
from pytest import mark

emails = [
    ("hello.world", "failure"),
    ("hello.world@company.com", "success"),
    ("hello.world@", "failure"),
    ("hello.world@.com", "failure"),
    ("hello.world@company.gov.in", "success"),
    ("hello.world@company.edu", "success")
    ]

@mark.parametrize("email, expected_result", emails)
def test_email(email, expected_result):
    response = request("GET", f"https://api.eva.pingutil.com/email?email={email}")
    print(f'Hitting URL: https://api.eva.pingutil.com/email?email={email}')
    r = json.loads(response.text)
    actual_response = response['data']['valid_syntax']
    assert expected_result == actual_response
