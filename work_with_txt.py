# with open("C:/Project/projects/python1/src/file.txt") as file: # alias (псевдоним). абсолютный путь
# with open("src/file.txt") as file: # относительный путь к файлу в папке текущей директории
# with open("file.txt") as file:
# with open("src/dist/file.txt", "r" , encoding='utf-8') as file: # относительный путь к файлу в текущей папке
    # text = file.readline() # читает выбранную строку
    # print(text)
    # text = file.readlines() # читает все строки, выдает массив
    # print(text)

    # new_list = []
    # for line in text:
    #     if len(line) > 1:
    #         new_list.append(line[0:-1:1])
    #     #     pass
    #     #     print(line[0:-1:1])
    # print(new_list)

print("\\\nHello\fWorld!\t") #спецсимволы в строках

# text = "Pellentasque"
# text1 = text[3::1] # обрезает строку в обычной последовательности от 3 строки и до конца
#
# text = "Pellentasque"
# text1 = text[3:10:1]  # обрезает строку от 3 символа до 10 символа
#
# text = "Pellentasque"
# text1 = text[::-1]  # обрезает строку в обратной последовательности
#
# # print(text1)
#
# city_list = ["Almaty", "Astana", "Taraz", "Shymkent"]
# print(city_list[2:0:-1])


    # for line in text:
    #
    #     print(line)
    # text = file.write()
    # text = file.read()

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [(fruit + "#1") for fruit in fruits if "e" in fruit]
# print(newlist)


with open("src/dist/new_file.txt", "a") as file:
    var_list = ["Almaty", "Astana", "Taraz", "Shymkent","Almaty", "Astana", "Taraz", "Shymkent"]
    # for city in var_list:
    #     file.write(f"{city}\n") # пишет в строки отдельно
    # file.writelines([f"{city}\n" for city in var_list])
    new_list = []
    for city in var_list:
        newlist.append(f"{city}\n")
    for city in var_list:
        file.write(f"{city}\n") # пишет в строки отдельно
    file.writelines(newlist)

    new_list = []
    for city in var_list:
        new_city =city + "\n"
        newlist.append(new_city)
    file.writelines(new_list)


text ="ShymkentShymkentShymkent"
new_text = ""
index = 0
for char in text:
    index = index + 1
    new = index % 2
    new_char = ""
    if new == 0:
        new_char = f"1{char} "
        new_text += new_char
print(new_text)

new_list = [f"1{char} " for char in text if text.index(char) % 2 != 0]
print("".join(new_list))