from tkinter import *
import menu

def exit(window):
    window.destroy()
    
def createWindow():
    window = Tk()
    window.title("Evil-Twin Scanner")
    window.geometry('600x400')
    window.minsize(width=600, height=400)
    return window

window = createWindow()
menu.Menu(window)
window.mainloop()
