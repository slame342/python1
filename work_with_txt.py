#with open ("src./file.txt") если читать файлы вниз по ветке,OPEN оператор позв откр определенный обьект.
#readme.txt file должен находиться в этой директ.
#with open ("../src./file.txt") as f: читать файл вверх по ветке
#здесь код будет закрыт
    #здесь код будет исполняться
#with оператор позваляет сразу закрыть цикл
#with open ("src./file.txt") as f:
#f любая переменная ,нужна чтобы использовать ее далее будущем alias/имя,псевдоним
#with open("C:/Users/User/Documents/GitHub/python1/src/file.txt") as file:#выбирает фаил по абсолютному пути
#with open("src/file.txt") as file: #выбирает фаил в папке текущей дериктории
with open('file.txt') as file:
    #text = file.readline()#читает выбранную строку
    #print(text)

    #text1=[начало:конец:шаг]
    text = file.readlines()#читает все строки и выдает массив
    print(text)

    #text1 = text[начало:конец:шаг]

    text = 'Pellentesque'
    text1 = text[3::1]  #обрезает строку в обычной последовательности от 3го символа и до конца
    print(text1)
    text = 'Pellentesque'
    text1 = text[3:10:-1]  #обрезает строкув обычной послед-ти от третьего символа и до 10символа

    text = 'Pellentesque'
    text1 = text[::2]   # обрезает строку в обратной послед-ти
    #print(text1)

    var_list = ["Almaty", "Nur-Sultan", "Taraz", "Ekibastuz","Almaty", "Nur-Sultan", "Taraz", "Ekibastuz"]
    var_list1 = var_list[0:8:5]
    print(var_list1)

    
    #for line in text



    #text = file.write()
    #text = file.read()
