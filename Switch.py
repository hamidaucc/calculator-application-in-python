#!/usr/bin/env python3
__module__ = 'Switch'

class Switch:
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    
    __FORMAL_REPRESENTATION = "<Switch statement>"
    # formal representation of switch statement
    __DEFAULT_PARAMETER_NAME = 'default'
    # default parameter name, if passed
    def __init__(self,expr,**cases):
        # input of expression and creates a dictionary of the cases
        self.__set_expression(expr)
        self.__set_cases(cases)

    def __str__(self):
        # string representation
        return str(self.__switch())

    def __repr__(self):
        # formal representation
        return Switch.__FORMAL_REPRESENTATION 

    def __set_expression(self,expr):
        # setter method for expression(operation in use)
        self.__expr = expr

    def __set_cases(self,cases):
        # setter method for all possible cases
        # (multiplication, division, addition, subtraction, etc)
        self.__cases = cases

    def __get_cases(self):
        # returns all possible cases
        return self.__cases

    def __get_expr(self):
        # returns current expression in use
        return self.__expr

    def __switch(self):
        for case in self.__get_cases():
            # loops through all possible operations
            if case == self.__get_expr():
            # checks whether the case is the operation needed
            # (whether the case is equal to the expression)
                return self.__get_cases()[case]()
                # if true then returns the output of the function in the dictionary

    def get_value(self):
        # gets the value returned by the method __switch,
        # unless there is no switch value and there is a default set 
        # then it returns the default.
        value = self.__switch()
        if not self.__switch() and Switch.__DEFAULT_PARAMETER_NAME in self.__get_cases():
            value = self.__get_cases()[Switch.__DEFAULT_PARAMETER_NAME]()
        return value

    def run(self):
        # executes the switch statement.
        self.get_value()


