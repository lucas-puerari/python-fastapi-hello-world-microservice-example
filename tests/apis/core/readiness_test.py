def test_readiness(client):
    """
    Test if the application is ready to handle a new request
    """

    response = client.get("/-/ready")

    assert response.status_code == 200
    assert response.json() == {"statusOk": True}
