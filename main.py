from tkinter import *
import menu
#from parts import scanner

def exit(window):
    window.destroy()
    
def createWindow():
    window = Tk()
    window.title("Evil-Twin Scanner")
    window.geometry('500x500')
    window.minsize(width=500, height=500)
    return window

window = createWindow()
menu.Menu(window)
window.mainloop()
