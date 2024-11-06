import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')



def fetch_data(animal):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
        ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
    },
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal}"
    headers = {
        "X-Api-Key": API_KEY
    }
    res = requests.get(url=url, headers=headers)
    animal = res.json()
    return animal