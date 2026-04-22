# with open("C:/Project/projects/python1/src/file.txt") as file: # alias (псевдоним)
# with open("src/file.txt") as file: # alias (псевдоним)
with open("file.txt") as file: # alias (псевдоним)
    text = file.readline() # читает выбранную строку
    print(text)
    # text = file.readlines()
    # text = file.write()
    # text = file.read()

