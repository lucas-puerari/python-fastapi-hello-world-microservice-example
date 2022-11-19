def test_checkup(client):
    """
    Test the availability of all the service's dependencies
    """

    response = client.get("/-/check-up")

    assert response.status_code == 200
    assert response.json() == {"statusOk": True}
