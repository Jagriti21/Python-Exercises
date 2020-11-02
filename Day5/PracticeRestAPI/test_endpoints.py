import pytest
import requests

url = 'http://127.0.0.1:5000' # The root url of the flask app

def test_index_page():
    r = requests.get(url + '/')
    assert r.status_code == 200

def test_get_developers():
    r = requests.get(url + '/developers/')
    assert r.status_code == 200

    data = r.json()
    assert len(data) > 0

def test_get_developer():
    r = requests.get(url + '/developers/3')
    assert r.status_code == 200

    data = r.json()
    assert len(data) > 0
    assert data["name"] == "james"

def test_get_developer_skills():
    r = requests.get(url + '/developers/2')
    assert r.status_code == 200

    data = r.json()
    assert len(data) > 0
    assert data["name"] == "jane"
    assert "java" in data["skills"]
    assert "jsp" in data["skills"]
    assert "python" not in data["skills"]

def test_no_developer():
    r = requests.get(url + '/developers/13')
    assert r.status_code == 404