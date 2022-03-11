#Python Glossary GUI OO code
# ref video (min:sec) - https://www.youtube.com/watch?v=_lSNIrR1nZU
# ref - documentation https://docs.python.org/3/library/tkinter.html
# ref - documentation https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# ref - documentation http://www.tkdocs.com/tutorial/index.html


from tkinter import *                           # (0:50 mins)

# event functions (10:30 mins)
def onClickSubmitButton():                                      # submit button event handler
        userEnteredText = textbox.get()                         # get the entered text from the Entry text box
        userEnteredText = userEnteredText.lower()               #converts user entered text to lowercase
        outputTextField.delete(0.0, END)                        # (14:30 mins)delete all of the output field text contents
        
        if (userEnteredText.find(".") == -1) or (userEnteredText.find("@") == -1): #searches text entered by user for an "@" or "."
            definition = "Not a valid email address" #states that a "@" or "." could not be found 
            outputTextField.insert(END, definition) #prints statement in the text box
        elif userEnteredText in python_dictionary: #checks if the filtered text is in the dictionary
            definition = python_dictionary[userEnteredText] #assigns the text from the dictionary to a key
            outputTextField.insert(END, definition) #prints the key to the text box
        else:
            outputTextField.insert(END, "Email address not found in the dictionary") #if the filtered text contains a "@" or "." but is not in the dictionary, it will print this statement
        

def  onClickExitButton():                                       # (18:30 mins) exit button event handler        
    window.destroy()
    exit()
    

#main window (1:30 mins)
window = Tk()
window.title("Jack Robins, jacko8967@gmail.com")                 #replaced student ID in window title to display email address
window.configure(background="white")

#photo displayed with a Label  (2:00) - display your photo add me.gif into the same folder as the .py file
photo = PhotoImage(file="ASSESSMENTS\AssessmentTask2\Completed\me.gif") #modified code to use my provided me.gif
Label(window, image=photo, bg="white").grid(row=0,column=0,sticky=W) # using grid (3:30  mins) layout , sticky W = West // OR E = East

# display text using - Label  (05:30 mins)
Label(window, text="Enter an email address", bg="white", font="none 12 bold").grid(row=1,column=0,sticky=W) # using grid layout

# textbox for text entry - Entry (8:15 mins)
textbox = Entry(window, width=20, bg="white")
textbox.grid(row=2, column=0,sticky=W)          # grid position of textbox

# submit button - Button (9:30 mins) - calls onClickSubmitButton function when clicked
Button(window, text="SUBMIT", width=6, command=onClickSubmitButton ).grid (row=3,column=0, sticky = W)

#definitions - Label (11:50 mins)
Label(window, text="\n Definitions", bg="white", font="none 12 bold").grid(row=4,column=0,sticky=W) # using grid layout

# output textField - Text(12:40 mins)
outputTextField = Text(window, width=75, height=6, wrap=WORD, background="white")
outputTextField.grid(row=4, column=0,sticky=W)  # grid position of textField

# Dictionary (13:40 mins)
# Students ToDo Add 20 python expressions / items to the dictionary - Note last item should not have a ',' at the end
python_dictionary = { #modified dictionary to include email address
    'jacko8967@gmail.com' : 'jack robins',
    'john.smith@gmail.com' : 'john smith', #added first key value pair to dictionary
    'fred.jones@gmail.com' :'fred jones', #added second key value pair to dictionary
    'bill.strong@gmail.com' : 'bill strong' #added third and final key value pair to dictionary
}

# exit Labeland Button (17:00 mins) - - calls onClickExitButton function when clicked
Label(window, text="click to exit", bg="white", font="none 12 bold").grid(row=6,column=0,sticky=W) # using grid layout
Button(window, text="Exit", width=14, command=onClickExitButton ).grid (row=7,column=0, sticky = W) #changed onClickSubmitButton > onClickExitButton so that the correct function is executed

# run the main loop
window.mainloop()