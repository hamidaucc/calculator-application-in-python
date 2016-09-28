#!/usr/bin/env python3
__module__="PopUp"
from tkinter import *
from CGG import *
from random import randint
from re import sub

def _format_text(text):
    # function for text formattinh, if it comes in as
    # list turned into a string
    # note that _ at the start means, do not copy than function when
    # "from module import *" is used.
    text = sub("\[|\]|\'|\'","",r'%s'%text)
    text = text.split(",")
    final_text = " "
    for word in text:
        final_text += "%s\n"%word
    return final_text
            
class PopUp(Text):
    # @author Herakliusz Lipiec (ID 114345041)
    # @author Hamid Abdul (ID 114734769)
    # @author Stephen Hannon(ID 113425638)
    # create a popup window
    # close button title
    __BUTTON_TITLE = "Close"
    # width of window
    __WIDTH = 40
    # height of window
    __HEIGHT = 15
    # color gamma for the window
    __GAMMA_BASE = 15
    # color start index for colors
    __COLOR_START = 0
    # color end index for colors
    __COLOR_STOP = 4
    # text color in window
    __FG_COLOR = "#000000"
    def __init__(self,text,title,color=get_color(__GAMMA_BASE),width=__WIDTH,height=__HEIGHT):
        text = _format_text(text)
        # initialise the pop_up window
        master = Tk()
        master.title(title)
        # make a text widget
        super().__init__(master,width=width,height=height,wrap=WORD)
        self.insert(INSERT,text)
        self.config(state=DISABLED)
        self.__set_scroll(master)
        if color:
            # if color exists, set up the colors
            bgindex=randint(PopUp.__COLOR_START,PopUp.__COLOR_STOP)
            self.config(bg=color[bgindex],fg=PopUp.__FG_COLOR)
        # make a button
        button = Button(master,text=PopUp.__BUTTON_TITLE,command=self.master.destroy)
        self.pack(side=TOP)
        button.pack(side=BOTTOM)
        mainloop()

    def __set_scroll(self,master):
        # initialise the scroll bar
        self.__scroll = Scrollbar(master,command=self.yview)
        self.__scroll.pack(side=RIGHT,fill=Y)
        self.config(yscrollcommand=self.__scroll.set)
