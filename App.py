from Tkinter import *
from threading import *
import tkMessageBox
import webbrowser

class App():

    w = 400
    h = 100
    bgColor = '#77216F'

    def __init__(self, labeltext):

        self.root = Tk()
        self.root.overrideredirect(1)
        self.root.configure(background=self.bgColor)

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen

        # set the dimensions of the screen and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws - self.w, 0))

        self.label = Label(self.root, text=labeltext, fg='#ffffff', bg=self.bgColor, wraplength=350)
        self.label.pack(pady=20)

        self.bQuit = Button(self.root, text="X", command=self.closeSelf)
        self.bQuit.place(x=375, y=0, height=25, width=25)
        self.bQuit.configure(background = '#77216F')

        self.label.bind("<Button-1>", self.bopen)
        
        self.root.after(5000, lambda: self.root.destroy())
        self.url = labeltext[labeltext.find('\n') + 1:]
        self.root.lift()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.root.mainloop()

    def closeSelf(self):
        self.root.destroy()

    def bopen(self, event):
        webbrowser.open(self.url)

# app = App('hello').root.mainloop()