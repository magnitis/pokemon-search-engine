from backend.api import pokemon_api, shakespeare_api
import pytest

@pytest.mark.parametrize("pokemon_name, content, code",[
    ("pikachu", "electricity", 200),
    ("snorlax", "lazy", 200),
    ("jigglypuffs", "Error", 404)
    ])

# test pokemon api
def test_pokemon_only(pokemon_name, content, code):
    """
    GIVEN a Pokemon name
    WHEN the response is retrieved
    THEN check the status code and content.
    """
    response = pokemon_api(name=pokemon_name)

    # test status code
    assert response[0] == code
    # test response content
    assert content in response[1]


# test shakespeare api
@pytest.mark.parametrize("description, content",[
    ("I would like to get a translation please", "prithee"),
    ("My favourite part of the day is morning", "minion")
    ])

def test_shakespeare_only(description, content):
    """
    GIVEN a random description
    WHEN the response is retrieved
    THEN check the translated content.
    """
    response = shakespeare_api(text=description)

    # test response content
    assert content in response