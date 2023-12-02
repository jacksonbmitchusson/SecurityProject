from tkinter import *

class Menu:
    #Closes the program
    def exit(window):
        window.destroy()

    #Creates the main menu, includes title, exit button 
    def __init__(self, window):
        frame = Frame(window, pady=20, padx=20)
        title = Label(frame, text="Evil-Twin Scanner", font=('Lucida Sans', 32), pady=10)
        start_button = Button(frame, text="Start Scanning", font=('Lucida Sans', 16), bg='#d6d6d6', activebackground='#d6d6d6', pady=(10), command= lambda: Menu.scan(window)) 
        exit_button = Button(frame, text="Close", font=('Lucida Sans', 16), bg='#d6d6d6', activebackground='#d6d6d6', pady=(10), command= lambda: Menu.exit(window))
        title.pack()
        start_button.pack()
        exit_button.pack()
        frame.pack()
