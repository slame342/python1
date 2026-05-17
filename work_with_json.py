import requests
import json

var_dict1 = dict(Age=24, Name="Ally") # создание словаря
print(var_dict1)

var_dict2 = {"Age": "24", "Name": "Ally"} # создание словаря
print(var_dict2)

var_dict3 = {} # создание словаря
var_dict3["Age"] = "24"
var_dict3["Name"] = "Ally"
print(var_dict3)

var_dict4 = {
    "name": "Alina",
    "address": {
        "street": "Khalglar Dostlugu",
        "city": "Baku",
        "postalCode": 12345
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "123-456-7890"
        },
        {
            "type": "work",
            "number": "111-14-1988"
        }
    ]
}
print(type(var_dict4))

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
json_data = response.content.decode()
print(json_data)

with open("json_data.json", "w") as file:
    json.dump(json_data, file)
    # json.dumps()

# with open("src/dist/new_file.json", "r") as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
#     json.load()
#     json.loads()


