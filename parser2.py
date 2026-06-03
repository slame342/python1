import requests
import json


# url = "https://jsonplaceholder.typicode.com/posts/4"
# response = requests.get(url)
# # http - ответ, content, данные, статус код = статус запроса
# print(response.status_code)
# content = response.content.decode()
# print(content)


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
# print(airlines[1:11:2)
# print(type(json.load(json_data)))


for airline in airlines[1:11:2]:
    with open(f"temp/data_{airline['id']}.json", 'w') as file:
        json.dump(airline, file)
    # with open("temp/data" + airline['id'] + '.json', 'w') as file:
    #     json.dump(airline, file)
    # with open("temp1/data_%s.json"  % airline['id'], 'w') as file:
    #     # записывает объект в файл
        json.dump(airline, file)
#     # json.dumps()

file_name = 'temp/data_4.json'

with open(file_name, 'r') as file:
    json_new_data = json.load(file)


    print(type(json_new_data))
    print(json_new_data)

# with open("src/dist/new_file.json", "r") as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
#     json.load()
#     json.loads()