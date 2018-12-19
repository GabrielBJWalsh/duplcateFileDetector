# #!/usr/bin/env python
import hashlib, os, sys, pandas as pd

"""
finds the sup directory's of a given file leaves out files
"""


def directoryFinder(dir):
    files = os.listdir(dir)
    listOfDirrectorys = []

    for i in files:

        if os.path.isdir(os.path.join(dir, i)):
            listOfDirrectorys.append(i)
        else:
            continue

    return listOfDirrectorys


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
    #
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
creates a dictonary with the the file name as key and hash as value. uses recursion to dive into sub directory's 

"""


def hashDictonary(dir):
    files = os.listdir(dir)
    subDirectroys = directoryFinder(dir)
    dirDictonary = {}
    count =0
    for name in files:
        #print("loop number",count,dirDictonary)
        count+=1
        if name in subDirectroys:
            subDictornary=hashDictonary(os.path.join(dir,name))
           # print(subDictornary)
            for i in subDictornary:
               # print(i)
                #print(subDictornary[i])
                dirDictonary[i]=subDictornary[i]

        else:dirDictonary[name] = fileHasher(os.path.join(dir, name))
        #dirDictonary[os.path.join(dir, name)] = fileHasher(os.path.join(dir, name))

    return dirDictonary


"""
finds redundant files in a directory and creates a diconary of the files name/path and its copy 
"""


def dirCompair(dir):
    hash = hashDictonary(dir)
    result = {}
    for i in hash:
        for j in hash:
            if i == j:
                continue
            elif hash[i] == hash[j] and i not in result.values():
                result[i] = j

    return result


"""
puts a dictonary into a excel file
"""


def dictonaryToExcel(dictToBeExceled):
    df = pd.DataFrame

    df = df.from_dict(dictToBeExceled, "index")
    try:
        df.to_excel("duplicateFiles.xlsx")
    except Exception:
        print("please delete duplicates of duplcateFiles and try again")


#dir = input("please provide the file path")

dir = "C:/Users/gbw76/Desktop/git/duplcateFileDetector/testcompare"
mesPath="C:/Users/gbw76/Desktop/git/duplcateFileDetector/testcompare/mes"
dictonaryToExcel(dirCompair(dir))
#hashDictonary(dir)
#print(fileCompair(os.path.join(dir,"test2.txt"),os.path.join(mesPath,"test1.txt")))
