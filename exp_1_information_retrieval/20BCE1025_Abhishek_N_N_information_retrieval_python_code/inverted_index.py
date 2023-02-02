"""
main module for inverted_index which handles everything
"""
from inverted_index_helpers import file_handler, inverted_index_dict_generator
import sys, pickle
import pandas as pd

dir, saveFileName = str, str

# get the directory and save file name from command line arguments
for i, arg in zip(*[iter(sys.argv[1:])]*2):
    if (i=="-d"):
        dir = arg
    elif (i=="-s"):
        saveFileName = arg


dataFromDoc = file_handler.getDataFromDocs(dir)
docIdToDocName = file_handler.getDocIDToDocNameMap(dir)

invertedIndexDict = inverted_index_dict_generator.generateInvertedIndexDict(dataFromDoc)

print("\n",pd.DataFrame(invertedIndexDict.items(), columns=["Term", "DocId"]),"\n")

# save the inverted index dictionary and docIDToDocName to a file
with open(saveFileName, 'wb') as handle:
    pickle.dump([invertedIndexDict, docIdToDocName] , handle, protocol=pickle.HIGHEST_PROTOCOL)
