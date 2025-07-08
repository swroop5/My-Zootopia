import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for item in animals_data:
    print('<li class="cards__item">')

    if 'name' in item:
        print(f'<div class="card__title">{item["name"]}</div>')
    print('<p class="card__text">')
    if 'characteristics' in item:
        if 'diet' in item["characteristics"]:
            print(f'<strong>Diet:</strong>  {item["characteristics"]["diet"]}<br/>')
    if 'locations' in item:
        print(f'<strong>Location:</strong> {item["locations"][0]}<br/>')
    if 'characteristics' in item:
        if 'type' in item["characteristics"]:
            print(f'<strong>Type:</strong> {item["characteristics"]["type"]}<br/>')
    print('</p>')
    print('</li>')
    print()