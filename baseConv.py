#!/usr/bin/env python3
__module__ = 'BaseConversion'
class BaseConversion:
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    _FORMAL_REPRESENTATION = "<Decimal Integer Converter>"
    # Formal representation of the BaseConversion Object
    def __init__(self,number,base,reverse=False):
        # Take in a number, a base and convert that number to a base 10.
        # If reverse is set a number is converted from base 10 to that number.
        self.__set_number(number)
        self.__set_base(base)
        if reverse:
            self.int_to_base()
        else:
            self.convert()

    def __str__(self):
        # String representation of BaseCovnersion object.
        return str(self.get_value())

    def __repr__(self):
        # Formal representation of BaseConversion Object
        return BaseConversion._FORMAL_REPRESENTATION

    def __int__(self):
        # Int value of BaseConversion object
        return self.get_value()

    def __set_number(self,number):
        # Note that this is a setter for number, it converts given number
        # to a string, in order to prepare the data for conversion.
        self.__number = str(number)

    def __set_base(self,base):
        # This is a setter for a base
        self.__base = base

    def __get_base(self):
        # Note. This is a getter for a base
        return self.__base

    def __get_number(self):
        # A getter for number
        return self.__number

    def __set_value(self,value):
        # A setter for value
        self.__value = value

    def get_value(self):
        # A getter for value
        return self.__value

    def convert(self):
        # This is a function that converts numbers from any basew between 2-36
        # to base 10.
        self.__set_value(int(self.__get_number(),self.__get_base()))
        return self.get_value()

    def __convert_base(self):
        # This is a main part of reverse conversion engine.
        # It yields (generates) a sequence that when reversed
        # represents a given number in given base.
        num = int(self.__get_number())
        negative = False
        if num == 0:
            yield 0
        else:
            while num:
                if num < 0:
                    num *= -1
                    negative = True
                yield (num%self.__get_base())
                num //= self.__get_base()
        if negative:
            yield "-"

    def int_to_base(self):
        # This calls __convert_base, and reverses a sequence generated 
        # by __convert_base, in order to return converted number.
        str_repr = ""
        for number in self.__convert_base():
            str_repr += str(number)
        self.__set_value(str_repr[::-1])
