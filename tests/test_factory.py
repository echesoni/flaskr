from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

# test checks that response to '/hello' route is 'Hello, World!'
def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
