# #!/usr/bin/env python
import hashlib, os, sys,pandas as pd



"""creates a md5 hash of a file"""


def fileHasher(file: str):
    hasher = hashlib.md5()

    with open(file, "rb")as openFile:
        content = openFile.read()
        hasher.update(content)

    hx = hasher.hexdigest()
    return hx


"""compairs two files to see if they are the same"""


def fileCompair(file1, file2):
    if fileHasher(file1) == fileHasher(file2):
        return True
    else:
        return False


"""
puts redundant files in a dictionary with its copy 
"""


def dirChecker(dir):
    files = os.listdir(dir)
    redundantFiles = {}
    for name in files:
        for j in files:
            if (name == j):
                continue
            elif fileCompair(os.path.join(dir, name), os.path.join(dir, j)):
                redundantFiles[name] = j

    return redundantFiles


"""
takes a dictionary and makes an excel file out of it
"""


def dictionaryToExel(dictonary):
    pass


"""creates a dictonary with the the file name as key and hash as value"""


def hashDictonary(dir):
    files = os.listdir(dir)
    dirDictonary = {}
    for name in files:
        dirDictonary[name] = fileHasher(os.path.join(dir, name))

    return dirDictonary


"""
finds redundant files in a directory and creates a diconary of the files name/path and its copy 
"""


def dirCompair(dir):
    hash = hashDictonary(dir)
    result ={}
    for i in hash:
        for j in hash:
            if i==j:
                continue
            elif hash[i]==hash[j] and i not in result.values():
                result[i]=j


    return result
"""
puts a dictonary into a excel file
"""
def dictonaryToExcel(result):
    df = pd.DataFrame
    reFrame = pd.DataFrame()
    df = df.from_dict(result, "index")

    print(df)
    try:
        df.to_excel("duplicateFiles.xlsx")
    except Exception:
        print("please delete duplicates of duplcateFiles and try again")


dir = "C:/Users/gbw76/Desktop/git/faceStuffForMOM/testcompare"
# print(fileCompair("test1.txt","test2.txt"))
# file1 = "C:/Users/gbw76/Desktop/git/faceStuffForMOM/me.jpg"
# file2 = "C:/Users/gbw76/Desktop/git/faceStuffForMOM/notME.jpg"
# print("HASH DICTIONARY")
#print(hashDictonary(dir))
# dir ="C:/Users/gbw76/Desktop/git/faceStuffForMOM/"
# print("REDUNDANT DICTIONARY")
# print("derChecker test",dirChecker(dir))
# print(fileCompair("me.jpg","notME.jpg"))
# print(fileHasher(file1))
#print(dirCompair(dir))


dictonaryToExcel(dirCompair(dir))
