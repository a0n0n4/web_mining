"""
main module for queries using Boolean retrieval model which handles everything
"""
import sys, pickle

from queries_boolean_retrieval_model.postfix_query_queue import getPostfixQueryQueue
from queries_boolean_retrieval_model.evaluate_postfix_query import evaluatePostfixQuery

saveFileName, queryFileName = str, str

# get the directory and save file name from command line arguments
for i, arg in zip(*[iter(sys.argv[1:])]*2):
    if (i=="-s"):
        saveFileName = arg
    elif (i=="-q"):
        queryFileName = arg

# read the inverted index dictionary and docIDToDocName from a file
with open(saveFileName, 'rb') as handle:
    invertedIndexDict, docIdToDocName = pickle.load(handle)

# read the querys from a file and storing in list
queryList = open(queryFileName).read().replace("(", "( ").replace(")", " )").split("\n")

for query in queryList:
    # split the query into tokens by space
    tokenizedQuery = query.split(" ")
    # get the postfix query queue
    q=getPostfixQueryQueue(tokenizedQuery)
    # evaluate the postfix query
    res=evaluatePostfixQuery(q, docIdToDocName, invertedIndexDict)
    # convert docIDs to docNames
    res=[docIdToDocName[docId] for docId in res]
    print("\n",query,":",res,"\n")
    

