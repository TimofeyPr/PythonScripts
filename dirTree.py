# Построение дерева каталогов и файлов. Корневой каталог запрашивается.
import os

dirName  = ""

def Output(str1, filename):
    if len(filename) > 0:
        f.write(str1 + '\n')
    else:
        print (str1)
    
def CreateDirTree(rootDir, filename):
    for lists in os.listdir(rootDir):
        try:      
            path = os.path.join(rootDir, lists)
            if os.path.isdir(path):
                Output(' '*(len(rootDir)-len(dirName)) + path[len(rootDir):] +'\\', filename)
                CreateDirTree(path, filename)
        except:
            Output(' '*(len(rootDir)-len(dirName)) + path[len(rootDir):] +'\\ - нет доступа', filename)
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if not(os.path.isdir(path)):
            lenDir = len(rootDir)
            if len(rootDir)-len(dirName) > 0:
                Output (' '*(len(rootDir)-len(dirName)+1) + path[lenDir+1:], filename)
            else:
                Output (path[lenDir:], filename)

dirName = input('Введите путь к папке: ')
filename = input ("Имя файла для вывода результатов (пустое имя - вывод в консоль): ")
if len(filename) > 0:
    f = open(filename, 'w', encoding='utf-8')
    f.write('Содержимое папки ' + dirName + '\n')
else:
    print ('Содержимое папки ' + dirName)   

CreateDirTree(dirName, filename)
      
if len(filename) > 0:
    f.close()

input()
