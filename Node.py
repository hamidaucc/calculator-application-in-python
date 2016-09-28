#!/usr/bin/env python3
__module__="Node"
class Node:
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    # formal representation of node object
    __FORMAL_REPRESENTATION = "<Stack Node object>"
    def __init__(self,value,prev):
        self.set_value(value)
        self.__set_prev(prev)

    def set_value(self,value):
        # setter for value to keep encapsulation
        self.__value=value

    def __set_prev(self,value):
        # setter for prev to keep encapuslation
        self.__prev=value
    
    def __str__(self):
        # string representation of node
        return "%s"%str(self.get_value())

    def __repr__(self):
        # formal representation of node
        return Node.__FORMAL_REPRESENTATION
    
    # getter methods
    def get_value(self):
        return self.__value
   
    def get_prev(self):
        return self.__prev
