from tkinter import *
class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.myCanvas = Canvas(width=150, height=150)
        self.myCanvas.create_text(10, 10, text="Hello World", width=70, fill="blue", anchor="nw", justify="center", font=("Times", 16))
        self.myCanvas.grid()
frame02 = MyFrame()
frame02.mainloop()
