class BooleanModel():
    """
    This class implements the boolean model for information retrieval.
    
    Attributes:
        docIds (set): set of all document ids
        
    Methods:
        andOperation(left_operand, right_operand): returns the intersection of two sets
        orOperation(left_operand, right_operand): returns the union of two sets
        notOperation(operand): returns the difference of two sets
    """
    def __init__(self,docIdToDocName):
        self.docIds = set(docIdToDocName.keys())
    
    @staticmethod
    def andOperation(left_operand, right_operand):
        return left_operand.intersection(right_operand)
    
    @staticmethod
    def orOperation(left_operand, right_operand):
        return left_operand.union(right_operand)
    
    @staticmethod
    def notOperation(self, operand):
        return self.docIds.difference(operand)