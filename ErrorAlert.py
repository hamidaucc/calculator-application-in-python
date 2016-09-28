#!/usr/bin/env python3
from tkinter import messagebox as mb
__module__="ErrorAlert"

class DisplayError:
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    
    # default title
    __TITLE = 'Error'
    def __init__(self,error,title=__TITLE):
        # initialise messagebox
        self.__set_error(error)
        self.__set_title(title)
        self.__display_error()
        
    def __set_error(self,error):
        # this is a setter for error
        self.__error = error
        
    def __get_error(self):
        # this is a getter for error
        return self.__error
    
    def __set_title(self,title):
        # this is a setter for title
        self.__title = title
        
    def __get_title(self):
        # this is a getter for title
        return self.__title
    
    def __display_error(self):
        # display error alert
        mb.showerror(self.__get_title(),self.__get_error())
            
