import requests
import json


x = 'apples'
y = 'lemons'
z = 'In the basket are %s and %s' % (x, y)
print(z)



url = "https://jsonplaceholder.typicode.com/posts"
# url = "https://api.instantwebtools.net/v1/airlines"
response = requests.get(url)
content = response.content
print(type(content))
json_data = content.decode()
print(type(json_data))
# print(json_data)
airlines = json.loads(json_data)
print(type(airlines))
print(airlines[0:2])
# print(type(json.load(json_data)))


for airline in airlines[0:2]:
    # with open(f"temp/data.{airline['id']}.json", 'w') as file:
    #     json.dump(airline, file)
    # with open("temp/data" + airline['id'] + '.json', 'w') as file:
    #     json.dump(airline, file)
    with open("temp1/data_%s.json"  % airline['id'], 'w') as file:
        json.dump(airline, file)
#     # json.dumps()

# with open("src/dist/new_file.json", "r") as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
#     json.load()
#     json.loads()