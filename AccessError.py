#!/usr/bin/env python3
__module__="StackError"
import StackError as error
class AccessError(error.StackError):
 
    # @author Hamid Abdul
   
    
    # Error class that is raised when invalid 
    # place in stack is being tried to access
    __ERROR_CONTENT="Access by indexes not permitted"
    # The description of the error.
    def __init__(self):
        super().__init__(AccessError.__ERROR_CONTENT)
