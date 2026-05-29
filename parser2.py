import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
# url = "https://api.instantwebtools.net/v1/airlines"
response = requests.get(url)
content = response.content
print(type(content))
json_data = content.decode()
print(type(json_data))
print(json_data)
airlines = json.loads(json_data)
# print(type(json.load(json_data)))


for airline in airlines:
    with open(f"temp/data.{airline['id']}.json", 'w') as file:
        json.dump(airline, file)
#     # json.dumps()

# with open("src/dist/new_file.json", "r") as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
#     json.load()
#     json.loads()