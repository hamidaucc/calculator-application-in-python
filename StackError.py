#!/usr/bin/env python3
__module__ = "StackError"
class StackError(Exception):
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    
    # base clas for all the stack errors
    __DEFAULT_DESCRIPTION="Uknown error occoured"
    # sets the default error message as ''Unknown error occoured''
    def __init__(self,value=__DEFAULT_DESCRIPTION):
        self.value=value

    @property
    def value(self):
        # returns the value
        return self.__value

    @value.setter
    def value(self,value):
        # setters to keep encapsulation
        self.__value = value

    def __str__(self):
        # str representation of error. This is required for error to be 
        # displayed.
        return repr(self.value)
