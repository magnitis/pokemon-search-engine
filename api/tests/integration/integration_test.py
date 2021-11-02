import pytest

@pytest.mark.parametrize("pokemon_name, content",[
    ("pikachu", "electricity"),
    ("snorlax", "rotund")
    ])

# Test overall GET endpoint functionality
def test_api_functionality(get, pokemon_name, content):
    """
    GIVEN a Pokemon name
    WHEN the response is retrieved
    THEN check the status code and translated content.
    """
    response = get("/pokemon/" + pokemon_name)
    # test status code
    assert response.status_code == 200
    # test response content
    assert content.encode() in response.data


