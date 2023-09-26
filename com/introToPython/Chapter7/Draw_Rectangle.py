from time import sleep
from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.myCanvas = Canvas(width=500, height=500, background="green")
        self.myCanvas.grid()
        self.myCanvas.create_rectangle(10, 10, 50, 50)
        self.myCanvas.update()
        sleep(1)
        self.myCanvas.create_rectangle(30, 30, 60, 60)


frame = MyFrame()
# frame.myCanvas.create_rectangle(10, 10, 100, 100)
# frame.myCanvas.update()
# sleep(1)
# frame.myCanvas.create_rectangle(30, 30, 100, 100)
frame.mainloop()