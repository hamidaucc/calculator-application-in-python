#!/usr/bin/env python3
__module__="Add"
from basicOp import BasicOperation

class Add(BasicOperation):
    # @author Hamid Abdul (ID 114734769)

    
    # takes in the first number and the second number as well as the base
    def __init__(self,number1,number2,base):
        # inherits the constructor from BasicOperation
        super().__init__(number1,number2,base)
        # calls the add method
        self.add()

    def add(self):
        # sets the result of the addition using the set_result method
        # which was inherited from BasicOperations
        self.set_result(self.number1 + self.number2)
