import pytest
import requests

url = 'http://127.0.0.1:5000' # The root url of the bank app

def test_index_page():              #test to get the index page
    r = requests.get(url + '/')
    assert r.status_code == 200

def test_get_users():               #test to fetch all users
    r = requests.get(url + '/bank_users/')
    assert r.status_code == 200

    data = r.json()
    assert len(data) > 0

def test_no_user():                 #test to check the non existing user
    r = requests.get(url + '/bank_users/aaaa')
    assert r.status_code == 404

def test_get_user():                #test to fetch the existing user
    r = requests.get(url + '/bank_users/jagriti')
    assert r.status_code == 200

    data = r.json()
    assert len(data) > 0
    assert data["username"] == "jagriti"