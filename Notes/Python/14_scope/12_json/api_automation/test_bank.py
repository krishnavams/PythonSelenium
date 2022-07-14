from requests import request
import json
from pytest import mark

codes = [
    ("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
    ("SBIN0040014","BASAVANAGUDI"),
    ("ICIC0000002", "BANGALORE - M G ROAD")
    ]

@mark.parametrize("code, expected_branch", codes)
def test_email(code, expected_branch):
    response = request("GET", f"https://ifsc.razorpay.com/{code}")
    print(f'Hitting URL: "https://ifsc.razorpay.com/{code}')
    r = json.loads(response.text)
    assert r['BRANCH'] == expected_branch