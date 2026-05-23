import json

person = {
    'name': 'vanshika',
    'age' : 22
}

f = open("data.json", "w")
json.dump(person, f)
f.close()