import pytest
import requests
from lesson8.constants import X_client_URL


@pytest.fixture()
def get_token(username='leyla', password='water-fairy'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(X_client_URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token
