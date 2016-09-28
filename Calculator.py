#!/usr/bin/env python3
#author Hamid Abdul
__module__="Calculator"
from tkinter import *
from IOPanel import *
from Digit import *
from GridPositioner import *
from Operation import Operation
from CGG import *
from PopUp import *

# Class for a GUI-based calculator.
class Calculator( Tk ) :
  
    # Width of @IOPanel@ in pixels.
    __IO_PANEL_WIDTH = 200
    # Height of @IOPanel@ in pixels.
    __IO_PANEL_HEIGHT = 50
    # Row number of @IOPanel@ in grid layout of the calculator.
    __IO_PANEL_ROW = 0
    # Column number of @IOPanel@ in grid layout of the calculator.
    __IO_PANEL_COL = 0
    # Span of @IOPanel@ in widgets in the grid layout of the calculator.
    __IO_PANEL_SPAN = 3

    # Title of display stack, in menu operations
    __DISPLAY_STACK_TITLE = "Display pending operations"

    # The number base of the calculator.
    __BASE = 10

    # The title of this calculator's window.
    __TITLE = "Calculator"
    
    # A constant for minimum base supported by calculator
    __MIN_BASE = 2
    # A constant value for maximium base supported by calculator
    __MAX_BASE = 10

    # Row number of the first digit row in grid layout of the calculator.
    __DIGIT_ROW = 1
    # Column number of the first digit row in grid layout of the calculator.
    __DIGIT_COL = 0
    # Number of digit buttons per row in grid layout of the calculator.
    __DIGITS_PER_ROW = 3

    # Text on the clear button.
    __CLEAR_TITLE = "C"
    # Text on the push button.
    __PUSH_TITLE  = "P"
    # Text on Apply button
    __APPLY_TITLE  = "A"
    # Place of file with help contents
    __HELP_FILE = "help.txt"
    # Read mode of help file
    __HELP_READ_MODE = "r"
    # Help text if help file cannot be opened for reading.
    __BACKUP_HELP = """This calculator works by entering your 1st number, and pressing P (push) on a keypad, then repeat this for 2nd number,
    choose the operation and press A (apply).
    Meaning of characters:
    \t- C - Clear input
    \t- A - Apply operation
    \t- P - push number onto buffer
    \t- -x - unary minus
    \t- + - addition
    \t- // - rounded division
    \t- - -subtraction
    \t- * - multuplication
    To change a base, please go to base menu and choose your base.
    """
    # Title of help window
    __HELP_WINDOW_TITLE = "Help"
    # Contents of about popup window
    __ABOUT_TEXT = "Assigment 4: GUI Calculator in Tkinter v1.0\nmade by:\n\t-Herakliusz Lipiec\n\t-Hamid Abdul\n\t-Stephen Hannon"
    # Title of about window
    __ABOUT_WINDOW_TITLE = "About"
    # Title of base menu
    __BASE_MENU_TITLE="Base"
    # Title of operations menu
    __OPERATIONS_MENU_TITLE = "Operations"
    # Title of Help entry in help menu
    __HELP_TITLE = "Help"
    # Title of About entry in help menu
    __ABOUT_TITLE = "About"
    # Title of preview stack entry in operations menu
    __PREVIEW_TITLE = "Preview pending operations"
    # Title of clear buffer in operations menu
    __CLEAR_BUFFER_TITLE = "Clear pending operations"
    
    # operational value of ADD button"
    __ADD_VALUE = "plus"
    # ADD button title
    __ADD_TITLE = "+"
    # operational value of UNARY SUBTRACTION button"
    __UNARY_VALUE = "unary_minus"
    # UNARY SUBTRACTION button title
    __UNARY_TITLE = "-x"
    # operational value of DIVISION button"
    __DIV_VALUE = "slash"
    # DIVISION button title
    __DIV_TITLE = "//"
    # operational value of SUBTRACTION button"
    __SUB_VALUE = "minus"
    # SUBTRACTION button title
    __SUB_TITLE = "-"
    # operational value of MULTUPLICATION button"
    __MUL_VALUE = "star"
    # MULTUPLICATION button title
    __MUL_TITLE = "*"

    # Title for add to output 
    __ADD_TO_OUTPUT_TITLE = "Output += x"
    # Title for sub to output
    __SUB_TO_OUTPUT_TITLE = "x -= Output"
    # Title for mul to output
    __MUL_TO_OUTPUT_TITLE = "Output *= x"
    # Title for div to output
    __DIV_TO_OUTPUT_TITLE ="x //= Output"
    # Title for unary_minus to output
    __UNARY_TO_OUTPUT_TITLE = "Output = -Output"
    
    # Index value for button panel background color, to access the color in given gamma
    __BUTTON_PANEL_BACKGROUND_COLOR = 0
    # Index value for background color, to access the color in given gamma
    __BACKGROUND_COLOR = 1
    # Index value for button color, to access the color in given gamma
    __BUTTON_COLOR = 2
    # Index value for IO panel background color, to access the color in given gamma
    __IO_PANEL_BG_COLOR = 3
    # Index value for special button color, to access the color in given gamma
    __SPECIAL_BUTTON_COLOR = 4
    # Range offset for using range function to index through an iterable element
    __RANGE_OFFSET = 1
    # Main constructor.
    #  @parent@: The master widget of this @Calculator@ or @None@
    #  @base@: The number base for this @Calculator@.
    def __init__( self, master, title=__TITLE, base=__BASE ) :
        # initialise color gamma for the window
        self.__set_colors(get_color(base))
        # initialise operation engine
        self.__set_operation(base)
        # Initialise main calculator window.
        Tk.__init__( self, master)
        # Set title.
        self.title( title )
        # Set background color
        self.config(bg=self.__get_color(Calculator.__BUTTON_PANEL_BACKGROUND_COLOR))
        # Initialise __buttons.
        self.__buttons = []
        # Save @master@. Not used...
        self.__master = master
        # Finish rest of initialisation.
        self.__initialise( base=base )
        self.__iopanel.set( "" )
        
    def __set_colors(self,colors):
        # This is a setter for __colors
        self.__colors = colors
        
    def __get_color(self,index):
        # This is a getter for color.
        return self.__colors[index]

    def __set_button(self,button):
        # this is a setter for button list.
        self.__buttons += [button]

    def __get_buttons(self):
        # this is a getter for button list
        return self.__buttons

    def __set_operation(self,base):
        # this is a setter and initialiser for operation.
        self.__operation = Operation(base)

    def __get_operation(self):
        # this is a getter for operation
        return self.__operation

    # Utility method for initialising this @Calculator@'s components.
    #  @base@: the number base of this @Calculator@'s operations.
    def __initialise( self, base ) :
        # Initialise the IO panel component.
        self.__initialiseIOPanel( )
        # Initialise the digit panel component.
        self.__initialiseDigitPanel( base=base)
        # initialise menus
        self.__initialise_menu()

    # Initialise the digit panel widget of this @Calculator@.
    #  @base@: the number base of this @Calculator@'s operations.
    #  @row@: row number in grid layout of this @Calculator@.
    #  @col@: column number in grid layout of this @Calculator@.
    #  @digitsPerRow@: digits per row in grid layout of this @Calculator@.

    def __initialise_menu(self):
        # create a menu
        menu = Menu(self)
        # set menu
        self.__set_menu(menu)
        # initialise base menu
        self.__initialise_base_menu()
        # initialise operations menu
        self.__initialise_operations_menu()
        # initialise help menu
        self.__initialise_help_menu()
        # append menu to main window
        self.config(menu=menu)

    def __set_menu(self,menu):
        # this is a setter for menu
        self.__menu = menu
        
    def __get_menu(self):
        # this is a getter for menu
        return self.__menu        

    def __initialise_base_menu(self):
        # initialise base_menu, with 'menu' as parent
        base_menu = Menu(self.__get_menu())
        # append base menu to the parent
        self.__get_menu().add_cascade(label=Calculator.__BASE_MENU_TITLE,menu=base_menu)
        # create entries in base menu, for each base from __MIN_BASE to __MAX_BASE
        for base in range(Calculator.__MIN_BASE,Calculator.__MAX_BASE + Calculator.__RANGE_OFFSET):
            base_menu.add_radiobutton(label="%i"%base,command=lambda base=base: self.__set_base(base))
        

    def __initialise_operations_menu(self):
        # initialise operations menu, with 'menu' as parent
        operations_menu = Menu(self.__get_menu())
        # append operations menu to the parent
        self.__get_menu().add_cascade(label=Calculator.__OPERATIONS_MENU_TITLE,menu=operations_menu)
        
        # append add to output to the operations menu
        operations_menu.add_command(label=Calculator.__ADD_TO_OUTPUT_TITLE,command=lambda: self.__apply_to_output(Calculator.__ADD_VALUE))
        # append sub to output to the operations menu
        operations_menu.add_command(label=Calculator.__SUB_TO_OUTPUT_TITLE,command=lambda: self.__apply_to_output(Calculator.__SUB_VALUE))
        # append mul to output to the operations menu
        operations_menu.add_command(label=Calculator.__MUL_TO_OUTPUT_TITLE,command=lambda: self.__apply_to_output(Calculator.__MUL_VALUE))
        # append div to output to the operations menu
        operations_menu.add_command(label=Calculator.__DIV_TO_OUTPUT_TITLE,command=lambda: self.__apply_to_output(Calculator.__DIV_VALUE))
        # append unary to output to the operations menu
        operations_menu.add_command(label=Calculator.__UNARY_TO_OUTPUT_TITLE,command=self.__unary_apply_to_output)
        # add separator to the menu
        operations_menu.add_separator()
        # add display pending operations onto operations menu
        operations_menu.add_command(label=Calculator.__PREVIEW_TITLE,command=self.__display_pending)
        # add clear buffer onto operations menu
        operations_menu.add_command(label=Calculator.__CLEAR_BUFFER_TITLE,command=self.__clear_buffer)
        
    
    def __initialise_help_menu(self):
        # initialise help menu, with 'menu' as parent
        help_menu = Menu(self.__get_menu())
        # append help menu to the parent
        self.__get_menu().add_cascade(label=Calculator.__HELP_TITLE,menu=help_menu)
        # add help command to menu
        help_menu.add_command(label=Calculator.__HELP_TITLE,command=self.__get_help)
        # add a separator
        help_menu.add_separator()
        # add about popup to menu
        help_menu.add_command(label=Calculator.__ABOUT_TITLE,command=self.__get_about)

    def __set_base(self,base):
        # initialise a base for the caluclator.
        # set colors corresponding to given base
        self.__set_colors(get_color(base))
        # re-initialise iopanel with new colors
        self.__iopanel.destroy()
        self.__initialiseIOPanel()
        # reinitialise operation to a new base
        self.__set_operation(base)
        # set new background color
        self.config(bg=self.__get_color(Calculator.__BUTTON_PANEL_BACKGROUND_COLOR))
        # set the new color for iopanel
        self.__iopanel.config(bg=self.__get_color(Calculator.__BACKGROUND_COLOR))
        # destroy all the buttons
        for button in self.__get_buttons():
            button.destroy()
        # initialise new buttons that correspond to given base
        self.__initialiseDigitPanel(base)
    
    def __initialiseDigitPanel( self,
                                base,
                                row=__DIGIT_ROW,
                                col=__DIGIT_COL,
                                digitsPerRow=__DIGITS_PER_ROW ) :
        appendee = self.__iopanel
        self.__base = base
        self.__positioner = GridPositioner( row=row, col=col, columns=digitsPerRow )
        for digit in [ digit for digit in range( 1, base ) ] + [ 0 ] :
            button = Digit( master=self, digit=digit, appendee=appendee,color=self.__colors[Calculator.__BUTTON_COLOR ])
            self.__positioner.add( button )
            self.__set_button(button)
        self.__addSpecialDigitPanelButton( text=Calculator.__CLEAR_TITLE,
                                           command=self.__onClearButtonClick )
        self.__addSpecialDigitPanelButton( text=Calculator.__PUSH_TITLE,
                                           command=self.__onPushButtonClick )
        # add an apply button
        self.__addSpecialDigitPanelButton( text=Calculator.__APPLY_TITLE,
                                           command=self.__onApplyButtonClick )
        # add buttons for main operations 
        self.__addSpecialDigitPanelButton( text=Calculator.__ADD_TITLE,
                                           command=self.__onAddButtonClick )
        self.__addSpecialDigitPanelButton( text=Calculator.__DIV_TITLE,
                                           command=self.__onDivButtonClick )
        self.__addSpecialDigitPanelButton( text=Calculator.__MUL_TITLE,
                                           command=self.__onMulButtonClick )
        self.__addSpecialDigitPanelButton( text=Calculator.__SUB_TITLE,
                                           command=self.__onSubButtonClick )
        self.__addSpecialDigitPanelButton( text=Calculator.__UNARY_TITLE,
                                           command=self.__unary )

    def __onApplyButtonClick(self):
        # function called when apply button is clicked
        self.__iopanel.set(self.__get_operation().apply())

    def __onAddButtonClick(self):
        # function called when add button is clicked
        self.__get_operation().push_buffer(Calculator.__ADD_VALUE)

    def __onDivButtonClick(self):
        # function called when division button is clicked
        self.__get_operation().push_buffer(Calculator.__DIV_VALUE)

    def __onMulButtonClick(self):
        # function called when muluplication button is clicked
        self.__get_operation().push_buffer(Calculator.__MUL_VALUE)

    def __onSubButtonClick(self):
        # function called when subtraction button is clicked
        self.__get_operation().push_buffer(Calculator.__SUB_VALUE)      

    def __unary(self):
        # function called when unary miuns button is clicked
        return self.__get_operation().push_buffer(Calculator.__UNARY_VALUE)

    def __unary_apply_to_output(self):
        # function called when unary minus is applied to output of previous operation
        self.__get_operation().push_buffer(self.__iopanel.get_output())
        self.__get_operation().push_buffer(Calculator.__UNARY_VALUE)
        self.__onApplyButtonClick()

    def __apply_to_output(self,operation):
        # function called when operation is applied to output of previous operation
        self.__get_operation().push_buffer(self.__iopanel.get())
        self.__get_operation().push_buffer(self.__iopanel.get_output())
        self.__get_operation().push_buffer(operation)
        self.__onApplyButtonClick()

    # Utility method for adding additional button to the digit panel.
    #  @text@: the text on the button.
    #  @command@: the button's callback method.
    def __addSpecialDigitPanelButton( self, text, command ) :
        button = Button( master=self, text=text, command=command,background=self.__colors[Calculator.__SPECIAL_BUTTON_COLOR])
        self.__positioner.add( button )
        self.__set_button(button)

    # Initialise the IO panel widget of this @Calculator@.
    def __initialiseIOPanel( self ) :
        width = Calculator.__IO_PANEL_WIDTH 
        height = Calculator.__IO_PANEL_HEIGHT
        # create the IO panel.
        iopanel = IOPanel( master=self, width=width, height=height,color=self.__colors[Calculator.__IO_PANEL_BG_COLOR] )
        iopanel.config(bg=self.__colors[Calculator.__BACKGROUND_COLOR])
        row = Calculator.__IO_PANEL_ROW
        col = Calculator.__IO_PANEL_COL
        span = Calculator.__IO_PANEL_SPAN
        # Add the IO panel to the current crid layout.
        iopanel.grid( row=row, column=col, columnspan=span )
        # Save object reference to the IO panel for future use.
        self.__iopanel = iopanel

    # Callback method for push button
    def __onPushButtonClick( self ) :
        # REMOVE THE NEXT STATEMENT. IT'S ONLY HERE TO SHOW YOU
        # HOW TO GET THE TEXT IN THE INPUT FIELD.
        self.__get_operation().push_buffer(self.__iopanel.get( ) )
        self.__iopanel.reset( )

    # Callback method for clear button
    def __onClearButtonClick( self ) :
        self.__iopanel.reset( )

    def __display_pending(self):
        # function called when display pending popup is opened from menu operations
        PopUp(self.__get_operation().view_buffer(),Calculator.__DISPLAY_STACK_TITLE)

    def __get_help_contents(self):
        # get help contents for a popup
        # try reading it from a file
        try:
            file = open(Calculator.__HELP_FILE,Calculator.__HELP_READ_MODE)
            output = ""
            for line in file:
                output += line
        # if file cannot be read, get a backup string for help and display.
        except IOError:
            output = Calculator.__BACKUP_HELP
        return output

    def __clear_buffer(self):
        # clear the operation buffer
        self.__get_operation().clear_buffer()

    def __get_help(self):
        # popup help
        PopUp(self.__get_help_contents(),Calculator.__HELP_WINDOW_TITLE)

    def __get_about(self):
        # popup about
        PopUp(Calculator.__ABOUT_TEXT,Calculator.__ABOUT_WINDOW_TITLE)

if __name__ == "__main__" :
     calculator = Calculator( None)
     calculator.mainloop( )
