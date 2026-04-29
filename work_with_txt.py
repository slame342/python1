# with open("C:/Project/projects/python1/src/file.txt") as file: # alias (псевдоним). абсолютный путь
# with open("src/file.txt") as file: # относительный путь к файлу в папке текущей директории
with open("file.txt") as file: # относительный путь к файлу в текущей папке
    # text = file.readline() # читает выбранную строку
    # print(text)
    text = file.readlines() # читает все строки, выдает массив
    print(text)

    new_list = []
    for line in text:
        if len(line) > 1:
            new_list.append(line[0:-1:1])
        #     pass
        #     print(line[0:-1:1])
    print(new_list)

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

