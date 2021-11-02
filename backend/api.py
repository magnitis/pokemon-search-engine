from flask import Blueprint
from flask_cors import CORS
import requests
import json
import re
import unidecode

api = Blueprint('api', __name__)

#CORS(api)


def pokemon_api(name):
    """
    Pokemon API function to retrieve the intial description.
    """

    base_url = "https://pokeapi.co/api/v2/pokemon-species/"
    request_url = base_url + name.lower()

    response = requests.get(request_url)
    status_code = response.status_code
    
    # Check for error in response
    if status_code == 200:
        response_json = json.loads(response.text)
        # filter out for the engish translations remove any special characters
        description = unidecode.unidecode([en for en in response_json["flavor_text_entries"] if en["language"]["name"] == "en"][0]["flavor_text"])
        clean_description = re.sub(r'[\x00-\x1f]+', ' ', description)
        return status_code, clean_description    
    else:
        error_text = "Error: " + str(status_code) + " : " + response.text
        return status_code, error_text

def shakespeare_api(text):
    """
    Shakespeare API function to retrieve the translation.
    """

    api_params = {"text" : text}
    response = requests.post('https://api.funtranslations.com/translate/shakespeare.json', data=api_params) # headers=headers, data=data

    # Check for errors in response
    if "error" not in response.text.lower():
        response_dict = json.loads(response.text)
        shakespeare_description = response_dict["contents"]["translated"]
        return shakespeare_description
    else:
        error_text = response.text
        return error_text



@api.route('/pokemon/<pokemon_name>', methods=['GET'])
def poke_search(pokemon_name):
    """
    Main GET functionality utilizing the Pokemon and Shakespeare API to retrieve the translation.
    """

    data = {}
    # Pokemon initial description
    try:
        pokemon_initial_decsription = pokemon_api(name=pokemon_name)
        if pokemon_initial_decsription[0] == 200:
            pokemon_description = pokemon_initial_decsription[1]
        else:
            pokemon_name = "'" + pokemon_name + "' is invalid! Please try again!" 
            pokemon_description = "None"
        
    except Exception as e:
        print("Pokemon API issue:", repr(e))

    # Shakespearean description
    try:
        shakespearean_initial_description = shakespeare_api(text=pokemon_description)
        if "error" not in shakespearean_initial_description:
            shakespearean_description = shakespearean_initial_description
        else:
            shakespearean_description = "Unable to retrieve Shakespearean Description: \n" + shakespearean_initial_description
    except Exception as e:
        print("Shakespeare API issue:", repr(e))

    data["name"] = pokemon_name
    data["description"] = shakespearean_description
    
    return data

if __name__ == '__main__':
    api.run()