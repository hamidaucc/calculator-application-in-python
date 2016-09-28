#!/usr/bin/env python3
__module__ = 'basicOP'
from baseConv import BaseConversion
class BasicOperation:
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    
    # the constructor takes in the first number, the second number and the base
    def __init__(self,number1,number2,base):
        # initialises the base variable
        self.base=base
        # initialises number1 after its converted with the base of that object
        self.number1 = BaseConversion(number1,base).get_value()
        # initises number2 after its converted with the base of that object
        self.number2 = BaseConversion(number2,base).get_value()

    def set_result(self,result):
        # allows result variable to be set with encapsulation
        self.__result = result

    def result(self):
        # returns the resulting value from the operation in its base
        return BaseConversion(self.__result,self.base,True).get_value()

    @property
    def base(self):
        # Note this is a getter for base
        return self.__base

    @base.setter
    def base(self,base):
        # Note this is a setter for base
        self.__base = base

    @property
    def number1(self):
        # Note this is a getter for number1
        return self.__number1
    
    @number1.setter
    def number1(self,number1):
        # Note this is a setter for number1
        self.__number1 = number1


    @property
    def number2(self):
        # Note this is a getter for number1
        return self.__number2
    
    @number2.setter
    def number2(self,number2):
        # Note this is a setter for number2
        self.__number2 = number2


