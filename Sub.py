#!/usr/bin/env python3
from basicOp import BasicOperation
__module__="Sub"
class Sub(BasicOperation):
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    
    # takes in the first number and the second number as well as the base
    def __init__(self,number1,number2,base):
        # runs the constructor of BasicOperation
        super().__init__(number1,number2,base)
        # calls the sub method
        self.sub()

    def sub(self):
            # sets the result of the subtraction using the set_result method which was inherited from BasicOperations
        self.set_result(self.number2 - self.number1 )


