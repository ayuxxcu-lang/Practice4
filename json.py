# json.py

import json

# Python dictionary
data = {
    "name": "Aigerim",
    "age": 19,
    "city": "Almaty"
}

# Convert Python to JSON
json_data = json.dumps(data)
print(json_data)

# Write to file
with open("sample.json", "w") as file:
    json.dump(data, file)

# Read JSON file
with open("sample.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)