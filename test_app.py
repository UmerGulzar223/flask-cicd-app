def test_home():
    from app import app
    client = app.test_client()
    response = client.get('/')
    assert response.data == b'Hello, CI/CD!'
