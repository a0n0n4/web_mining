"""
main module for term_document_incidence_matrix which handles everything
"""
import sys, pickle
import pandas as pd

saveFileName = str

# get the directory and save file name from command line arguments
for i, arg in zip(*[iter(sys.argv[1:])]*2):
    if (i=="-s"):
        saveFileName = arg

# read the inverted index dictionary and docIDToDocName from a file
with open(arg, 'rb') as handle:
    invertedIndexDict, docIdToDocName = pickle.load(handle)

# create a term-document incidence matrix with pandas
df=pd.DataFrame(index=invertedIndexDict.keys(),columns=range(len(docIdToDocName)),data=0)

# fill the matrix with 1s
for term in invertedIndexDict.keys():
    for docId in invertedIndexDict[term]:
        df.loc[term,docId]=1
        
df.columns=docIdToDocName.values()

print("\n",df,"\n")
