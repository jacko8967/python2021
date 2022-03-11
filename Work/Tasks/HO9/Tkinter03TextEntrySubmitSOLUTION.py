# ref video (min:sec) - https://www/youtube.com/watch?v=_1SNIrR1nZU
# ref - documentation https://docs.python.org/3/library/tkinter.html
# ref - documentation https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# ref - documentation http://www.tkdocs.com/tutorias/index.html


from tkinter import *

# event functions (10:30 mins)
def onClickSubmitButton():                              # submit button event handler
    userEnteredText = textbox.get()                     # get entered text from Entry text box
    outputTextField.delete(0.0, END)                    # (14:30 mins) delete all text in output box
    outputTextField.insert(END, userEnteredText.lower())        # (15:50 mins) output the user entered text


#main window (1:30 mins)
window = Tk()
window.title("Python Glossary")
window.configure(background="white")


# display text using - label (05:30 mins)
Label(window, text="Enter a string and press submit", bg="white", font="none 12 bold").grid(row=0, column=0, sticky=W)
# using grid layout



# textbox for text entry - Entry (8:15 mins)
textbox = Entry(window, width=20, bg="white")
textbox.grid(row=1, column=0) #grid position of textbox

#submit button - Button (9:30 mins) - calls onClickSubmitButton function when clicked
Button(window, text="SUBMIT", width=6, command=onClickSubmitButton).grid(row=1, column=1, sticky=W)

#definitions - label (11:50 mins)
Label(window, text="\n Your string", bg="white", font="none 12 bold").grid(row=2, column=0)
#using grid layout


#output text field - Text (12:40 mins)
outputTextField = Text(window, width=75, height=6, wrap=WORD, background="white")
outputTextField.grid(row=2, column=1)
#grid position of textfield


#run the main loop
window.mainloop()