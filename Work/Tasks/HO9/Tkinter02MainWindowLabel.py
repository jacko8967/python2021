# ref video (min:sec) - https://www/youtube.com/watch?v=_1SNIrR1nZU
# ref - documentation https://docs.python.org/3/library/tkinter.html
# ref - documentation https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# ref - documentation http://www.tkdocs.com/tutorias/index.html


from tkinter import *

#main window (1:30 mins)
window = Tk()
window.title("Python Glossary")
window.configure(background="white")

#photo displayed with a Label (2:00) - display your photo add me.gif into the same folder as the .py file

photo = PhotoImage(file=r"Tasks\HO9\me.gif")

Label(window, image=photo, bg="white").grid(row=0,column=0,sticky=W)
# using grid (3:30 mins), sticky W = west // OR E = East

#run the main loop
window.mainloop()