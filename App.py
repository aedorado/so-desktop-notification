from Tkinter import *
from threading import *

class App(Thread):

    w = 400
    h = 100
    bgColor = '#77216F'

    def __init__(self, labeltext):

        self.root = Tk()
        self.root.overrideredirect(1)
        self.root.configure(background=self.bgColor)

        # get screen width and height
        ws = self.root.winfo_screenwidth() # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen

        # set the dimensions of the screen and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.w, self.h, ws - self.w, 0))

        # self.frame = Frame(self.root, width=self.w, height=self.h, borderwidth=2, relief=RAISED)
        # self.frame.pack_propagate(False)
        # self.frame.pack()
        # self.frame.configure(background = '#77216F')

        self.label = Label(self.root, text=labeltext, fg='#ffffff', bg=self.bgColor)
        self.label.pack(pady=20)

        self.bQuit = Button(self.root, text="X", command=self.root.quit)
        self.bQuit.place(x=375, y=0, height=25, width=25)
        self.bQuit.configure(background = '#77216F')
        # self.bHello = Button(self.frame, text="Hello", command=self.hello)
        # self.bHello.pack(pady=20)
        
        # self.root.after(8000, self.closeSelf)
        self.root.after(15000, lambda: self.root.destroy())
        self.root.mainloop()
        # Thread.__init__(self)

    def closeSelf(self):
        self.root.destroy()

    def hello(self):
        tkMessageBox.showinfo("Popup", "Hello!")

# app = App('hello').root.mainloop()