"""
file module for handling all file operations
"""
from os import listdir
from os.path import isfile, join


def getDataFromDocs(dir):
    """
    gets strings from docs 

    parameters:

    dir (str) : directroy which contains all files

    return: 
    list of str read from docs in the directory given by user

    """
    return [open(join(dir, f)).read() for f in sorted(listdir(dir)) if isfile(join(dir, f))]

def getDocIDToDocNameMap(dir):
    """
    gets the map of docID to docName

    parameters:

    dir (str) : directroy which contains all files

    return: 
    dict of docID to docName of docs in the directory given by user

    """
    return {i:x for i, x in enumerate([f for f in sorted(listdir(dir)) if isfile(join(dir, f))])}
