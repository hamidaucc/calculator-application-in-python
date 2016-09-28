#!/usr/bin/env python3
__module__= "SetError"
from StackError import StackError
class SetError(StackError):
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    
    # Error class that is raised when invalid 
    # place in stack is being tried to set a value
    __ERROR_DESCRIPTION = "Access by indexes not permitted"
    # The description of the error.
    def __init__(self):
        super().__init__(SetError.__ERROR_DESCRIPTION)
