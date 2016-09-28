#!/usr/bin/env python3
__module__="StackError"
import StackError as error
class AccessError(error.StackError):
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    
    # Error class that is raised when invalid 
    # place in stack is being tried to access
    __ERROR_CONTENT="Access by indexes not permitted"
    # The description of the error.
    def __init__(self):
        super().__init__(AccessError.__ERROR_CONTENT)
