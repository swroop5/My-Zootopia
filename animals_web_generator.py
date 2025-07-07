import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for item in animals_data:
    #print(item)
    if 'name' in item:
        print(f'Name: {item["name"]}')
    if 'characteristics' in item:
        if 'diet' in item["characteristics"]:
            print(f'Diet:  {item["characteristics"]["diet"]}')
    if 'locations' in item:
        print(f'Location: {item["locations"][0]}')
    if 'characteristics' in item:
        if 'type' in item["characteristics"]:
            print(f'Type: {item["characteristics"]["type"]}')
    print()