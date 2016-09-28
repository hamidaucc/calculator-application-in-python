#!/usr/bin/env python3
__module__="Mul"
from basicOp import BasicOperation

class Mul(BasicOperation):
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    
    # takes in the first number and the second number as well as the base
    def __init__(self,number1,number2,base):
        # inherits the constructor from BasicOperation
        super().__init__(number1,number2,base)
        # calls the mul method
        self.mul()

    def mul(self):
        # sets the result of the multiplication using the set_result
        # method which was inherited from BasicOperations
        self.set_result(self.number1 * self.number2)


