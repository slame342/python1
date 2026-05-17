import requests


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

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print(response.content.decode())