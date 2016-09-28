#!/usr/bin/env python3
from basicOp import BasicOperation
__module__="Div"

class Div(BasicOperation):

    # @author Hamid Abdul
  
    # takes in the first number and the second number as well as the base
    def __init__(self,number1,number2,base):
        if number2 == 0:
            # if number is 0, rase Error.
            raise ZeroDivisionError
        # else:
        # inherits the constructor from BasicOperation
        super().__init__(number1,number2,base)
        # calls the div method
        self.div()

    def div(self):
        # sets the result of the division using 
        # the set_result method which was inherited from BasicOperations
        # rounds the division outcome, for better accuracy than integer division
        self.set_result(round(self.number2/self.number1))
