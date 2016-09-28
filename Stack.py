#!/usr/bin/env python3
__module__="Stack"
from Node import Node
from AccessError import AccessError
from SetError import SetError
from EmptyError import EmptyError
class Stack:
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    __FORMAL_REPRESENTATION = "<Stack object; length:%i>"
    def __init__(self,initial_value=None):
        # initialises the head, tail and length of the stack
        self.__set_head(Node(None,None))
        self.__set_last(Node(initial_value,self.__head))
        self.length = 1

    def __len__(self):
        # returns the length of the stack
        return self.length

    def __getitem__(self,index):
        # pops the last item on the stack unless the stack is empty
        # or index value is not a valid last position of stack,
        # then it will call the error message
        if self.isempty():
            raise EmptyError
        elif index==len(self):
            return self.pop()
        raise AccessError

    def __setitem__(self,index,value):
        # change the value of last element on the stack, using index values
        if index==len(self):
            self.get_last().set_value(value)
        else:
            raise SetError

    def __iter__(self):
        # make stack iterable
        return self

    def __next__(self):
        # pop each value on stack
        if self.isempty():
            raise StopIteration
        else:
            return self.pop()
    
    def __str__(self):
        # string representation of stack
        output_string = [element for element in self.peak_through()]
        return str(output_string)

    def peak_through(self):
        # look through the stack, to see what values are in it
        node = self.get_last()
        while node != self.__get_head():
            yield node.get_value()
            node = node.get_prev()

    def __repr__(self):
        # formal representation of stack
        return Stack.__FORMAL_REPRESENTATION%len(self)

    def __iadd__(self,other):
        # push values onto a stack using +=
        self.push(other)
        return self

    def isempty(self):
        # checks to see if the stack is empty
        return self.__last == self.__head
    
    def push(self,item):
        # adds node to the top of the stack and increments the stack
        self.__prev = self.__last
        self.__last = Node(item,self.__prev)
        self.length += 1

    def pop(self):
        # returns the top node's value, deletes it and
        # decrements the length of the stack
        node=None
        if self.__last != self.__head:
            node=self.__last
            self.__last=self.__last.get_prev()
            self.length-=1
        return node.get_value() if node else None

    def peek(self):
        # returns the value of the node thats at the bottom of the stack.
        return self.__last.get_value()

    @property
    def length(self):
        # returns the length of the stack
        return self.__length

    @length.setter
    def length(self,value):
        # setters to keep encapsulation
        self.__length = value

    def __set_head(self,node):
        # setter for head
        self.__head=node

    def __set_last(self,node):
        # setter for the top element in stack
        self.__last=node

    def __set_prev(self,node):
        # setter for prev node
        self.__prev = node

    def __get_prev(self):
        # getter for prev node
        return self.__prev

    def __get_head(self):
        # getter for head
        return self.__head

    def get_last(self):
        return self.__last
