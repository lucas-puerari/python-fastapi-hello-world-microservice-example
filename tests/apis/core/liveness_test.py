def test_liveness(client):
    """
    Test if the application is up and runnig
    """

    response = client.get("/-/healthz")

    assert response.status_code == 200
    assert response.json() == {"statusOk": True}
