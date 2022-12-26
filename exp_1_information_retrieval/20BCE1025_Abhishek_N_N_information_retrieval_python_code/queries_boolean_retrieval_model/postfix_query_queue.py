from queue import Queue


def getPostfixQueryQueue(tokenizedQuery):
    """
    Returns a queue that will be used to store the postfix query

    Parameters:
        tokenizedQuery (list): list of tokens in the query

    Returns:
        Queue: queue that will be used to store the postfix query
                queue ements are tuples of the form (token, isOperator)
    """
    q = Queue()

    operators = {"(", ")", "OR", "AND", "NOT"}
    priority = {"OR": 0, "AND": 1, "NOT": 2}

    stack = []

    for token in tokenizedQuery:
        if token not in operators:
            q.put((token, 0))
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                q.put((stack.pop(), 1))
            stack.pop()
        else:
            while stack and stack[-1] != "(" and priority[token] <= priority[stack[-1]]:
                q.put((stack.pop(), 1))
            stack.append(token)

    while stack:
        q.put((stack.pop(), 1))

    return q
