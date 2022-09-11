from chalice.test import Client
from app import app


def test_index():
    with Client(app) as client:
        response = client.lambda_.invoke('renew_tls', {})
        assert response.payload is not None
