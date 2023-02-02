def generateInvertedIndexDict(dataFromDoc: list[str]) :
    """
    generates the inverted index dict

    parameters:
    dataFromDoc (list[str]) : list of strings read from docs

    return:
    dict of term to set of docIDs
    """

    d=dict()

    termsListFromDoc = [s.split() for s in dataFromDoc]

    for docId, termList in enumerate(termsListFromDoc):
        for term in termList:
            if term not in d:
                d[term]={docId}
            else:
                d[term].add(docId)

    return d