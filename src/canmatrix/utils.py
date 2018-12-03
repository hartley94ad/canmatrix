import sys
import shlex
import csv

def my_split(inLine):
    if sys.version_info > (3, 0):  # is there a clean way to to it?
        return shlex.split(inLine.strip())
    else:
        tempArray = shlex.split(inLine.strip().encode('utf-8'))
        newArray = []
        for item in tempArray:
            newArray.append(item.decode('utf-8'))
        return newArray


def my_comma_splitter(string):
    temp = list(csv.reader([string], skipinitialspace = True))
    return temp[0]