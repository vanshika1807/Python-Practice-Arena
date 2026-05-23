import json

person = {
    "name": "Vanshika",
    "age": 22
}

with open("data.json", "w") as f:
    json.dump(person, f, indent=4)