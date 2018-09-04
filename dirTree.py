# Построение дерева каталогов и файлов. Корневой каталог запрашивается.
import os 
def CreateDirTree(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            print(path)
            CreateDirTree(path)
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if not(os.path.isdir(path)):
            lenDir = len(rootDir)
            print (' '*lenDir + path[lenDir:])

dirName = input('Directory: ')
CreateDirTree(dirName)

      
