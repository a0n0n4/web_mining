from .boolean_model import BooleanModel

def evaluatePostfixQuery(queue, docIdToDocName, invertedIndexDict):
    """Evaluate a postfix query on the given index.
    
    Args:
        query (list): A list of tokens representing a postfix query.
        index (dict): The index to evaluate the query on.
    
    Returns:
        list: A list of document IDs matching the query.
    """
    bm = BooleanModel(docIdToDocName)
    stack = []
    while not queue.empty():
        token, isOperator = queue.get()
        if isOperator:
            if token == "NOT":
                operand = stack.pop()
                stack.append(bm.notOperation(bm,operand))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if token == "AND":
                    stack.append(bm.andOperation(left_operand, right_operand))
                elif token == "OR":
                    stack.append(bm.orOperation(left_operand, right_operand))
        else:
            stack.append(invertedIndexDict[token])
    
    return stack.pop()
