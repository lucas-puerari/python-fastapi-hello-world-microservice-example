def test_hello_world(client):
    """
    Test say Hello
    """

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
