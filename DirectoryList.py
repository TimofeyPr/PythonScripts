import os
DirName = input("Путь к директории: ")
list1 = os.listdir(DirName)
filename = input('Имя файла для вывода результатов: ')
f = open(filename, 'w', encoding='utf-8')
for n in list1:
        path = os.path.join(DirName, n)
        if os.path.isdir(path):
                f.write ('+- ' + n + '\n')
for n in list1:
        path = os.path.join(DirName, n)
        if not(os.path.isdir(path)):
                f.write ( n + '\n')
f.close()
