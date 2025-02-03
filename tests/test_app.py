# test_app.py
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app  # Assuming your Flask code is in app.py


# Add the repository root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Simple flask Application' in response.data