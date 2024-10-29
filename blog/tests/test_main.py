from fastapi.testclient import TestClient

from blog.main import app

client = TestClient(app)

# test functions are to not be async

def test_main_app():
    response = client.get('/')
    assert response.status_code == 200