#!/usr/bin/env python3
__module__="Operation"
from Stack import Stack
from Switch import Switch
from ErrorAlert import DisplayError
from Add import Add
from Mul import Mul
from Sub import Sub
from Div import Div

class Operation:
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    
    # value of unary subtraction
    __UNARY_SUBTRACTION = -1
    # message if there is no operations pending
    __NO_OPERATION = "No operation pending"
    # translation of signs into function names
    __SIGN_MEANINGS = {"plus":"+","star":"*","minus":"-","slash":"/","unary_minus":"=-",None:"No operations pending"}
    # value at which stack is empty
    __EMPTY_STACK = 1
    # division error message
    __DIVISION_ERROR = "Division by 0 is not allowed"
    
    def __init__(self,base):
        self.__set_up_buffer(Stack())
        self.set_base(base)

    def set_base(self,base):
        # base setter
        self.__base = base

    def __get_base(self):
        # base getter
        return self.__base        

    def __set_up_buffer(self,stack):
        # buffer setter (create a stack for operations)
        self.__buffer=stack

    def __access_buffer(self):
        # access the stack
        return self.__buffer

    def clear_buffer(self):
        # clear the stack
        for buff in self.__access_buffer():
            pass

    def push_buffer(self,number):
        # push new value to the stack
        if len(self.__access_buffer()) == Operation.__EMPTY_STACK and not self.__access_buffer().peek():
           self.__access_buffer()[len(self.__access_buffer())] = number
        else:
            self.__access_buffer().push(number)

    def __add(self):
        # calculates the result of the addition and returns it
        number1 = self.__access_buffer().pop()
        number2 = self.__access_buffer().pop()
        result = Add(number1,number2,self.__get_base())
        return result.result()
    
    def __mul(self):
        # calculates the result of the multiplication and returns it
        number1 = self.__access_buffer().pop()
        number2 = self.__access_buffer().pop()
        result = Mul(number1,number2,self.__get_base())
        return result.result() 
    
    def __sub(self):
        # calculates the result of the subtraction and returns it
        number1 = self.__access_buffer().pop()
        number2 = self.__access_buffer().pop()
        result = Sub(number1,number2,self.__get_base())
        return result.result()

    def __div(self):
        # calculates the result of the division and returns it
        number1 = self.__access_buffer().pop()
        number2 = self.__access_buffer().pop()
        # if there is a zerodivision error, display notification, that
        # division by zero is not allowed
        try:
            result = Div(number1,number2,self.__get_base()).result()
        except ZeroDivisionError:
            DisplayError(Operation.__DIVISION_ERROR)
            result = ""
        return result 

    def __flip(self):
        # applies unary subtraction
        number = int(self.__access_buffer().pop()) * Operation.__UNARY_SUBTRACTION
        return number
    
    def apply(self):
        # applies the operations in the switch object which is constructed
        val = self.__access_buffer().pop()
        switch = Switch(val,
                        plus=self.__add,
                        star=self.__mul,
                        minus=self.__sub,
                        slash=self.__div,
                        unary_minus=self.__flip)
        return switch

    def view_buffer(self):
        # preview buffer (stack)
        signs = Operation.__SIGN_MEANINGS
        buffer = [sign if sign not in signs else signs[sign] for sign in self.__access_buffer().peak_through()]
        return buffer if buffer else Operation.__NO_OPERATION

