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
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            Output(' '*(len(rootDir)-len(dirName)) + path[len(rootDir):] +'\\', filename)
            CreateDirTree(path, filename)
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if not(os.path.isdir(path)):
            lenDir = len(rootDir)
            Output (' '*(len(rootDir)-len(dirName)+1) + path[lenDir+1:], filename)

dirName = input('Directory: ')
filename = input ("Имя файла для вывода результатов (пустое имя - вывод в консоль): ")
if len(filename) > 0:
    f = open(filename, 'w', encoding='utf-8')
    f.write('Содержимое папки ' + dirName + '\n')

print ('Содержимое папки ' + dirName)   
CreateDirTree(dirName, filename)
      
if len(filename) > 0:
    f.close()

input()
