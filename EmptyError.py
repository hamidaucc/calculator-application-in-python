#!/usr/bin/env python3
__module__="EmptyError"
import StackError as error
class EmptyError(error.StackError):
    
    # @author Hamid Abdul 
 
    
    # Error class that is raised when trying 
    # to access empty stack through indexing
    # The description of the error.
    __ERROR_CONTENT="Indexing through empty stack is not permitted"
    def __init__(self):
        super().__init__(EmptyError.__ERROR_CONTENT)
