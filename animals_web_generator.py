import json
import requests



ANIMALS_FILE = "animals_data.json"
HTML_FILE = "animals_template.html"
KEY = "iZlME8CzS4pIYNUSJfhJzQ==COSShqfeyIFzN9Ey"



def API(animal, KEY):
    """"""
    url = f"https://api.api-ninjas.com/v1/animals?name={animal}"
    headers = {
        "X-Api-Key": KEY
    }
    res = requests.get(url=url, headers=headers)
    animal = res.json()
    return animal



def load_json(FILE):
    """Load a json file."""
    with open(FILE, "r") as handle:
        return json.load(handle)


def read_html(FILE):
    """Read the html file."""
    with open(FILE, "r") as handle:
        return handle.read()


def write_html(new_html):
    """Write html file with new code."""
    with open("animals.html","w") as handle:
        handle.write(new_html)


def get_animal_string(animal_obj):
    """Generate the new part of the html file and return it. Output contains the new html."""
    output = ""
    output += '<li class="cards__item">'
    if "name" in animal_obj:
        output += f' <div class="card__title">{animal_obj["name"]}</div>\n<p class="card__text"><ul class="no_dots">\n'
    if "diet" in animal_obj["characteristics"]:
        output += f"<li><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n"
    if "locations" in animal_obj:
        output += f"<li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n"
    if "type" in animal_obj["characteristics"]:
        output += f"<li><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n"
    if "type" in animal_obj["characteristics"]:
        output += f"<li><strong>Life span:</strong> {animal_obj["characteristics"]["lifespan"]}</li>\n"
    output += "</ul></p>\n</li>"
    return output

def print_list_of_skin_types(animals_data):
    """Print hair types available for the user_input."""
    list_of_hairtypes = set()
    for animal in animals_data:
        if "skin_type" in animal["characteristics"]:
            list_of_hairtypes.add(animal["characteristics"]["skin_type"])
    for hairtype in list_of_hairtypes:
        print(hairtype)

def get_skin_type_user():
    """Get the skin type from user input. Try to get input as long as it is correct."""
    while True:
        skin_type = input("Enter a skin type form above: ")
        if skin_type == "Fur" or skin_type == "Scales" or skin_type == "Hair":
            return skin_type


def main():
    animal = input("Enter a name of an animal: ")
    animals_data = API(animal, KEY)
    animal_string = ''
    print_list_of_skin_types(animals_data)
    skin_type = get_skin_type_user()
    for animal_obj in animals_data:
        if animal_obj["characteristics"]["skin_type"] == skin_type:
            animal_string += get_animal_string(animal_obj)
    html = read_html(HTML_FILE)
    new_html = html.replace("__REPLACE_ANIMALS_INFO__", animal_string)
    write_html(new_html)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()