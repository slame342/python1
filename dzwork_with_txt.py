import os

os.mkdir("folder/folder1")

with open("folder/file.txt", "r") as file:
    text = file.readlines()
    # print(text)
    for word in text:
        if len(word) > 1:
            print(word)

    # var_list = ["Almaty", "Astana", "Taraz", "Shymkent","Almaty", "Astana", "Taraz", "Shymkent"]
    # for city in var_list:
    #     file.write(f"{city}\n") # пишет в строки отдельно
    # file.writelines([f"{city}\n" for city in var_list])
    # new_list = []
    # for city in var_list:
    #     new_list.append(f"{city}\n")
    # for city in var_list:
    #     file.write(f"{city}\n") # пишет в строки отдельно
    # file.writelines(new_list)
    #
    # new_list = []
    # for city in var_list:
    #     new_city =city + "\n"
    #     new_list.append(new_city)
    # file.writelines(new_list)