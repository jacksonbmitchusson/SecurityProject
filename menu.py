from tkinter import *
from tkinter import ttk
import time
import threading

class Menu:
    #Closes the program
    def exit(window):
        window.destroy()

    #Creates the main menu, includes title, exit button 
    def __init__(self, window):
        frame = Frame(window, pady=20, padx=20)
        title = Label(frame, text="Evil-Twin Scanner", font=('Lucida Sans', 32), pady=10)
        start_button = Button(frame, text="Start Scanning", font=('Lucida Sans', 16), bg='#d6d6d6', activebackground='#d6d6d6', pady=(10), command= lambda: Menu.options(window)) 
        exit_button = Button(frame, text="Close", font=('Lucida Sans', 16), bg='#d6d6d6', activebackground='#d6d6d6', pady=(10), command= lambda: Menu.exit(window))
        title.pack()
        start_button.pack()
        exit_button.pack()
        frame.pack()

    def options(window):
        try:
            for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            email = StringVar()
            timer = StringVar()
            frame = Frame(window, pady=20, padx=20)
            title = Label(frame, text='Settings', font=('Lucida Sans', 24), pady=(5), padx=100)
            login_div = Frame(frame, pady=10)
            details = Label(login_div, text = "Please input an email if you would like an email to be sent when we detect an Evil Twin.", font=("Lucida Sans", 10), pady=3)
            more_details = Label(login_div, text = "If you don't want to receive an email, leave blank.", font = ("Lucida Sans", 10), pady=3)
            email_label = Label(login_div, text="Email",font=('Lucida Sans', 16), pady=3)
            timer_details = Label(login_div, text = "Please input how often the a scan should occur (in seconds).", font=("Lucida Sans", 10), pady=3)
            begin_button = Button(frame, text="Start Scanning", font=("Lucida Sans", 16), bg='#d6d6d6', activebackground='#d6d6d6', pady=(10), command= lambda: Menu.start_scanner(window, email.get(), timer.get()))
            details.pack()
            more_details.pack()
            email = Entry(login_div, textvariable=email, width=50)
            timer = Entry(login_div, textvariable=timer, width=10)
            email_label.pack()
            email.pack()
            timer_details.pack()
            timer.pack()
            title.pack()
            login_div.pack()
            begin_button.pack()
            frame.pack()

    def PBThread(progressbar, delay):
        th = threading.Thread(target=Menu.startPB, args=(progressbar, delay))
        th.start()

    def startPB(progressbar, delay):
        while True:
            progressbar['value'] += 1
            time.sleep(1)
            if progressbar['value'] == delay:
                progressbar['value'] = 0
                time.sleep(1)
            
    def start_scanner(window, email, delay):
        try:
            for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            frame = Frame(window, pady=20, padx=20)
            title = Label(frame, text="Now scanning!", font=("Lucida Sans", 24), pady=5, padx=100)
            text = Label(frame, text="The scanner is now running. Please feel free to leave the program in the background.", font=("Lucida Sans", 10), pady=3)
            moreText = Label(frame, text="If an Evil Twin is encountered, the program will give you an alert.", font=("Lucida Sans", 10), pady=3)
            evenMoreText = Label(frame, text="If chosen, it will also send an email to: " + email, font = ("Lucida Sans", 10), pady=3)
            exit_button = Button(frame, text="Close Program", font=('Lucida Sans', 16), bg='#d6d6d6', activebackground='#d6d6d6', pady=(10), command= lambda: Menu.exit(window))
            progressbar = ttk.Progressbar(frame, maximum=delay, length = 400)
            spacer1 = Label(frame, text="")
            spacer2 = Label(frame, text="")
            
            title.pack()
            text.pack()
            moreText.pack()
            evenMoreText.pack()
            spacer1.pack()
            progressbar.pack()
            spacer2.pack()
            exit_button.pack()
            frame.pack()

            Menu.PBThread(progressbar, int(delay))
        
