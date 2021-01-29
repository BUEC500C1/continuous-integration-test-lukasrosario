def test_index(client):
    rv = client.get("/")
    assert b"Enter a conversion question below!" in rv.data
