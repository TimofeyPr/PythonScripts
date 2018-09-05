import os
list1 = os.listdir()
filename = input('Имя файла для вывода результатов: ')
f = open(filename, 'w', encoding='utf-8')
for n in range (0, len(list1)):
        if os.path.isdir(list1[n]):
                f.write ('+- ' + list1[n] + '\n')
        else:
                f.write ('-- ' + list1[n] + '\n')
f.close()
